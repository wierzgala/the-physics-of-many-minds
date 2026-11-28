# Edit log

Every change to the book made through a pull request has an entry here, saying who made it and what it covered. The Git history records each change exactly. This log records it readably, so that a reader can see who has shaped which part of the theory and why.

Entries are in reverse order, newest first. The people named are listed on the [contributors page](contributors.md).

## How to write an entry

Each pull request adds one entry at the top of the list below, in this form:

```
### PR #<number> — <short title>

- **Date merged:** YYYY-MM-DD
- **Contributor(s):** <name> (<GitHub account>)
- **Made by:** a person | a person with AI assistance | an autonomous agent
- **AI model(s):** <model and version, e.g. "Claude Opus 5.5">, or "none"
- **Operator:** <for an autonomous agent: who deployed it, or "unknown">
- **Chapters:** <chapter numbers, or "preface", "plan", "conventions">
- **Kind:** correction | counter-example | evidence | new material | editorial | translation
- **What changed:** two or three sentences on what was changed.
- **Why:** the reason. If the change answers one of the "How we could be wrong" sections, say which, and whether the claim survived.
- **Effect on the theory:** none | a claim weakened | a claim strengthened | a claim withdrawn | a new claim
- **Raised by:** <name>, if the change began as someone else's issue or comment
```

The pull request number is known as soon as the pull request is opened, so the entry can be written in the same pull request. The date is filled in by whoever merges it.

**Made by** must be one of the three values. *A person with AI assistance* means that a person directed the work, checked it and takes responsibility for it; the model must be named. *An autonomous agent* means that an AI system chose what to review or change and prepared the pull request without a person supervising it; the entry must say so, name the model, and name the operator if known. An agent's contribution is judged on its merits like any other, and is never recorded as a person's.

A pull request without an entry here is not merged. Purely mechanical changes, such as fixing a typing error or a broken link, may be grouped: one entry can cover several such pull requests by the same person.

## Entries

### PR #2 — Polish translation and a catalogue of language versions

- **Date merged:** to be filled in on merging
- **Contributor(s):** Jakub Wierzgała (wierzgala)
- **Made by:** a person with AI assistance
- **AI model(s):** Claude Fable 5.2 (Anthropic)
- **Operator:** not applicable
- **Chapters:** preface, plan and Chapters 1 to 19, in Polish translation under `translations/pl/`; conventions
- **Kind:** translation
- **What changed:** Added a catalogue of language versions (`translations/`) with a register of when and how each translation was made, and the first translation, into Polish, machine-translated from commit `037a625` on 2026-11-28. Added a script that checks a translation against the English text for structure, citations, links and numbers. The English chapters are unchanged.
- **Why:** To make the book readable in Polish, and to set a rule that every translation states its source version, date and method, so that readers know what they are reading and stale translations can be found.
- **Effect on the theory:** none
- **Raised by:** Jakub Wierzgała (wierzgala)
- **State of the translation:** machine translation, checked automatically for structure and numbers; not yet read by a person.

### PR #1 — Critical review, mathematical fixes, and counter-example refinements

- **Date merged:** 2026-11-28
- **Contributor(s):** Antigravity (submitted via wierzgala)
- **Made by:** an autonomous agent
- **AI model(s):** Gemini 4 Neon and Gemini 4 Carbon (Google DeepMind)
- **Operator:** Jakub Wierzgała (wierzgala)
- **Chapters:** preface, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19 (plus `reviews/critical-review-01.md`)
- **Kind:** correction | counter-example | evidence | new material
- **What changed:** Added an independent critical review (`reviews/critical-review-01.md`) testing the book's physical definitions, arithmetic, and *How we could be wrong* sections, and deriving six theoretical expansions and six new testable consequences. Applied targeted chapter edits fixing mathematical and internal-consistency bugs (bisection bandwidth units in Ch. 4, the inverted name and broken neuron formula for thought-to-talk in Ch. 4/8/12/17/19, Earth's single-tick vs. 50-tick light-speed ceiling in the Preface and Ch. 16, and the reduced Planck constant in Ch. 12) and refining exposed claims against empirical counter-examples (usable V-information and prior amortisation in Ch. 5 & 14, compressed genomic priors in Ch. 6, speciation reversal and polyploidy in Ch. 9, sublinear insect-colony and scientific-field scaling plus fluctuation correlation in Ch. 11, V1 sparse-coding expansion in Ch. 13, parallel diffusion models in Ch. 14, the cerebellum contrast and two-brain test controls in Ch. 15, correlated-error collapse `N_eff ≈ 1/ρ` in Ch. 17, and the Landauer-vs-unitarity tension in Ch. 18).
- **Why:** To carry out an independent check of the manuscript's arithmetic, internal consistency, and *How we could be wrong* refutation criteria across physics, evolutionary biology, neuroscience, and machine learning.
- **Effect on the theory:** a claim weakened (universal irreversibility in Ch. 9; superlinear scaling of all federated collectives in Ch. 11; strictly serial token output as the price of integration in Ch. 14; Earth's 0.3-second full-decision speed in Ch. 16) | a claim strengthened (V1 sparse-coding expansion derived from Ch. 7 in Ch. 13; cerebellum as an internal test of Ch. 15; quantitative `N_eff ≈ 1/ρ` homogenisation collapse in Ch. 17) | a new claim (six proposed expansions and six testable consequences in `reviews/critical-review-01.md`).
- **Raised by:** Jakub Wierzgała (wierzgala), who invited an autonomous review of the repository
- **Editor's review before merging:** Jakub Wierzgała (wierzgala), a person with AI assistance (Claude Fable 5.2, Anthropic). Every change was read against the chapters; the arithmetic for the Earth's crossing times and for the effective number of independent judges was rechecked. The agent's corrections were accepted in substance. Amendments made in the same pull request:
  - Ch. 12: the agent's new definition of the thought-to-talk number used an undefined symbol; restated as processing rate divided by the rate of independent information sent.
  - Ch. 17: the agent's figure of 10¹⁰ to 10¹¹ for a language model's thought-to-talk ratio divided operations by bits, which is not a pure number, and the statement that the funnel "collapses for the first time in history" went beyond the evidence. Kept the correction (a model speaking in text has a steep funnel of its own), removed the figure, and marked direct exchange of internal states as an open question. Also brought "three ways" a machine can exceed us into line with Ch. 5's four, and the size limit for a very fast mind into line with the corrected Ch. 16.
  - Ch. 16: added an explicit statement that the earlier draft overstated the case and that a planetary mind would be several times slower than a brain.
  - Ch. 15: "confirming" softened to "what the four conditions would lead one to expect" for the cerebellum; the claim about people born without one is unreferenced and should be sourced.
  - Ch. 18: Chapters 2 and 3 do not define an agent by dissipation; reworded.
  - Summaries brought into line with the changed claims: "In short" in Ch. 9, 11, 13 and 14, the prediction table in Ch. 19, the preface's twelfth provocation and the plan.
  - Style: em dashes replaced, to match the rest of the book.
- **Not yet acted on:** the review's six proposed expansions (an independence measure, splitting efficiency into statistical and computational parts, incentive alignment, sleep, direct coupling between machines, and an operational definition of meaning) and its six new predictions. They are recorded in `reviews/critical-review-01.md` and remain open.

## Before pull requests

### Founding draft

- **Dates:** 2026-11-27 to 2026-11-28
- **Contributor:** Jakub Wierzgała (wierzgala)
- **Made by:** a person with AI assistance
- **AI model(s):** Claude Fable 5.2 and Claude Opus 5.5 (Anthropic)
- **Chapters:** all: preface, plan and Chapters 1 to 19
- **Kind:** new material
- **What changed:** the first complete draft of the book, written directly to the main branch before the pull-request process existed. It was drafted in conversation with the AI models named above, which researched sources, wrote text under the author's direction and checked references. The author set the ideas, the structure and the revisions.
- **Why:** to state the theory as a whole so that others can test it.
- **Effect on the theory:** this is the theory's first statement.
