# Conventions

## Writing

- **Voice.** Descriptive and story-led. Each concept is introduced through something the reader can picture: a swarm, a slime mould, a crowd guessing the weight of an ox.
- **Three kinds of statement, never blurred:**
  - *Established findings*: results from experiments and observations, with a source in the chapter's Notes.
  - *The theory's claims*: hypotheses that follow from the framework and still need testing.
  - *Speculation*: ideas at the edge, marked as such.
- **Chapter endings.** Every chapter ends with two sections: *In short* (what the chapter claims) and *How we could be wrong* (the observation that would undermine it).
- **Numbers.** Every figure taken from a source is listed in the chapter's Notes. Estimates of our own are labelled "rough" or "estimate" in the text.
- **Units.** Bits, metres, seconds, joules, watts. Scientific notation with Unicode superscripts (10¹⁵, 3 × 10⁻²¹).

## Files

- One chapter per file: `book/chNN-short-title.md`, numbered with two digits.
- The chapter title is the only `#` heading in the file; sections use `##`.
- Notes and sources go at the end of each chapter file under `## Notes`.

## Versioning

- Branch `main` holds the current text.
- One commit per meaningful change (a new chapter, a revised section, a batch of corrections), with a message that says what changed and why.
- Larger rewrites go on a branch (for example `rewrite/ch03`) and are merged when finished.
- Draft numbers are tracked in the README status table.
