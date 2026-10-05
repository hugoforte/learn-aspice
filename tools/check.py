"""Check the course's cross-file rules that no browser shows.

- reference/glossary.html matches GLOSSARY.md's ASPICE terms word for word,
  in the same groups and order.
- Every "Taught in" / "First used in" pointer names a heading on its page.
- Every Anki deck row has three fields, a GUID of its own lesson, no "&"
  and no straight double quote, and no GUID appears twice.
- Every page's tags are balanced.

Needs only the standard library. Run from anywhere: python tools/check.py
Exits 1 and lists every problem when any rule is broken.
"""

import glob
import html
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOID_TAGS = {"meta", "link", "br", "img", "input", "hr", "col", "source", "wbr"}
IMPLICITLY_CLOSED = {"p", "li"}

problems = []


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def context_terms():
    """(group, term, definition, avoid) for each ASPICE term, in file order."""
    lines = read("GLOSSARY.md").split("\n")
    terms, group = [], None
    for i, line in enumerate(lines):
        if line.startswith("### "):
            group = line[4:]
        match = re.match(r"^\*\*(.+)\*\*:$", line)
        if match and group != "The course":
            avoid = None
            if lines[i + 2].startswith("_Avoid_: "):
                avoid = lines[i + 2][len("_Avoid_: "):]
            terms.append((group, match.group(1), lines[i + 1], avoid))
    return terms


def glossary_terms():
    """(group, term, definition, avoid) for each glossary entry, in file order."""
    terms, group = [], None
    for line in read("reference/glossary.html").split("\n"):
        heading = re.match(r"^\s*<h2>(.+)</h2>$", line)
        if heading:
            group = html.unescape(heading.group(1))
        entry = re.match(r"^\s*<p><strong>(.+?)</strong>: (.+)</p>$", line)
        if entry:
            body = html.unescape(entry.group(2))
            definition, _, avoid = body.partition(" <em>Avoid:</em> ")
            terms.append((group, html.unescape(entry.group(1)), definition, avoid or None))
    return terms


def lowercase_first_word(text):
    """The glossary lowercases a definition's first word when it is ordinary."""
    word = text.split(" ")[0]
    if word[0].isupper() and (word[1:].islower() or len(word) == 1):
        return text[0].lower() + text[1:]
    return text


def check_glossary():
    expected = context_terms()
    actual = glossary_terms()
    if len(expected) != len(actual):
        problems.append(f"glossary: {len(actual)} terms, GLOSSARY.md has {len(expected)}")
    for (group, term, definition, avoid), (g_group, g_term, g_definition, g_avoid) in zip(expected, actual):
        where = f"glossary: {term!r}"
        if term != g_term:
            problems.append(f"{where}: glossary has {g_term!r} in its place")
            continue
        if group != g_group:
            problems.append(f"{where}: under {g_group!r}, GLOSSARY.md groups it under {group!r}")
        if lowercase_first_word(definition) != g_definition:
            problems.append(f"{where}: definition differs from GLOSSARY.md")
        # The glossary quotes the avoided words, which GLOSSARY.md leaves bare.
        if (avoid or "") != (g_avoid or "").replace('"', "").removesuffix("."):
            problems.append(f"{where}: avoid list differs from GLOSSARY.md")


class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.headings, self._text = [], None

    def handle_starttag(self, tag, attrs):
        if re.fullmatch(r"h[1-4]", tag):
            self._text = ""

    def handle_endtag(self, tag):
        if re.fullmatch(r"h[1-4]", tag) and self._text is not None:
            self.headings.append(" ".join(self._text.split()))
            self._text = None

    def handle_data(self, data):
        if self._text is not None:
            self._text += data


def check_pointers():
    context = read("GLOSSARY.md")
    for label, path in re.findall(r"\[([^\]]+ · [^\]]+)\]\(([^)#]+)\)", context):
        heading = label.split(" · ", 1)[1]
        if heading == "opening":
            continue
        if not os.path.exists(os.path.join(ROOT, path)):
            problems.append(f"GLOSSARY.md: [{label}] points at missing {path}")
            continue
        parser = Headings()
        parser.feed(read(path))
        if heading not in parser.headings:
            problems.append(f"GLOSSARY.md: [{label}] names no heading in {path}")


def check_decks():
    guids = Counter()
    for path in sorted(glob.glob(os.path.join(ROOT, "anki", "*.txt"))):
        name = os.path.basename(path)
        lesson = name[2:4]
        with open(path, encoding="utf-8") as f:
            rows = f.read().split("\n")
        for number, row in enumerate(rows, 1):
            if not row or row.startswith("#"):
                continue
            where = f"{name}:{number}"
            fields = row.split("|")
            if len(fields) != 3:
                problems.append(f"{where}: {len(fields)} fields, not 3")
                continue
            guid = fields[2]
            guids[guid] += 1
            if not re.fullmatch(rf"aspice-{lesson}-\d\d", guid):
                problems.append(f"{where}: GUID {guid!r} is not aspice-{lesson}-NN")
            if "&" in row:
                problems.append(f"{where}: contains &")
            if '"' in row:
                problems.append(f"{where}: contains a straight double quote")
    for guid, count in guids.items():
        if count > 1:
            problems.append(f"anki: GUID {guid} used {count} times")


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open, self.errors = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.open.append(tag)

    def handle_endtag(self, tag):
        if self.open and self.open[-1] == tag:
            self.open.pop()
        elif tag not in IMPLICITLY_CLOSED:
            line = self.getpos()[0]
            self.errors.append(f"line {line}: </{tag}> closes <{self.open[-1] if self.open else 'nothing'}>")


def check_tags():
    pages = glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "*", "*.html"))
    for path in sorted(pages):
        parser = TagBalance()
        with open(path, encoding="utf-8") as f:
            parser.feed(f.read())
        name = os.path.relpath(path, ROOT).replace(os.sep, "/")
        problems.extend(f"{name}: {error}" for error in parser.errors)
        if parser.open:
            problems.append(f"{name}: unclosed {', '.join('<' + t + '>' for t in parser.open)}")


check_glossary()
check_pointers()
check_decks()
check_tags()

for problem in problems:
    print(problem)
if problems:
    sys.exit(1)
print("All checks pass.")
