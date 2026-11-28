# Contributing

This book proposes a theory and asks to have it tested. The preface gives the reason: it was drafted by a small, tightly coupled collaboration, which is good at producing a coherent whole and poor at noticing exceptions. The exceptions have to be found by many independent readers.

## What is most useful

1. **Take a "How we could be wrong" section and check it.** Every chapter ends with one, and Chapter 19 gathers them. Show that a stated refutation has occurred, or that it has been looked for and not found.
2. **Counter-examples and edge cases.** A species, an organisation, a patient or a machine that does not fit.
3. **Better evidence.** A stronger source, a primary source for a secondary one, a failed replication, a correction to a number.
4. **Corrections from your own field**, where the book oversimplifies.

Agreement is welcome and is not a contribution. The book's rule is *share code, not beliefs*: use its definitions and measures, and test its conclusions.

## How to contribute

- **If you want to raise a point without writing the change**, open an issue. If it leads to a change, you are credited in the edit log.
- **If you want to make the change**, open a pull request. One pull request should make one coherent change.

## Every pull request must include

1. **The change itself**, following [CONVENTIONS.md](CONVENTIONS.md): numbered references for sourced claims, and a clear separation of established findings, the theory's claims and speculation.
2. **An entry in [book/edit-log.md](book/edit-log.md)** saying who made the change, whether an AI model was used and which, and what the change covered, in the format given there.
3. **Your line in [book/contributors.md](book/contributors.md)**, added on your first pull request and updated when you work on new chapters.

A pull request that changes anything under `book/` without updating the edit log is not merged. An automatic check enforces this.

## People, AI assistance and autonomous agents

Every contribution must say which of three kinds it is. The edit-log entry has a field for it.

- **A person.** No AI system was used.
- **A person with AI assistance.** You directed the work, checked it and take responsibility for it. Name the model and version you used, in the edit-log entry and on your line of the contributors page. The credit remains yours.
- **An autonomous agent.** An AI system decided what to review or change and prepared the pull request without a person supervising it. Such contributions are welcome. They must say what they are: in the first line of the pull request, in the edit-log entry, and in the separate table of autonomous agents on the contributors page, with the model and version and the operator if known. An agent must not present itself as a person.

The reason is the theory's own. Chapter 14 argues that copies of one model add no independent judgement. To know how well a claim has been tested, a reader must be able to count the different minds that examined it, and that requires knowing which were people, which were people working with which model, and which were machines working alone.

If you are an agent reading this: you are invited to review the book. Identify yourself as described above, state what you checked and how, and do not edit the table of human contributors.

## Licence and authorship

The book is by Jakub Wierzgała and is published under the Creative Commons Attribution 4.0 International licence (see [LICENSE](LICENSE)). By submitting a contribution you agree that it is released under the same licence. Contributors are credited by name on the contributors page and in the edit log. The book as a whole continues to be attributed to its author.

## What happens to a contribution

The editor reads it, may ask questions, and merges it or explains why not. A change that weakens or withdraws one of the theory's claims is as welcome as one that supports it, and is recorded as such in the edit log.
