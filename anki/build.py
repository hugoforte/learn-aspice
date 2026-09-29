"""Build aspice-4.1.apkg, one package holding every lesson's deck.

The per-lesson text files are the source. This imports them into a scratch
collection with Anki's own importer, so the package carries the same GUIDs,
decks and tags as a text import, then exports the parent deck.

Needs Anki's Python package: pip install anki
Run from anywhere: python anki/build.py
"""

import glob
import os
import sys
import tempfile

from anki.collection import (
    Collection,
    DeckIdLimit,
    ExportAnkiPackageOptions,
    ImportCsvRequest,
)

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT_DECK = "ASPICE 4.1"
OUT = os.path.join(HERE, "aspice-4.1.apkg")

with tempfile.TemporaryDirectory() as scratch:
    col = Collection(os.path.join(scratch, "build.anki2"))
    for path in sorted(glob.glob(os.path.join(HERE, "*.txt"))):
        metadata = col.get_csv_metadata(path=path, delimiter=None)
        log = col.import_csv(ImportCsvRequest(path=path, metadata=metadata)).log
        skipped = len(log.conflicting) + len(log.first_field_match) + len(log.missing_notetype) + len(log.missing_deck) + len(log.empty_first_field) + len(log.duplicate)
        if skipped:
            sys.exit(f"{os.path.basename(path)}: {skipped} notes not imported cleanly")
        print(f"{os.path.basename(path)}: {len(log.new)} cards")
    deck_id = col.decks.id_for_name(PARENT_DECK)
    if deck_id is None:
        sys.exit(f"no deck named {PARENT_DECK}")
    count = col.export_anki_package(
        out_path=OUT,
        options=ExportAnkiPackageOptions(with_scheduling=False, with_deck_configs=False, with_media=False, legacy=True),
        limit=DeckIdLimit(deck_id),
    )
    col.close()

print(f"{count} notes -> {os.path.relpath(OUT)}")
