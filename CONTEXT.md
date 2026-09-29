# Automotive SPICE 4.1: the vital 20 %

The vocabulary of a self-paced course on the Automotive SPICE 4.1 process assessment model. Each term is used in exactly this sense in every lesson, reference sheet and Anki deck. [reference/glossary.html](reference/glossary.html) is the learner's copy of the ASPICE terms below, and a change here goes there in the same commit.

"Taught in" names the page, then the heading, where a term is explained; "First used in" marks a name the lessons use without explaining. The PAM and the VDA Guidelines are cited by printed page; see [NOTES.md](NOTES.md).

## Language

### The model

**PRM (process reference model)**:
The set of processes, each with a purpose and outcomes.
_Avoid_: the standard, the model
Taught in: [L01 · A grid, not a score](lessons/0001-two-axes-of-a-rating.html)

**PAM (process assessment model)**:
The PRM plus the indicators an assessor uses to rate it.
_Avoid_: the checklist, the model
Taught in: [L01 · A grid, not a score](lessons/0001-two-axes-of-a-rating.html)

**VDA Guidelines**:
The VDA's companion to the PAM: how to interpret it, and the rating rules assessors apply. Always plural.
_Avoid_: the Guideline
Taught in: [L08 · How assessors rate](lessons/0008-how-assessors-rate.html)

**Process**:
In the PAM, a distinct set of related goals with a purpose and outcomes; not a workflow and not a lifecycle phase.
_Avoid_: phase, workflow
Taught in: [L01 · The PAM is the WHAT](lessons/0001-two-axes-of-a-rating.html), [L11 · ASPICE has processes, not phases](lessons/0011-lifecycles-gates-and-approvals.html)

**WHAT / HOW / DOING**:
The goals the PAM states / the methods and tools an organisation chooses / the actual performance on real work. Assessors rate the WHAT, evidenced by the DOING.
Taught in: [L01 · The PAM is the WHAT](lessons/0001-two-axes-of-a-rating.html), [Capability levels · WHAT · HOW · DOING](reference/capability-levels.html)

**Purpose**:
The one-sentence reason a process exists.
Taught in: [L02 · The anatomy of a process](lessons/0002-reading-a-process.html)

**Outcome**:
An observable result of achieving a process's purpose. PA 1.1 rates outcomes.
Taught in: [L02 · The anatomy of a process](lessons/0002-reading-a-process.html)

**Process dimension / capability dimension**:
The two axes of a rating: which processes are assessed, and how capable each one is.
Taught in: [L01 · A grid, not a score](lessons/0001-two-axes-of-a-rating.html)

**Recommended VDA Scope**:
The VDA's recommended process selection. It is the base (MAN.3, SUP.1, SUP.8, SUP.9, SUP.10) plus at least one plug-in, with flex processes added as the purpose needs.
_Avoid_: the eleven processes, ASPICE scope
Taught in: [L03 · Base plus plug-in](lessons/0003-the-vda-scope.html)

**Plug-in**:
One domain's engineering processes, added to the base: SYS.2–SYS.5, SWE.1–SWE.6, HWE.1–HWE.4, or MLE.1–MLE.4 with SUP.11. The Guidelines count system as one domain among four; PAM Annex C.1 keeps the system V above the domains.
Taught in: [L03 · Base plus plug-in](lessons/0003-the-vda-scope.html)

**Flex process**:
A process outside the base and the plug-ins of the recommended VDA Scope, added when the assessment purpose needs it. Examples are SYS.1, VAL.1, SPL.2 and MAN.5.
_Avoid_: optional process, outside the VDA Scope
Taught in: [L03 · Base plus plug-in](lessons/0003-the-vda-scope.html), [L16 · Who validates](lessons/0016-validation.html)

### Indicators

**Indicator**:
Something an assessor looks for when rating: a practice or an information item.
Taught in: [L02 · The anatomy of a process](lessons/0002-reading-a-process.html)

**Base practice (BP)**:
A process-specific activity indicator for level 1.
Taught in: [L02 · The anatomy of a process](lessons/0002-reading-a-process.html)

**Generic practice (GP)**:
An activity indicator for a process attribute, applied identically to every process.
Taught in: [L05 · Generic practices apply to every process](lessons/0005-level-2-managing-performance.html)

**Information item (II)**:
What an assessor looks for, described by its characteristics in PAM Annex B and numbered (13-13, 17-57 and so on). It is not a document anyone must write.
_Avoid_: required document, record
Taught in: [L02 · Information items are not documents to write](lessons/0002-reading-a-process.html)

**Work product**:
What the organisation actually produced, including tool content such as Jira tickets, commits and CI results.
_Avoid_: document, deliverable
Taught in: [L02 · Information items are not documents to write](lessons/0002-reading-a-process.html), [L06 · Which work products count](lessons/0006-level-2-managing-work-products.html)

**Record**:
A work product held in a tool, such as a ticket, a review approval or a Markdown file with front-matter. It is never a synonym for information item.
Taught in: [L10 · Seat-Heat goes docs-as-code](lessons/0010-automated-checks.html)

**Objective evidence**:
Work products and testimony, the only two sources a rating may rest on.
Taught in: [L02 · Information items are not documents to write](lessons/0002-reading-a-process.html)

**Testimony**:
What the people doing the work say in interviews: the second source of objective evidence.
_Avoid_: interview notes
Taught in: [L02 · Information items are not documents to write](lessons/0002-reading-a-process.html)

### The capability dimension

**Capability level**:
0 Incomplete, 1 Performed, 2 Managed, 3 Established, 4 Predictable or 5 Innovating. Derived from PA ratings, for one process.
_Avoid_: maturity level, which rates organisations in other models
Taught in: [L01 · Six levels, nine attributes](lessons/0001-two-axes-of-a-rating.html)

**Capability profile**:
The result of an assessment: one capability level per assessed process.
_Avoid_: score, overall level
Taught in: [L01 · A grid, not a score](lessons/0001-two-axes-of-a-rating.html)

**Process attribute (PA)**:
A measurable property of capability. There are nine: PA 1.1, then two per level from 2 to 5.
Taught in: [L01 · Six levels, nine attributes](lessons/0001-two-axes-of-a-rating.html)

**N / P / L / F**:
Not (≤ 15 %), partially (≤ 50 %), largely (≤ 85 %) and fully (> 85 %) achieved. P and L may be refined to P−/P+ and L−/L+.
Taught in: [L01 · Each attribute is rated N, P, L or F](lessons/0001-two-axes-of-a-rating.html), [Capability levels · Rating scale](reference/capability-levels.html)

**Level rule**:
Level n needs its own PAs rated L or F and every lower PA rated F.
Taught in: [L01 · The one rule that turns ratings into a level](lessons/0001-two-axes-of-a-rating.html)

**Downrate**:
Rate an indicator or attribute lower because of a weakness.
Taught in: [L08 · 5. Rating rules and weakness statements](lessons/0008-how-assessors-rate.html)

**Process performance objective**:
A target for how one process is performed (GP 2.1.1). It is not a project goal and not a restated outcome.
Taught in: [L05 · The keystone: process performance objectives](lessons/0005-level-2-managing-performance.html)

**Process performance strategy**:
How a process will be performed to meet its objectives (GP 2.1.2). Tool-enforced workflows and CI can be one.
Taught in: [L05 · The PA 2.1 loop](lessons/0005-level-2-managing-performance.html)

**Review evidence (13-19)**:
The information item a review leaves: the object and its version, the reviewers and their roles, the date, the status, the criteria and the non-conformances found.
Taught in: [L06 · Review evidence has a shape](lessons/0006-level-2-managing-work-products.html)

**Status model**:
The defined states a work product moves through, part of its storage and control (GP 2.2.2).
Taught in: [L06 · Four generic practices, two pairs](lessons/0006-level-2-managing-work-products.html)

**Standard process**:
The organisation-wide reference process, with tailoring guidelines (PA 3.1).
_Avoid_: the standard, the handbook (the company's own word in L07's story, never the course's)
Taught in: [L07 · Two kinds of process](lessons/0007-level-3-standard-and-defined-process.html)

**Defined process**:
A project's tailored instance of the standard process (PA 3.2).
Taught in: [L07 · Two kinds of process](lessons/0007-level-3-standard-and-defined-process.html)

**Tailoring guideline**:
Predefined, unambiguous criteria for deriving a defined process from the standard process, naming who tailors and who approves.
Taught in: [L07 · PA 3.1: the standard process](lessons/0007-level-3-standard-and-defined-process.html)

**Waiver**:
An approved one-off deviation from the standard process. A recurring waiver for the same deviation is a sign the standard process needs changing.
Taught in: [L07 · PA 3.1: the standard process](lessons/0007-level-3-standard-and-defined-process.html)

**Competency**:
What a role requires people to know and be able to do (GP 3.1.2), and the basis for assigning people to roles (GP 3.2.2).
Taught in: [L07 · PA 3.1: the standard process](lessons/0007-level-3-standard-and-defined-process.html), [L07 · PA 3.2: deploying it](lessons/0007-level-3-standard-and-defined-process.html)

### The V and engineering

**V-model**:
A picture of which work products must be consistent and traceable with which. It is not a sequence of phases.
_Avoid_: V-model phases
Taught in: [L11 · ASPICE has processes, not phases](lessons/0011-lifecycles-gates-and-approvals.html), [L16 · The whole V, in one table](lessons/0016-validation.html)

**Left leg / right leg**:
The processes that specify (requirements, architecture, design) and the processes that check what was specified (verification, validation).
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html), [L14 · The right leg: one pattern, used five times](lessons/0014-the-v-system-level.html)

**Bidirectional traceability**:
Links that can be followed both ways between related items.
_Avoid_: using it to mean consistent
Taught in: [L04 · Two words, two different demands](lessons/0004-consistency-and-traceability.html)

**Unidirectional traceability**:
Links followed one way only. This is sufficient when a validation measure derives from a legal or homologation requirement (VAL.1.BP4).
Taught in: [L16 · What VAL.1 asks for](lessons/0016-validation.html)

**Consistency**:
Linked items actually agree in content. Links alone don't prove it.
Taught in: [L04 · Two words, two different demands](lessons/0004-consistency-and-traceability.html)

**Connection point**:
A consistency or traceability BP: the only way a weakness in one process can count against another.
Taught in: [L08 · 3. Each process is rated on its own](lessons/0008-how-assessors-rate.html)

**Cluster**:
A group of requirements traced as one. Cluster-level tracing is not downrated (TAC.RL.1).
Taught in: [L04 · What counts as evidence, and what doesn't have to](lessons/0004-consistency-and-traceability.html)

**System**:
Whatever the team delivers as its product, whether a mechatronic system, an ECU or a chip. SYS processes are not tied to a fixed product level.
Taught in: [L14 · Seat-Heat's company bids for the whole ECU](lessons/0014-the-v-system-level.html)

**System element**:
A building block of the system architecture, whether logical (a design object) or physical (a sensor, a mechanical part, a software executable).
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**Stakeholder requirement (SYS.1)**:
An agreed requirement from a stakeholder: the customer's, but also the supplier's own and legal or regulatory ones. System requirements are derived from them.
_Avoid_: customer requirement, when other stakeholders count too
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**System requirement (SYS.2)**:
A functional or non-functional requirement on the system, derived from the stakeholder requirements.
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**Software requirement (SWE.1)**:
A requirement on the software, derived from the system requirements and architecture, or from stakeholder requirements in software-only development.
Taught in: [L15 · The left leg: requirements, architecture, design and code](lessons/0015-the-v-software-level.html)

**Static aspects / dynamic aspects**:
An architecture's elements, interfaces and relationships / its behaviour and interactions in each mode. An architecture needs at least one view of each.
_Avoid_: diagrams
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**Hardware-software interface (HSI)**:
Which pins, signals and timing the software sees. It is defined at system level in SYS.3 and is an input to the software requirements.
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**Special characteristic**:
A property of a non-software system element derived in the system architecture (SYS.3.BP3) and communicated to all affected parties.
Taught in: [L14 · The left leg: from needs to an architecture](lessons/0014-the-v-system-level.html)

**Software component**:
What the software architecture (SWE.2) decomposes the software into, down to the lowest-level components.
Taught in: [L15 · Three words first: element, component, unit](lessons/0015-the-v-software-level.html)

**Software unit**:
What the detailed design (SWE.3) decomposes a component into, not subdivided further. First a design idea, not a file or a function; under verification it is represented by source code or object files.
_Avoid_: module (Seat-Heat's own word in L04's story, never the course's)
Taught in: [L15 · Three words first: element, component, unit](lessons/0015-the-v-software-level.html)

**Software element**:
A component or a unit, seen as something that is integrated (SWE.5).
_Avoid_: element, on its own, for anything else
Taught in: [L15 · Three words first: element, component, unit](lessons/0015-the-v-software-level.html)

**Detailed design**:
What each software unit shall do and how it interacts with other units. It is not a picture of the code.
Taught in: [L15 · The left leg: requirements, architecture, design and code](lessons/0015-the-v-software-level.html)

**Coding principles**:
Rules units are developed to (SWE.3.BP3), such as no implicit type conversions, one entry and one exit, and range checks. A level 1 matter.
Taught in: [L15 · The left leg: requirements, architecture, design and code](lessons/0015-the-v-software-level.html)

### Verification and validation

**Verification measure**:
Any check against a specification: a test, measurement, calculation, simulation, review or analysis. ASPICE 4 says "verification" rather than "testing".
_Avoid_: test, when any other kind of measure would do
Taught in: [L14 · The right leg: one pattern, used five times](lessons/0014-the-v-system-level.html)

**Verification pattern**:
The five steps every right-leg process follows: specify measures, select them, perform and record, trace, and summarise and communicate.
Taught in: [L14 · The right leg: one pattern, used five times](lessons/0014-the-v-system-level.html)

**Automated verification measure**:
A measure run by scripts or programs. Its definition must address their correctness, completeness and consistency.
_Avoid_: test code, as if it were exempt
Taught in: [L14 · The right leg: one pattern, used five times](lessons/0014-the-v-system-level.html)

**Exploratory test**:
A verification measure, or under VAL.1 a validation measure (Guidelines p. 164), with no specification to trace to. Not downrated for that, but it must trace to its results.
Taught in: [L14 · The right leg: one pattern, used five times](lessons/0014-the-v-system-level.html)

**Component verification / integration verification**:
SWE.5's two halves: each component's behaviour and interfaces, then how the integrated elements work together.
Taught in: [L15 · The right leg: units, components, the whole software](lessons/0015-the-v-software-level.html)

**Code coverage**:
Accompanying information on how complete the chosen tests are. Never a verification objective in itself.
Taught in: [L15 · The right leg: units, components, the whole software](lessons/0015-the-v-software-level.html)

**Validation (VAL.1)**:
Evidence that the end product meets its users' intended-use expectations in its operational target environment. The test is not whether a requirement exists but whether objective measurement settles it (verification) or it takes a judgement of what users need, made by end users or their representatives or approximated, for instance by accident simulations (validation). A simulation checked against a specification is still verification. It does not apply to pure embedded software, an ECU or a drive.
Taught in: [L16 · Verification and validation are different questions](lessons/0016-validation.html), [L16 · Who validates](lessons/0016-validation.html)

**Validation measure**:
A check against intended use, such as use-case testing under real-life conditions, end-user trials, panel or blind tests, or expert panels.
Taught in: [L16 · Verification and validation are different questions](lessons/0016-validation.html)

**End product**:
A product people use directly, with a direct end-user interface. It is the only thing VAL.1 validates.
Taught in: [L16 · Who validates](lessons/0016-validation.html)

### Support, change and release

**Quality assurance (SUP.1)**:
Independent, objective assurance that work products and processes meet their criteria, with non-conformances resolved.
Taught in: [L03 · The eleven, one line each](lessons/0003-the-vda-scope.html)

**Independence**:
SUP.1's demand that quality assurance is unbiased and free of conflicts of interest: no self-monitoring, and not done by the project's own manager or developers. ASPICE demands it of no other process.
_Avoid_: using it for GEN.RL.1, or for verification
Taught in: [L11 · Two things gates are often credited with, wrongly](lessons/0011-lifecycles-gates-and-approvals.html)

**Non-conformance**:
A deviation found against defined criteria, by a review or by quality assurance.
Taught in: [L06 · Review evidence has a shape](lessons/0006-level-2-managing-work-products.html)

**Configuration item**:
A work product, or a group of them, managed as one entity under SUP.8. For AI assistance, the Guidelines' examples include prompts as new configuration items and version control of AI tools, models and their settings.
Taught in: [L12 · What the Guidelines say](lessons/0012-ai-generated-work-products.html)

**Baseline**:
A defined, consistent, read-only set of configuration items at a point in time, serving as input for the affected parties.
_Avoid_: snapshot, tag
Taught in: [L11 · Seat-Heat's gates, and where each lands](lessons/0011-lifecycles-gates-and-approvals.html)

**Problem (SUP.9)**:
Something wrong, to be analysed and tracked to closure.
Taught in: [L03 · The two pairs people confuse](lessons/0003-the-vda-scope.html)

**Change request (SUP.10)**:
A wanted change, analysed, approved before implementation and traced to what it affects.
_Avoid_: CR in prose; bug or defect, for a change request
Taught in: [L03 · The two pairs people confuse](lessons/0003-the-vda-scope.html)

**CCB (change control board)**:
A decision authority that approves change requests (SUP.10.BP3). The PAM gives a CCB as one example mechanism, and the Guidelines call any such authority a CCB for simplicity. It represents all affected disciplines and required stakeholders, with authority to decide, and there may be more than one.
_Avoid_: approving body; approval authority, except when quoting the Guidelines' rules
Taught in: [L09 · SUP.10 in brief](lessons/0009-capstone-assess-seat-heat.html)

**Lifecycle**:
The project's own phases, gates and order (MAN.3.BP2): a HOW. ASPICE defines none.
_Avoid_: ASPICE phases
Taught in: [L11 · ASPICE has processes, not phases](lessons/0011-lifecycles-gates-and-approvals.html)

**Gate**:
A decision point in a project's lifecycle, such as "Requirements agreed". A stage-gate model is a lifecycle, and going back through a gate is iteration, not a deviation.
Taught in: [L11 · ASPICE has processes, not phases](lessons/0011-lifecycles-gates-and-approvals.html)

**Gate approval**:
The decision to pass a gate: a lifecycle HOW. A complete, consistent baseline can support one (SUP.8.BP7).
_Avoid_: release approval
Taught in: [L11 · Seat-Heat's gates, and where each lands](lessons/0011-lifecycles-gates-and-approvals.html)

**Release approval (SPL.2.BP5)**:
Approval against release criteria before delivery. An assessor looks for it as information item 13-13: the date and the approver's name and role.
_Avoid_: gate approval, sign-off
Taught in: [L11 · A new process for the course: SPL.2 Product Release](lessons/0011-lifecycles-gates-and-approvals.html)

**Release note**:
What SPL.2 delivers alongside a release to say what it contains (information item 11-03).
Taught in: [L11 · A new process for the course: SPL.2 Product Release](lessons/0011-lifecycles-gates-and-approvals.html)

### Automation and AI

**Docs-as-code**:
Keeping requirements, architecture and verification as files in Git, with trace IDs in their front-matter. A HOW.
Taught in: [L10 · Seat-Heat goes docs-as-code](lessons/0010-automated-checks.html)

**Structural check / semantic check**:
An automated check that the trace graph is well-formed / a recorded review that linked items agree in content. Only a semantic check shows consistency.
_Avoid_: compliance check
Taught in: [L10 · What no structural check can establish](lessons/0010-automated-checks.html)

**Orphan**:
A record nothing traces to. A checker flags it, and must accept a recorded justification.
Taught in: [L10 · What each check supports](lessons/0010-automated-checks.html)

**Compliance**:
An assessor's judgement about a process. No check or tool can establish it.
Taught in: [L10 · What no structural check can establish](lessons/0010-automated-checks.html)

**Coding agent**:
An AI tool that drafts work products, such as requirements, code and tests, usually as pull requests. Using one is a HOW.
_Avoid_: agent, for the course's teacher
Taught in: [L12 · Seat-Heat adopts coding agents](lessons/0012-ai-generated-work-products.html)

**Self-monitoring**:
The producer of a work product checking it. It can support a review, but never counts as quality assurance.
Taught in: [L12 · Four consequences worth designing for](lessons/0012-ai-generated-work-products.html)

### Assessment

**Assessment purpose**:
Why the assessment is done, such as supplier evaluation or an improvement baseline. The scope is defined to cover it.
Taught in: [Assessment rules · Scope first](reference/assessment-rules.html)
First used in: [L03 · Base plus plug-in](lessons/0003-the-vda-scope.html)

**Assessment scope**:
Four things: organisational-unit boundaries, the processes, the target capability level per process, and the process context. The purpose is not part of it.
Taught in: [L08 · 1. Everything starts from the scope](lessons/0008-how-assessors-rate.html)

**Sponsor**:
Whoever commissions the assessment and agrees its scope. A process leaves the scope only with the sponsor's approval.
Taught in: [L03 · Base plus plug-in](lessons/0003-the-vda-scope.html)

**Process context**:
The factors bounding what is rated, such as releases, components and inclusions.
Taught in: [L08 · 1. Everything starts from the scope](lessons/0008-how-assessors-rate.html)

**Process instance**:
One distinct way a process is performed within the scope. Each is rated separately, then aggregated.
Taught in: [L08 · 4. Instances, then aggregation](lessons/0008-how-assessors-rate.html)

**Aggregation**:
Combining instance ratings as N0 P1 L2 F3 by arithmetic mean, or by a weighted mean whose weights are explained in the report. Exactly halfway rounds up.
Taught in: [L08 · 4. Instances, then aggregation](lessons/0008-how-assessors-rate.html)

**Plausibility check**:
An assessor's check that evidence fits the rhythm of the work. A work product created shortly before the assessment, with no plausible reason, is not considered.
Taught in: [L08 · 2. Evidence: sampled, plausible, and read](lessons/0008-how-assessors-rate.html)

**Rating rule (RL)**:
A Guidelines directive such as "shall (not) be downrated" or "not higher than", named like SYS.2.RL.5.
_Avoid_: Guideline rule
Taught in: [L08 · 5. Rating rules and weakness statements](lessons/0008-how-assessors-rate.html)

**Weakness statement**:
What is missing, the traceable evidence and the process risk. Required for every downrating, and for any weakness found within an F rating.
Taught in: [L08 · 5. Rating rules and weakness statements](lessons/0008-how-assessors-rate.html)

### Abbreviations and names

**ECU (electronic control unit)**:
The embedded controller Seat-Heat's software runs on.
First used in: [L01 · opening](lessons/0001-two-axes-of-a-rating.html)

**OEM / Tier-1**:
The vehicle maker / a supplier delivering directly to it.
First used in: [L01 · opening](lessons/0001-two-axes-of-a-rating.html)

**HIL (hardware-in-the-loop)**:
Testing software on the real ECU against a simulated environment.
First used in: [L03 · A. Which process?](lessons/0003-the-vda-scope.html)

**SIL (software-in-the-loop)**:
Running software against a simulated environment with no target hardware. It can support integration verification.
First used in: [L15 · The right leg: units, components, the whole software](lessons/0015-the-v-software-level.html)

**CI (continuous integration)**:
Building and checking every change automatically. Never used for configuration items.
First used in: [L01 · opening](lessons/0001-two-axes-of-a-rating.html)

**RASIC**:
A matrix saying who is Responsible, Approves, Supports, is Informed or Consulted for each activity (GP 3.1.1).
First used in: [L07 · PA 3.1: the standard process](lessons/0007-level-3-standard-and-defined-process.html)

**intacs / Gate4SPICE**:
The assessor certification body / its regular community events where practising assessors talk.
First used in: [L07 · Read next](lessons/0007-level-3-standard-and-defined-process.html)

### The course

These terms are for authors and agents working on the course. They are not in `reference/glossary.html`.

**Seat-Heat team**:
The one invented project every example uses: eight engineers at a Tier-1 supplier writing the control software for a seat-heating ECU, working in Jira, Git, pull requests and CI.
_Avoid_: real company, product or tool names
Taught in: [L01 · opening](lessons/0001-two-axes-of-a-rating.html)

**Lesson**:
One self-contained page in `lessons/` that teaches one idea in 10–20 minutes.
Taught in: [Course index](index.html)

**Core course**:
Lessons 1–9, ending in the capstone. Lessons 10–13 cover automation and AI, and lessons 14–16 walk the V process by process.
Taught in: [Course index](index.html)

**Warm-up**:
The retrieval questions that open a lesson, recalling earlier lessons.
Taught in: [Course index](index.html)

**Your win**:
The box closing each lesson's practice, saying what the learner can now do.

**Capstone**:
Lesson 9: a paper assessment of one Seat-Heat process, using everything in the core course.
Taught in: [L09 · Capstone: assess Seat-Heat's change management](lessons/0009-capstone-assess-seat-heat.html)

**Reference sheet**:
One printable page in `reference/`, such as the glossary, process cards or assessment rules.
Taught in: [Course index](index.html)

**Deck**:
One lesson's Anki flashcards in `anki/`, also bundled in `aspice-4.1.apkg`.
Taught in: [Course index](index.html)

**Teacher**:
The learner's AI chat partner, which lesson asides suggest asking.
_Avoid_: agent, which means a coding agent
