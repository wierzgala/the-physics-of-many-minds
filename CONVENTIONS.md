# Conventions

## Writing

- **Voice.** Descriptive and story-led. Each concept is introduced through something the reader can picture: a swarm, a slime mould, a crowd guessing the weight of an ox.
- **Three kinds of statement, never blurred:**
  - *Established findings*: results from experiments and observations, with a source in the chapter's Notes.
  - *The theory's claims*: hypotheses that follow from the framework and still need testing.
  - *Speculation*: ideas at the edge, marked as such.
- **Chapter endings.** Every chapter ends with two sections: *In short* (what the chapter claims) and *How we could be wrong* (the observation that would undermine it).
- **Research first.** Before a chapter is written, look for studies, measurements and striking facts that bear on it, and build the chapter around them.
- **Numbered references.** Every claim taken from a source carries a number in parentheses in the text, for example (3) or (1, 2). The chapter ends with a `## References` section: a numbered list in order of first appearance, each entry with authors, year, title and a link where available. A source keeps its number when cited again.
- **Numbers.** Estimates of our own carry no reference number and are labelled "rough" or "estimate" in the text.
- **Units.** Bits, metres, seconds, joules, watts. Scientific notation with Unicode superscripts (10¹⁵, 3 × 10⁻²¹).

## Files

- One chapter per file: `book/chNN-short-title.md`, numbered with two digits.
- The chapter title is the only `#` heading in the file; sections use `##`.
- References go at the end of each chapter file under `## References` (numbered). Chapters 1, 2, 3, 6, 10 and 13 still use the older unnumbered `## Notes` and are to be converted.

## Versioning

- Branch `main` holds the current text.
- One commit per meaningful change (a new chapter, a revised section, a batch of corrections), with a message that says what changed and why.
- Larger rewrites go on a branch (for example `rewrite/ch03`) and are merged when finished.
- Draft numbers are tracked in the README status table.
