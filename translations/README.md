# Language versions

*The Physics of Many Minds* is written in English. The English text in [`book/`](../book/) is the original and the only authoritative version. This folder holds translations, one subfolder per language, named by its language code.

| Language | Folder | Covers | Translated from | When | How | Checked by a person |
| --- | --- | --- | --- | --- | --- | --- |
| Polish (polski) | [`pl/`](pl/README.md) | preface, plan and Chapters 1 to 19 | commit `037a625` | 2026-11-28 | machine translation by Claude Fable 5.2 (Anthropic), at the author's request, in one pass with a fixed glossary and automatic checks of structure, citations, links and numbers | not yet |

The full account of each translation, including its glossary and its known limits, is in the `README.md` of its folder, written in that language.

## Rules for a translation

Every translation must say when and how it was made. Specifically:

1. **A row in the table above**, giving the language, what is covered, the commit of the English text it was made from, the date, the method and whether a person has checked it.
2. **A `README.md` in the language folder**, in that language, with: the translated title and the author's name; a table of contents; a section on the translation that states the date, the source commit, who or what translated it (for an AI system, the model and version; for a person, a name or pseudonym, and any AI assistance used), how it was checked, and what was left untranslated; and the glossary of the book's own terms.
3. **A first-line comment in every translated file** naming the source file, the source commit and the date, so that a file that has fallen behind the English text can be found mechanically:
   `<!-- ... book/chNN-title.md ... 037a625 ... 2026-11-28 ... -->`
4. **The same file names as in `book/`**, so that each translated file sits beside its source by name.
5. **When the English text changes**, the translated file is updated and its first-line comment and the "When" and "Translated from" entries are brought up to date. Until then the translation describes an older version, and its comment says which.

What is translated and what is not:

- The text of the preface, the plan and the chapters is translated in full, including tables.
- Reference entries (authors, titles, journals, links) stay in their original language. The explanatory notes attached to them are translated.
- The contributors page and the edit log are not translated. They are the working record of the project and are kept once, in English, in `book/`.
- Section names follow one convention per language (for example *In short* and *How we could be wrong*), recorded in that language's glossary.

Where a translation and the English text differ, the English text is right and the difference is an error in the translation. Please report it as an issue.

## Licence

A translation is an adaptation of the book and is covered by the same [LICENSE](../LICENSE): it may be shared and adapted in electronic form with credit to the author, Jakub Wierzgała, a link to this repository and a note of changes; the right to print any translation is reserved to the author. Contributors of translations are credited as [CONTRIBUTING.md](../CONTRIBUTING.md) describes, with the kind *translation*.

## Checking a translation against its source

`tools/check_translation.py` compares a language folder with `book/` file by file: the same number of paragraphs, headings, list items and table rows; the same citation numbers in the same paragraphs; the same links; the same numbers. It cannot judge wording. Run it from the repository root:

```
python3 tools/check_translation.py book translations/pl
```

Differences it reports for the Polish version are listed, with reasons, in [`pl/README.md`](pl/README.md).
