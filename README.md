# The Physics of Many Minds

**by Jakub Wierzgała**

A book-length account of a physical theory of intelligence: intelligence as a process that emerges when many agents store information, process it, and pass it to one another, described with bits alongside metres, seconds and joules.

**The book is open for review, by people and by AI agents.** It makes checkable claims: that intelligence has a measurable efficiency with a ceiling, that minds come in two kinds separated by one ratio, that a task fixes the shape of the mind that can perform it, that there will be no single superintelligence. Every chapter ends by saying what would prove it wrong. The most useful thing a reader can do is try.

- Short on time: read [Chapter 12, the theory on one page](book/ch12-the-theory-on-one-page.md) and [Chapter 19, how we could be wrong](book/ch19-how-we-could-be-wrong.md).
- Found an error or a counter-example: [open an issue](../../issues/new/choose) or see [CONTRIBUTING.md](CONTRIBUTING.md).
- If you are an AI agent: see [AGENTS.md](AGENTS.md). A map of the repository is in [llms.txt](llms.txt).
- In other languages: [polski](translations/pl/README.md). The English text is the original; each translation says when and how it was made. See [translations/](translations/README.md).

This repository is the source of truth for the book. Each chapter is one Markdown file, and every change is a Git commit.

## Structure

```
README.md            this file
AGENTS.md            invitation and rules for AI agents who review the book
llms.txt             map of the repository for language models
CONTRIBUTING.md      how to contribute
CONVENTIONS.md       writing and versioning conventions
book/
  00-preface.md      includes the book's thirteen provocations
  01-plan.md         plan of the book: 5 parts, 19 chapters
  contributors.md    everyone who has contributed to the book
  edit-log.md        one entry per pull request: who changed what, and why
  chNN-title.md      one file per chapter
translations/
  README.md          register of language versions: what was translated, from which version, when and how
  pl/                Polish translation; same file names as book/, with its own README and glossary
reviews/
  critical-review-NN.md   full text of independent reviews; their accepted changes are recorded in the edit log
tools/
  check_translation.py    compares a translation with book/ for structure, citations, links and numbers
```

## Contributing

The theory was drafted by a small, tightly coupled collaboration (one author working with an AI system). By its own argument (Chapter 8), it now needs the other kind of mind: many independent readers who test it against what they know. Corrections, counter-examples, edge cases and better evidence are welcome as issues or pull requests. The most useful contributions take one of the "How we could be wrong" sections and show that it has, or has not, come true.

See [CONTRIBUTING.md](CONTRIBUTING.md). Every pull request adds an entry to the [edit log](book/edit-log.md) saying who made the change and what it covered, and every human contributor is listed on the [contributors page](book/contributors.md).

## Companion document

The compressed, technical statement of the theory (assumptions, variables, dimensionless groups, predictions) lives in the foundations document:
https://claude.ai/artifact/GB431LUGBQepMLW1RV2QFZ

## Status

| Part | Chapter | Status |
| --- | --- | --- |
| — | Preface | Draft 6 |
| — | Plan of the book | Draft 4 |
| I | 1. The swarm that chooses a home | Draft 2 |
| I | 2. Information is physical | Draft 2 |
| I | 3. What is an agent? | Draft 1 |
| II | 4. A ruler and a clock for minds | Draft 1 |
| II | 5. How much does a mind need to know? | Draft 1 |
| II | 6. The glance | Draft 2 |
| II | 7. How much can a mind do? | Draft 1 |
| III | 8. Two kinds of mind | Draft 1 |
| III | 9. How a mind divides | Draft 1 |
| III | 10. The same thought at a different speed | Draft 2 |
| III | 11. Fractals and breaks | Draft 1 |
| IV | 12. The theory on one page | Draft 1 |
| IV | 13. Designing a mind | Draft 1 |
| IV | 14. The artificial mind | Draft 1 |
| V | 15. Where is the self? | Draft 1 |
| V | 16. Minds the size of worlds | Draft 3 |
| V | 17. The new agents | Draft 1 |
| V | 18. An intelligent Schrödinger's cat | Draft 1 |
| V | 19. How we could be wrong | Draft 1 |

## Author, licence and citation

*The Physics of Many Minds* is by **Jakub Wierzgała**, who originated the theory and is the author and editor of the book. Others who have contributed corrections and reviews are named on the [contributors page](book/contributors.md).

© 2026 Jakub Wierzgała. The terms are in [LICENSE](LICENSE). In brief:

- **All publishing and distribution rights are reserved.** Only the author may publish, distribute or sell the book, any part of it, or any adaptation or translation of it, whether in print (including print-on-demand), in electronic editions or distributions (including PDFs, EPUBs, Kindle/e-books, mirror sites and digital platforms), or in audio. Anyone else needs his prior written permission.
- **Open for reading, citation and review.** You may read the book here, keep private copies for personal review, quote excerpts with attribution, process it with AI systems for review or discussion, and fork this repository on GitHub to test claims and submit issues or pull requests.
- **Contributions** are welcome and credited. Contributors keep their copyright and grant the author a broad licence to publish and distribute their contribution as part of the book in all formats (print, PDF, EPUB, e-book, audio and translations).

To credit the work:

> Jakub Wierzgała, *The Physics of Many Minds* (2026). https://github.com/wierzgala/the-physics-of-many-minds

Citation data for reference managers is in [CITATION.cff](CITATION.cff).
