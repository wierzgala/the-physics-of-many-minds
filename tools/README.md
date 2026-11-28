# Book Build & Translation Tools

This directory contains tools for maintaining and compiling *The Physics of Many Minds* (`book/`) and its translations (`translations/`).

## 1. Compiling EPUB3 and Print-Ready PDF (`build_book.py`)

`build_book.py` compiles both the English original (`book/`) and the Polish edition (`translations/pl/`, *Fizyka wielu umysłów*) into:

- **EPUB 3.3 (`.epub`)** — validated OCF/OPF3 package with backwards-compatible NCX navigation, e-reader stylesheet, colophon/ISBN metadata, and a `1600 × 2560 px` cover image (either auto-generated or supplied via `--cover`). Ready for **Empik Selfpublishing**, **Ridero**, **Amazon KDP**, **Apple Books**, and **Leanpub**.
- **Print-ready & Reader PDF (`.pdf`)** — typeset with [Typst](https://typst.app), **including a full-bleed vector front cover on Page 1** (or your custom `--cover` image), followed by mirrored inside/outside book margins, recto (`odd`-page) part and chapter openings with blank headerless versos, Roman front-matter pagination (`i–v`) switching to Arabic (`1…`) at the main text, running headers, booktabs tables with repeating headers across page breaks, mathematical subscripts/superscripts, and Polish orphan (*sierotki*) protection (`\u00a0` after single-letter prepositions and short abbreviations).
- **Optional Print-on-Demand Bundle (`--pod-bundle`)** — because print-on-demand services (Amazon KDP, Empik Selfpublishing, Totem.com.pl) require uploading the **interior text block** and the **wrap-around cover spread** as two separate PDFs, passing `--pod-bundle` additionally emits `*-pod-interior-*.pdf` (without Page 1 cover) and `*-pod-cover-spread-*.pdf` (Back Cover + dynamically calculated Spine + Front Cover + `3.175 mm` bleed + barcode box).

### Requirements

- **Python 3.9+** (uses only the Python standard library; no `pip` packages needed).
- **[Typst](https://github.com/typst/typst) 0.12+** (single binary; required for print PDFs and default high-resolution PNG cover generation).
  - Windows: `winget install Typst.Typst`
  - macOS: `brew install typst`
  - Linux: download binary from GitHub Releases or package manager.

### Quick start

Build everything (English + Polish, EPUB3 + `6 × 9 in` print PDF) into `dist/`:

```bash
python3 tools/build_book.py
```

On Windows Command Prompt or PowerShell (even before restarting your terminal after installing Python/Typst):

```powershell
.\tools\build_book.cmd
```

### Print trim presets (`--trim`)

| Flag | Dimensions | Target platforms / printers |
| --- | --- | --- |
| `--trim 6x9` *(default)* | `152.4 × 228.6 mm` (`6 × 9 in`) | **Amazon KDP** (`Amazon.pl` & global) / US Trade paperback |
| `--trim b5` | `165 × 235 mm` | **Polish popular-science standard** (Totem.com.pl, Sowa Druk, Imker) |
| `--trim a5` | `148 × 210 mm` | **Empik Selfpublishing** / compact Polish paperback |

*(For non-bleed text interiors, Amazon KDP and Empik Selfpublishing expect `--bleed 0`, which is the default. If a commercial print house asks for 3 mm bleed, pass `--bleed 3`.)*

### Adding ISBNs, publisher imprint, and a custom cover

Once you claim free ISBNs from Biblioteka Narodowa (`e-isbn.pl` — assign a separate ISBN to each format and language):

```bash
python3 tools/build_book.py \
  --lang pl \
  --trim b5 \
  --publisher "Jakub Wierzgała" \
  --edition "Wydanie I" \
  --isbn-print 978-83-XXXXX-01-0 \
  --isbn-epub  978-83-XXXXX-02-7 \
  --cover assets/cover-pl.png
```

Or build both languages at once with per-language ISBNs:

```bash
python3 tools/build_book.py \
  --isbn-print-en 978-83-XXXXX-03-4 \
  --isbn-epub-en  978-83-XXXXX-04-1 \
  --isbn-print-pl 978-83-XXXXX-01-0 \
  --isbn-epub-pl  978-83-XXXXX-02-7
```

### Useful flags

- `--lang {all,en,pl}` — build both editions or a single language.
- `--format {all,epub,pdf,typ}` — build only EPUB, only PDF, or emit the `.typ` source.
- `--font "Palatino Linotype"` — override the primary body serif font (defaults to `Libertinus Serif`, bundled inside Typst across all platforms).
- `--no-pdf-cover` — omit the front cover from Page 1 of the PDF when you only want a bare interior block.
- `--pod-bundle` — additionally generate a coverless `*-pod-interior-*.pdf` and a full wrap-around `*-pod-cover-spread-*.pdf` (Back + Spine + Front, spine width computed from interior page count × `--paper-thickness-mm`).
- `--no-plan` — omit `01-plan.md` from the compiled book (since the generated Table of Contents already lists all parts and chapters).
- `--no-back-matter` — omit the Contributors / Edit-log back matter.
- `--keep-draft-markers` — retain `*(drafted)*` markers and repository PR instructions instead of stripping them for publication.

---

## 2. Checking Translations (`check_translation.py`)

Compares a translation directory file-by-file against `book/` for structural parity (headings, paragraph count, lists, tables, citation numbers, links, numbers, and punctuation rules):

```bash
python3 tools/check_translation.py book translations/pl
```
