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

*(No pull requests have been merged yet.)*

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
