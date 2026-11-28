# Foundations

This folder holds the foundational document of the theory:

- [foundations.md](foundations.md): *A Physical Theory of Collective Intelligence: Foundations*, by Jakub Wierzgała, version 0.6, 27 November 2026.

## What it is

The foundations document is the first, compact statement of the theory, written before the book. It sets out the premise, the six primitive concepts, 21 numbered assumptions (A1 to A21), the variables and their units, the dimensionless groups (Π₁ to Π₇), the physical bounds and the predictions, in about 11,000 words. The book tells the same ideas slowly and with evidence; this document states them in the order a physicist would.

It is kept here as a **reference and a frame of mind**: the place to look when you want the whole theory in view at once, or want to see which assumption a chapter rests on.

## How to use it

- **The book is the current text.** This document is a snapshot of version 0.6 and has not been revised since the book was written and reviewed. Review and cite the chapters in [`book/`](../book/), not this file. Where the two disagree, the book is right.
- **The compact statement that is kept up to date** is [Chapter 12, The theory on one page](../book/ch12-the-theory-on-one-page.md).
- **Do not correct this file to match the book.** It is kept as a record of where the theory started. A new version, if one is written, will be added beside it under its own version number.
- Three topics are treated more fully here than in the book: the candidate definitions of efficiency, the roofline form of the bound, and consciousness as a separate layer.

## Where the book has moved on

The first review ([reviews/critical-review-01.md](../reviews/critical-review-01.md)) and later decisions changed the following. The edit log ([book/edit-log.md](../book/edit-log.md)) has the details.

| In this document | In the book |
| --- | --- |
| Efficiency η: the unit is an open choice (pure number, bit⁻¹ or J/bit), with the pure number preferred | Decided: η is a pure number with a ceiling of one (Chapter 5) |
| Π₂ "talk-to-compute ratio", r / (k·C) | "Thought to talk", r / s, where s is the rate of independent information sent; a signal copied to every link counts once (Chapters 4, 8, 12) |
| Bisection bandwidth introduced through a flux in bit/s/m² | Cross-talk B is a total flow in bit/s (Chapter 4) |
| Light-speed ceiling: a mind thinking at human speed can span about 90,000 km, seven Earth diameters | Corrected. One tick and a full decision of about fifty ticks are separate limits; a planetary mind shares a human-scale present but decides five to ten times more slowly than a brain (Chapter 16) |
| Genome as priors: about 6 × 10⁹ bits | Six billion raw bits; compressed functional content perhaps 10⁷ to 10⁸ bits (Chapter 6) |
| Scaling with size (P4): one power law, with the superlinear scaling of cities as the example | Refined: open, freely mixing federations speed up with size; integrated minds and transport- or attention-limited federations slow down (Chapters 11, 19) |
| Seven dimensionless groups | Ten pure numbers; added: exchange to drift, cognitive time, wiring dimension (Chapter 12) |
| Three base dimensions: bit, second, metre | Four: the joule is added (Chapter 12) |

The symbols also changed:

| Quantity | Here | Book (Chapter 12) |
| --- | --- | --- |
| Links per agent | k | d |
| Capacity of one link | C | c |
| Size of the collective | R | L |
| Timescale of the world | τ_env | T_w |
| Crossing time | τ_cross | t_x |
| Bisection bandwidth (cross-talk) | B_bis | B |
| Outer bandwidth | C_ext | R_in, R_out |
| Mean spacing between agents | d | not used |

The book also contains material that is not here: how a mind divides (Chapter 9), designing a mind from its task (Chapter 13), artificial minds (Chapters 14 and 17), and the repertoire rule.

## Source and conversion

The document was written as a Claude Doc by the author working with an AI system (Claude, Anthropic). This Markdown copy was exported from it on 28 November 2026. The wording is unchanged. Only the form was adapted: the two diagrams were replaced by plain-text sketches, the status column of the assumptions table became plain text, formulas are in GitHub's `math` blocks, and the title line, byline and a note at the top were written for this copy.

The same terms apply as to the rest of the repository; see [LICENSE](../LICENSE).
