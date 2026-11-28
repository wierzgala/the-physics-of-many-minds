#!/usr/bin/env python3
"""Compile The Physics of Many Minds (and translations) into EPUB3 and print-ready PDF.

Usage examples:
  python3 tools/build_book.py
  python3 tools/build_book.py --lang pl --trim b5 --isbn-print 978-83-XXXXX-XX-X
  python3 tools/build_book.py --lang en --trim 6x9 --format pdf
  python3 tools/build_book.py --lang all --format all --out-dir dist

Requires only the Python 3 standard library for EPUB3 generation, and Typst
(https://typst.app) for print-ready PDF and default high-resolution PNG covers.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import pathlib
import re
import shutil
import struct
import subprocess
import sys
import uuid
import zipfile
import zlib
from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/wierzgala/the-physics-of-many-minds"
AUTHOR_NAME = "Jakub Wierzgała"


# ---------------------------------------------------------------------------
# Language & trim presets
# ---------------------------------------------------------------------------

@dataclass
class LangConfig:
    code: str
    source_dir: pathlib.Path
    title: str
    subtitle: str
    original_title: Optional[str]
    toc_title: str
    part_word: str
    chapter_word: str
    colophon_heading: str
    rights_lines: List[str]
    back_matter_note_title: str
    back_matter_note_paragraphs: List[str]
    back_cover_blurb: List[str]
    file_slug: str


LANG_PRESETS = {
    "en": LangConfig(
        code="en",
        source_dir=REPO_ROOT / "book",
        title="The Physics of Many Minds",
        subtitle="Information, Collective Intelligence, and What Minds Can Be",
        original_title=None,
        toc_title="Contents",
        part_word="Part",
        chapter_word="Chapter",
        colophon_heading="Copyright and publication notice",
        rights_lines=[
            f"Copyright © {{year}} {AUTHOR_NAME}.",
            "All publishing and distribution rights are reserved. No part of this book may be reproduced, packaged, distributed, hosted or sold in print, print-on-demand, electronic edition (including PDF, EPUB and e-book formats) or audio without the author's prior written permission, except for brief quotations in reviews and scholarly works as permitted by law.",
            f"An open reading and review text is maintained at {REPO_URL}.",
        ],
        back_matter_note_title="",
        back_matter_note_paragraphs=[],
        back_cover_blurb=[
            "Intelligence is not a substance hidden inside a skull. It is a physical process that appears whenever many agents store information, work on it, and pass it to one another.",
            "Counting information in bits alongside metres, seconds and joules, this book builds a single physical framework for brains, honeybee swarms, species, human societies and artificial minds. Along the way it asks why you can think only one thing at a time, why small teams disrupt while large teams develop, why every mind faces a trade-off between speed, size and unity, and why there will be no single superintelligence.",
            "Every chapter ends by stating what observation would prove it wrong.",
        ],
        file_slug="the-physics-of-many-minds-en",
    ),
    "pl": LangConfig(
        code="pl",
        source_dir=REPO_ROOT / "translations" / "pl",
        title="Fizyka wielu umysłów",
        subtitle="Informacja, inteligencja zbiorowa i granice tego, czym może być umysł",
        original_title="The Physics of Many Minds",
        toc_title="Spis treści",
        part_word="Część",
        chapter_word="Rozdział",
        colophon_heading="Nota wydawnicza i prawa autorskie",
        rights_lines=[
            f"Copyright © {{year}} {AUTHOR_NAME}.",
            "Tytuł oryginału angielskiego: The Physics of Many Minds.",
            "Wszelkie prawa do wydawania, rozpowszechniania i sprzedaży niniejszej książki oraz jej przekładów, zarówno drukiem (w tym w druku na żądanie), w wydaniach elektronicznych (w tym w formatach PDF, EPUB i innych e-bookach), jak i w formie nagrań audio, są zastrzeżone wyłącznie dla autora.",
            f"Otwarte repozytorium projektu do lektury i recenzji: {REPO_URL}.",
        ],
        back_matter_note_title="Współtwórcy i dziennik zmian",
        back_matter_note_paragraphs=[
            "Zgodnie z zasadą opisaną w Przedmowie książka jest rozwijana jawnie w publicznym repozytorium projektu, gdzie prowadzony jest bieżący wykaz osób oraz autonomicznych agentów sztucznej inteligencji sprawdzających poszczególne rozdziały, a także pełny dziennik zmian.",
            f"Aktualna lista współtwórców (book/contributors.md) oraz dziennik zmian (book/edit-log.md) są dostępne pod adresem: {REPO_URL}.",
        ],
        back_cover_blurb=[
            "Inteligencja nie jest substancją ukrytą we wnętrzu czaszki. Jest procesem fizycznym, który pojawia się zawsze, gdy wielu agentów przechowuje informację, przetwarza ją i przekazuje sobie nawzajem.",
            "Licząc informację w bitach na równi z metrami, sekundami i dżulami, książka ta buduje wspólne ramy fizyczne dla mózgów, rojów pszczół, gatunków biologicznych, ludzkich społeczeństw oraz sztucznej inteligencji. Wyjaśnia, dlaczego możemy myśleć tylko o jednej rzeczy naraz, dlaczego żaden umysł nie może być jednocześnie wielki, szybki i jednolity oraz dlaczego nie powstanie jedna superinteligencja.",
            "Każdy rozdział kończy się wskazaniem obserwacji, która obaliłaby jego twierdzenia.",
        ],
        file_slug="fizyka-wielu-umyslow-pl",
    ),
}


@dataclass
class TrimSpec:
    name: str
    width_mm: float
    height_mm: float
    inside_mm: float
    outside_mm: float
    top_mm: float
    bottom_mm: float
    body_pt: float
    table_pt: float
    ref_pt: float
    description: str


TRIM_SPECS = {
    "6x9": TrimSpec(
        name="6x9",
        width_mm=152.4,
        height_mm=228.6,
        inside_mm=22.0,
        outside_mm=16.0,
        top_mm=19.0,
        bottom_mm=21.0,
        body_pt=10.5,
        table_pt=8.8,
        ref_pt=9.0,
        description="6 × 9 in (152.4 × 228.6 mm) — Amazon KDP / US Trade standard",
    ),
    "b5": TrimSpec(
        name="b5",
        width_mm=165.0,
        height_mm=235.0,
        inside_mm=23.0,
        outside_mm=17.0,
        top_mm=20.0,
        bottom_mm=22.0,
        body_pt=10.5,
        table_pt=9.0,
        ref_pt=9.2,
        description="Polish book B5 (165 × 235 mm) — Polish popular-science standard",
    ),
    "a5": TrimSpec(
        name="a5",
        width_mm=148.0,
        height_mm=210.0,
        inside_mm=20.0,
        outside_mm=14.0,
        top_mm=17.0,
        bottom_mm=19.0,
        body_pt=10.0,
        table_pt=8.3,
        ref_pt=8.6,
        description="ISO A5 (148 × 210 mm) — Empik Selfpublishing / compact Polish paperback",
    ),
}

# Chapter range for each of the 5 parts (1-indexed inclusive)
PART_CHAPTER_RANGES: List[Tuple[int, int]] = [
    (1, 3),
    (4, 7),
    (8, 11),
    (12, 14),
    (15, 19),
]


# ---------------------------------------------------------------------------
# AST definitions
# ---------------------------------------------------------------------------

@dataclass
class InlineSpan:
    kind: str  # "text", "bold", "italic", "bold_italic", "code", "link", "sup", "sub"
    text: str = ""
    children: List["InlineSpan"] = field(default_factory=list)
    url: str = ""


@dataclass
class ListItem:
    inlines: List[InlineSpan]
    number: Optional[int] = None
    subitems: List[List[InlineSpan]] = field(default_factory=list)


@dataclass
class Block:
    kind: str  # "h2", "h3", "para", "blockquote", "ul", "ol", "table", "codeblock"
    inlines: List[InlineSpan] = field(default_factory=list)
    paragraphs: List[List[InlineSpan]] = field(default_factory=list)  # for blockquote
    items: List[ListItem] = field(default_factory=list)  # for ul / ol
    headers: List[List[InlineSpan]] = field(default_factory=list)  # for table
    rows: List[List[List[InlineSpan]]] = field(default_factory=list)  # for table
    raw_text: str = ""


@dataclass
class ChapterDoc:
    doc_id: str
    filename: str
    kind: str  # "preface", "plan", "chapter", "backmatter"
    chapter_num: Optional[int]
    label: Optional[str]  # e.g. "Chapter 1" / "Rozdział 1"
    title: str            # e.g. "The swarm that chooses a home"
    full_heading: str     # e.g. "Chapter 1. The swarm that chooses a home"
    part_index: Optional[int]  # 0..4 if first chapter of a part or belongs to part
    blocks: List[Block]


# ---------------------------------------------------------------------------
# Typst & git discovery helpers
# ---------------------------------------------------------------------------

def find_typst_binary(explicit: Optional[str] = None) -> Optional[pathlib.Path]:
    if explicit:
        p = pathlib.Path(explicit)
        return p if p.exists() else None
    found = shutil.which("typst")
    if found:
        return pathlib.Path(found)
    local_appdata = os.environ.get("LOCALAPPDATA")
    if local_appdata:
        winget_dir = pathlib.Path(local_appdata) / "Microsoft" / "WinGet" / "Packages"
        if winget_dir.exists():
            matches = sorted(winget_dir.glob("Typst.Typst*/**/typst.exe"))
            if matches:
                return matches[-1]
    return None


def git_short_commit() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return out or "working-tree"
    except Exception:
        return "working-tree"


# ---------------------------------------------------------------------------
# Polish typography & text pre-processing
# ---------------------------------------------------------------------------

PL_ORPHAN_RE = re.compile(
    r"(?<!\w)([aiouwzAIOUWZ]|np\.|m\.in\.|tzw\.|ok\.|rozdz\.|por\.|zob\.|nr|dr|prof\.) +"
)


def apply_lang_microtypography(text: str, lang: str) -> str:
    if lang == "pl":
        # Bind single-letter prepositions/conjunctions and short Polish abbreviations
        # to the following word with a non-breaking space (\u00a0).
        for _ in range(2):
            text = PL_ORPHAN_RE.sub("\\1\u00a0", text)
    return text


def preprocess_markdown(raw: str, filename: str, keep_draft_markers: bool) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    # Strip HTML comments (such as translation provenance comments on line 1)
    text = re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)

    if not keep_draft_markers:
        if filename == "01-plan.md":
            text = re.sub(r"\s*\*\(drafted\)\*", "", text)
            text = re.sub(r"\s*\*\(wersja robocza gotowa\)\*", "", text)
            # Clean draft-only sentence in line 3 of 01-plan.md if present
            text = text.replace(" All nineteen now exist in draft.", "")
            text = text.replace(" Wszystkie dziewiętnaście istnieje już w wersji roboczej.", "")
        elif filename == "contributors.md":
            # Strip GitHub PR submission instructions at the bottom for published book editions
            text = re.sub(r"\n## How to be listed\n.*\Z", "\n", text, flags=re.S)
            # Remove empty placeholder row if still empty
            text = re.sub(r"(?m)^\|\s*\*\(be the first\)\*\s*\|.*$\n?", "", text)
        elif filename == "edit-log.md":
            # Strip PR markdown template instructions for published book editions
            text = re.sub(
                r"\n## How to write an entry\n.*?(?=\n## Entries\n)",
                "\n",
                text,
                flags=re.S,
            )

    # In translations/pl/00-preface.md, remove duplicate standalone "*Jakub Wierzgała*"
    # right under "# Przedmowa" because the author is on the title page and cover.
    if filename == "00-preface.md":
        text = re.sub(r"(?m)^(# [^\n]+\n)\n\*Jakub Wierzgała\*\n", r"\1", text)

    return text.strip() + "\n"


# ---------------------------------------------------------------------------
# Inline Markdown parser (handles code, links, bare URLs, bold/italic, ^(...), X_y)
# ---------------------------------------------------------------------------

INLINE_TOKEN_RE = re.compile(
    r"(`[^`]+`)"                                     # 1: inline code
    r"|(\[([^\]]+)\]\(([^)]+)\))"                    # 2: link [3](4)
    r"|(https?://[^\s<>)\]]+)"                       # 5: bare URL
    r"|(\*\*\*([^*]+)\*\*\*)"                        # 6: bold+italic (7)
    r"|(\*\*([^*]+)\*\*)"                            # 8: bold (9)
    r"|(\*([^*]+)\*)"                                # 10: italic (11)
)

SCRIPT_TOKEN_RE = re.compile(
    r"(\^\(([^)]+)\))"                               # 1: ^(2) superscript
    r"|(\b([A-Za-z])_([A-Za-z0-9]+)\b)"              # 3: 4_5 subscript
)


def parse_plain_with_scripts(segment: str, lang: str) -> List[InlineSpan]:
    segment = apply_lang_microtypography(segment, lang)
    spans: List[InlineSpan] = []
    pos = 0
    for m in SCRIPT_TOKEN_RE.finditer(segment):
        if m.start() > pos:
            spans.append(InlineSpan("text", text=segment[pos:m.start()]))
        if m.group(1):
            spans.append(InlineSpan("sup", text=m.group(2)))
        else:
            spans.append(InlineSpan("text", text=m.group(4)))
            spans.append(InlineSpan("sub", text=m.group(5)))
        pos = m.end()
    if pos < len(segment):
        spans.append(InlineSpan("text", text=segment[pos:]))
    return spans


def resolve_internal_link(url: str, included_files: set[str], target_format: str) -> Optional[str]:
    clean = url.split("#")[0].strip()
    base = os.path.basename(clean)
    if url.startswith(("http://", "https://", "mailto:")):
        return url
    if base in included_files:
        stem = pathlib.Path(base).stem
        if target_format == "epub":
            return f"{stem}.xhtml"
        if target_format == "typst":
            return f"#sec-{stem}"
    return None


def parse_inlines(text: str, lang: str) -> List[InlineSpan]:
    spans: List[InlineSpan] = []
    pos = 0
    for m in INLINE_TOKEN_RE.finditer(text):
        if m.start() > pos:
            spans.extend(parse_plain_with_scripts(text[pos:m.start()], lang))

        if m.group(1):
            spans.append(InlineSpan("code", text=m.group(1)[1:-1]))
        elif m.group(2):
            label_raw, url = m.group(3), m.group(4).strip()
            spans.append(
                InlineSpan(
                    "link",
                    children=parse_inlines(label_raw, lang),
                    url=url,
                )
            )
        elif m.group(5):
            raw_url = m.group(5)
            trailing = ""
            while raw_url and raw_url[-1] in ".,;:!?)":
                trailing = raw_url[-1] + trailing
                raw_url = raw_url[:-1]
            spans.append(
                InlineSpan(
                    "link",
                    children=[InlineSpan("text", text=raw_url)],
                    url=raw_url,
                )
            )
            if trailing:
                spans.append(InlineSpan("text", text=trailing))
        elif m.group(6):
            spans.append(
                InlineSpan("bold_italic", children=parse_inlines(m.group(7), lang))
            )
        elif m.group(8):
            spans.append(
                InlineSpan("bold", children=parse_inlines(m.group(9), lang))
            )
        elif m.group(10):
            spans.append(
                InlineSpan("italic", children=parse_inlines(m.group(11), lang))
            )
        pos = m.end()

    if pos < len(text):
        spans.extend(parse_plain_with_scripts(text[pos:], lang))
    return spans


def inline_plain_text(spans: Sequence[InlineSpan]) -> str:
    parts: List[str] = []
    for sp in spans:
        if sp.kind in ("text", "code", "sup", "sub"):
            parts.append(sp.text)
        else:
            parts.append(inline_plain_text(sp.children))
    return "".join(parts)


# ---------------------------------------------------------------------------
# Block Markdown parser
# ---------------------------------------------------------------------------

CHAPTER_HEADING_RE = re.compile(
    r"^(Chapter\s+\d+|Rozdział\s+\d+)\.\s+(.+)$", re.IGNORECASE
)


def split_table_row(line: str) -> List[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.match(r"^:?-{2,}:?$", c) for c in cells)


def parse_chapter_markdown(
    filepath: pathlib.Path,
    doc_kind: str,
    lang: str,
    keep_draft_markers: bool,
    chapter_num: Optional[int] = None,
    part_index: Optional[int] = None,
) -> ChapterDoc:
    raw = filepath.read_text(encoding="utf-8")
    cleaned = preprocess_markdown(raw, filepath.name, keep_draft_markers)
    lines = cleaned.split("\n")

    full_heading = filepath.stem
    label: Optional[str] = None
    title = filepath.stem
    idx = 0

    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx < len(lines) and lines[idx].startswith("# "):
        full_heading = lines[idx][2:].strip()
        m = CHAPTER_HEADING_RE.match(full_heading)
        if m:
            label = m.group(1)
            title = m.group(2).strip()
        else:
            title = full_heading
        idx += 1

    blocks: List[Block] = []
    n = len(lines)

    while idx < n:
        line = lines[idx]
        stripped = line.strip()

        if not stripped:
            idx += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            idx += 1
            code_lines: List[str] = []
            while idx < n and not lines[idx].strip().startswith("```"):
                code_lines.append(lines[idx])
                idx += 1
            if idx < n:
                idx += 1
            blocks.append(Block("codeblock", raw_text="\n".join(code_lines)))
            continue

        # Headings
        if line.startswith("### "):
            blocks.append(Block("h3", inlines=parse_inlines(line[4:].strip(), lang)))
            idx += 1
            continue
        if line.startswith("## "):
            blocks.append(Block("h2", inlines=parse_inlines(line[3:].strip(), lang)))
            idx += 1
            continue

        # Table
        if stripped.startswith("|") and idx + 1 < n and is_table_separator(lines[idx + 1]):
            header_cells = split_table_row(lines[idx])
            ncols = len(header_cells)
            headers = [parse_inlines(c, lang) for c in header_cells]
            idx += 2  # skip header + separator
            rows: List[List[List[InlineSpan]]] = []
            while idx < n and lines[idx].strip().startswith("|"):
                rcells = split_table_row(lines[idx])
                # Normalise stray lone comma unit placeholder if present on older branches
                norm_cells: List[str] = []
                for c in rcells:
                    norm_cells.append("—" if c == "," else c)
                if len(norm_cells) < ncols:
                    norm_cells.extend([""] * (ncols - len(norm_cells)))
                elif len(norm_cells) > ncols:
                    norm_cells = norm_cells[:ncols]
                rows.append([parse_inlines(c, lang) for c in norm_cells])
                idx += 1
            if rows:
                blocks.append(Block("table", headers=headers, rows=rows))
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_paras: List[List[str]] = [[]]
            while idx < n and lines[idx].strip().startswith(">"):
                content = re.sub(r"^>\s?", "", lines[idx].strip())
                if not content:
                    if bq_paras[-1]:
                        bq_paras.append([])
                else:
                    bq_paras[-1].append(content)
                idx += 1
            bq_paras = [p for p in bq_paras if p]
            blocks.append(
                Block(
                    "blockquote",
                    paragraphs=[parse_inlines(" ".join(p), lang) for p in bq_paras],
                )
            )
            continue

        # Unordered list (supports 2-space indented sub-bullets)
        if line.startswith("- "):
            items: List[ListItem] = []
            while idx < n:
                cur = lines[idx]
                if cur.startswith("- "):
                    items.append(ListItem(inlines=parse_inlines(cur[2:].strip(), lang)))
                    idx += 1
                elif re.match(r"^  +-\s+", cur) and items:
                    sub_txt = re.sub(r"^  +-\s+", "", cur).strip()
                    items[-1].subitems.append(parse_inlines(sub_txt, lang))
                    idx += 1
                else:
                    break
            blocks.append(Block("ul", items=items))
            continue

        # Ordered list
        if re.match(r"^\d+\.\s+", line):
            items = []
            while idx < n:
                m_ol = re.match(r"^(\d+)\.\s+(.*)$", lines[idx])
                if not m_ol:
                    break
                items.append(
                    ListItem(
                        inlines=parse_inlines(m_ol.group(2).strip(), lang),
                        number=int(m_ol.group(1)),
                    )
                )
                idx += 1
            blocks.append(Block("ol", items=items))
            continue

        # Regular paragraph
        para_lines: List[str] = []
        while idx < n:
            cur = lines[idx]
            cur_s = cur.strip()
            if (
                not cur_s
                or cur.startswith(("# ", "## ", "### ", "- "))
                or cur_s.startswith(("```", ">", "|"))
                or re.match(r"^\d+\.\s+", cur)
            ):
                break
            para_lines.append(cur_s)
            idx += 1
        if para_lines:
            blocks.append(Block("para", inlines=parse_inlines(" ".join(para_lines), lang)))
        else:
            idx += 1

    return ChapterDoc(
        doc_id=filepath.stem,
        filename=filepath.name,
        kind=doc_kind,
        chapter_num=chapter_num,
        label=label,
        title=title,
        full_heading=full_heading,
        part_index=part_index,
        blocks=blocks,
    )


def extract_part_titles(plan_path: pathlib.Path, fallback_lang: str) -> List[Tuple[str, str]]:
    """Extract [(part_label, part_title), ...] from 01-plan.md H2 headings."""
    parts: List[Tuple[str, str]] = []
    if plan_path.exists():
        for line in plan_path.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                h = line[3:].strip()
                m = re.match(r"^((?:Part|Część)\s+[IVX]+)\.\s+(.+)$", h, re.IGNORECASE)
                if m:
                    parts.append((m.group(1), m.group(2).strip()))
    if len(parts) == 5:
        return parts
    if fallback_lang == "pl":
        return [
            ("Część I", "Idea"),
            ("Część II", "Miary"),
            ("Część III", "Umysły w umysłach"),
            ("Część IV", "Teoria w działaniu"),
            ("Część V", "Krańce"),
        ]
    return [
        ("Part I", "The idea"),
        ("Part II", "The measures"),
        ("Part III", "Minds inside minds"),
        ("Part IV", "The theory at work"),
        ("Part V", "The edges"),
    ]


def load_edition_docs(
    cfg: LangConfig,
    include_plan: bool,
    include_back_matter: bool,
    keep_draft_markers: bool,
) -> Tuple[List[Tuple[str, str]], List[ChapterDoc]]:
    src = cfg.source_dir
    if not src.exists():
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    part_titles = extract_part_titles(src / "01-plan.md", cfg.code)
    docs: List[ChapterDoc] = []

    preface_path = src / "00-preface.md"
    if preface_path.exists():
        docs.append(parse_chapter_markdown(preface_path, "preface", cfg.code, keep_draft_markers))

    plan_path = src / "01-plan.md"
    if include_plan and plan_path.exists():
        docs.append(parse_chapter_markdown(plan_path, "plan", cfg.code, keep_draft_markers))

    ch_files = sorted(src.glob("ch[0-9][0-9]-*.md"))
    for ch_path in ch_files:
        m = re.match(r"^ch(\d{2})-", ch_path.name)
        ch_num = int(m.group(1)) if m else None
        p_idx: Optional[int] = None
        if ch_num is not None:
            for i, (lo, hi) in enumerate(PART_CHAPTER_RANGES):
                if lo <= ch_num <= hi:
                    p_idx = i
                    break
        docs.append(
            parse_chapter_markdown(
                ch_path,
                "chapter",
                cfg.code,
                keep_draft_markers,
                chapter_num=ch_num,
                part_index=p_idx,
            )
        )

    if include_back_matter:
        if cfg.code == "en":
            for bm_name in ("contributors.md", "edit-log.md"):
                bm_path = src / bm_name
                if bm_path.exists():
                    docs.append(
                        parse_chapter_markdown(bm_path, "backmatter", cfg.code, keep_draft_markers)
                    )
        else:
            # Synthesize a clean native-language back-matter note for translations
            bm_blocks = [
                Block("para", inlines=parse_inlines(p, cfg.code))
                for p in cfg.back_matter_note_paragraphs
            ]
            docs.append(
                ChapterDoc(
                    doc_id="backmatter-credits",
                    filename="backmatter-credits.md",
                    kind="backmatter",
                    chapter_num=None,
                    label=None,
                    title=cfg.back_matter_note_title,
                    full_heading=cfg.back_matter_note_title,
                    part_index=None,
                    blocks=bm_blocks,
                )
            )

    return part_titles, docs


# ---------------------------------------------------------------------------
# Cover generation (Typst high-res PNG with pure-Python PNG fallback)
# ---------------------------------------------------------------------------

def make_fallback_png(width: int = 1600, height: int = 2560) -> bytes:
    """Create a valid minimalist deep-navy PNG cover using only Python stdlib."""
    raw_rows = bytearray()
    for y in range(height):
        raw_rows.append(0)  # filter type 0
        # Subtle vertical gradient in deep slate-navy
        r = 16 + (y * 10) // height
        g = 24 + (y * 16) // height
        b = 42 + (y * 24) // height
        raw_rows.extend(bytes((r, g, b)) * width)

    def chunk(tag: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(tag + data) & 0xFFFFFFFF
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", crc)

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    idat = zlib.compress(bytes(raw_rows), level=6)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", idat) + chunk(b"IEND", b"")


def render_front_cover_typst_box(
    cfg: LangConfig,
    panel_w_mm: float,
    panel_h_mm: float,
    title_pt: float = 28.0,
    sub_pt: float = 12.0,
    author_pt: float = 13.0,
    pad_x_mm: float = 17.0,
    pad_y_mm: float = 20.0,
) -> str:
    """Return a self-contained Typst box rendering the front cover artwork at any dimensions."""
    title_esc = escape_typst(cfg.title)
    sub_esc = escape_typst(cfg.subtitle)
    author_esc = escape_typst(AUTHOR_NAME).upper()

    # Constellation coordinates proportional to panel dimensions
    pts = [
        (0.16, 0.17, 1.35, "#d4a857"),
        (0.34, 0.13, 0.95, "#7da2c8"),
        (0.55, 0.19, 1.65, "#d4a857"),
        (0.76, 0.15, 1.05, "#7da2c8"),
        (0.84, 0.24, 1.25, "#f3efe6"),
        (0.26, 0.26, 1.15, "#f3efe6"),
        (0.46, 0.275, 1.05, "#7da2c8"),
        (0.68, 0.265, 0.95, "#d4a857"),
    ]
    edges = [
        (0, 1, 0.25, "#415675"),
        (1, 2, 0.30, "#415675"),
        (2, 3, 0.25, "#415675"),
        (3, 4, 0.25, "#415675"),
        (0, 5, 0.25, "#415675"),
        (5, 6, 0.25, "#415675"),
        (6, 2, 0.35, "#6b82a3"),
        (2, 7, 0.25, "#415675"),
        (7, 4, 0.25, "#415675"),
        (1, 6, 0.20, "#334560"),
    ]

    geom_lines: List[str] = []
    for i, j, sw, col in edges:
        x1 = pts[i][0] * panel_w_mm + pts[i][2]
        y1 = pts[i][1] * panel_h_mm + pts[i][2]
        x2 = pts[j][0] * panel_w_mm + pts[j][2]
        y2 = pts[j][1] * panel_h_mm + pts[j][2]
        geom_lines.append(
            f'    #place(line(start: ({x1:.2f}mm, {y1:.2f}mm), end: ({x2:.2f}mm, {y2:.2f}mm), stroke: {sw}pt + rgb("{col}")))'
        )
    for rx, ry, rad, col in pts:
        x = rx * panel_w_mm
        y = ry * panel_h_mm
        geom_lines.append(
            f'    #place(dx: {x:.2f}mm, dy: {y:.2f}mm, circle(radius: {rad}mm, fill: rgb("{col}")))'
        )

    geom_block = "\n".join(geom_lines)
    top_gap_mm = panel_h_mm * 0.36

    return f"""#box(width: {panel_w_mm:.2f}mm, height: {panel_h_mm:.2f}mm, fill: rgb("#111927"))[
{geom_block}
  #pad(x: {pad_x_mm:.2f}mm, y: {pad_y_mm:.2f}mm)[
    #set text(
      font: ("Libertinus Serif", "Palatino Linotype", "Georgia"),
      fill: rgb("#f3efe6"),
      lang: "{cfg.code}",
      hyphenate: false,
    )
    #set par(justify: false, first-line-indent: 0pt)
    #v({top_gap_mm - pad_y_mm:.2f}mm)
    #line(length: 26mm, stroke: 1.2pt + rgb("#d4a857"))
    #v(6.5mm)
    #par(leading: 0.55em)[
      #text(size: {title_pt}pt, weight: "bold", tracking: 0.2pt)[{title_esc}]
    ]
    #v(5.5mm)
    #par(leading: 0.65em)[
      #text(size: {sub_pt}pt, style: "italic", fill: rgb("#c6d0df"))[{sub_esc}]
    ]
    #v(1fr)
    #line(length: 100%, stroke: 0.4pt + rgb("#394b66"))
    #v(4.5mm)
    #text(size: {author_pt}pt, tracking: 1.6pt, fill: rgb("#f3efe6"))[{author_esc}]
  ]
]"""


def generate_typst_cover_png(
    cfg: LangConfig,
    out_png: pathlib.Path,
    typst_bin: Optional[pathlib.Path],
    work_dir: pathlib.Path,
) -> pathlib.Path:
    if typst_bin is None:
        out_png.write_bytes(make_fallback_png())
        return out_png

    box_code = render_front_cover_typst_box(
        cfg,
        panel_w_mm=160.0,
        panel_h_mm=256.0,
        title_pt=30.0,
        sub_pt=12.5,
        author_pt=14.0,
        pad_x_mm=18.0,
        pad_y_mm=22.0,
    )
    cover_typ = f"""// Auto-generated e-book cover (1600 x 2560 px at 254 PPI)
#set page(width: 160mm, height: 256mm, margin: 0pt)
{box_code}
"""
    work_dir.mkdir(parents=True, exist_ok=True)
    typ_file = work_dir / f"cover-{cfg.code}.typ"
    typ_file.write_text(cover_typ, encoding="utf-8")
    subprocess.run(
        [str(typst_bin), "compile", "--format", "png", "--ppi", "254", str(typ_file), str(out_png)],
        check=True,
    )
    return out_png


def compile_typst_pdf_safe(
    typst_bin: pathlib.Path,
    typ_path: pathlib.Path,
    out_pdf: pathlib.Path,
    work_dir: pathlib.Path,
) -> pathlib.Path:
    """Compile via work_dir temp PDF first so open/locked PDFs on Windows never abort the build."""
    tmp_pdf = work_dir / f".tmp-{out_pdf.name}"
    subprocess.run(
        [str(typst_bin), "compile", "--pdf-standard", "1.7", str(typ_path), str(tmp_pdf)],
        check=True,
    )
    try:
        shutil.copyfile(tmp_pdf, out_pdf)
        tmp_pdf.unlink(missing_ok=True)
        return out_pdf
    except PermissionError:
        alt_pdf = out_pdf.with_name(f"{out_pdf.stem}-with-cover{out_pdf.suffix}")
        shutil.copyfile(tmp_pdf, alt_pdf)
        tmp_pdf.unlink(missing_ok=True)
        print(
            f"Note: '{out_pdf.name}' is currently open in another program; wrote '{alt_pdf.name}' instead.",
            file=sys.stderr,
        )
        return alt_pdf


def generate_pod_wrap_cover_pdf(
    cfg: LangConfig,
    trim: TrimSpec,
    interior_pages: int,
    paper_thickness_mm: float,
    isbn_print: Optional[str],
    out_pdf: pathlib.Path,
    typst_bin: pathlib.Path,
    work_dir: pathlib.Path,
) -> Tuple[pathlib.Path, float]:
    """Generate a full Print-on-Demand wrap-around cover PDF (Back + Spine + Front + 3.175mm bleed)."""
    bleed = 3.175  # 0.125 in standard KDP / Polish POD cover bleed
    even_pages = interior_pages + (interior_pages % 2)
    spine_w = max(even_pages * paper_thickness_mm, 5.0)
    total_w = (2.0 * bleed) + (2.0 * trim.width_mm) + spine_w
    total_h = (2.0 * bleed) + trim.height_mm

    title_pt = 25.0 if trim.name == "a5" else 28.0
    sub_pt = 11.0 if trim.name == "a5" else 12.0
    author_pt = 12.0 if trim.name == "a5" else 13.0

    front_box = render_front_cover_typst_box(
        cfg,
        panel_w_mm=trim.width_mm + bleed,
        panel_h_mm=total_h,
        title_pt=title_pt,
        sub_pt=sub_pt,
        author_pt=author_pt,
        pad_x_mm=16.0,
        pad_y_mm=19.0 + bleed,
    )

    blurb_paras = "\n\n    ".join(
        escape_typst(apply_lang_microtypography(p, cfg.code)) for p in cfg.back_cover_blurb
    )
    isbn_label = f"ISBN {escape_typst(isbn_print)}" if isbn_print else "ISBN / Barcode Zone"
    title_esc = escape_typst(cfg.title)
    author_esc = escape_typst(AUTHOR_NAME)
    spine_pt = 9.0 if spine_w >= 8.5 else 7.5

    wrap_typ = f"""// Print-on-Demand full wrap-around cover ({even_pages} pp -> {spine_w:.2f}mm spine + 3.175mm bleed)
#set page(
  width: {total_w:.3f}mm,
  height: {total_h:.3f}mm,
  margin: 0pt,
  fill: rgb("#111927"),
)
#set text(
  font: ("Libertinus Serif", "Palatino Linotype", "Georgia"),
  fill: rgb("#f3efe6"),
  lang: "{cfg.code}",
)

#grid(
  columns: ({trim.width_mm + bleed:.3f}mm, {spine_w:.3f}mm, {trim.width_mm + bleed:.3f}mm),
  rows: ({total_h:.3f}mm,),
  // 1. Back cover (left panel + left/top/bottom bleed)
  box(width: 100%, height: 100%, fill: rgb("#111927"))[
    #pad(left: {16.0 + bleed:.2f}mm, right: 16mm, top: {22.0 + bleed:.2f}mm, bottom: {19.0 + bleed:.2f}mm)[
      #set par(justify: true, leading: 0.68em, spacing: 0.95em, first-line-indent: 0pt)
      #set text(size: 10pt, fill: rgb("#dbe2ee"))
      #line(length: 20mm, stroke: 1pt + rgb("#d4a857"))
      #v(5mm)
      {blurb_paras}
      #v(1fr)
      #align(right)[
        #box(
          width: 50.8mm,
          height: 30.5mm,
          fill: white,
          radius: 1pt,
          inset: 3mm,
        )[
          #align(center + horizon)[
            #set text(size: 8pt, fill: black)
            #par(justify: false)[{isbn_label}]
          ]
        ]
      ]
    ]
  ],
  // 2. Spine (center panel)
  box(width: 100%, height: 100%, fill: rgb("#0d1420"))[
    #align(center + horizon)[
      #rotate(90deg, reflow: true)[
        #box(width: {trim.height_mm - 24.0:.2f}mm)[
          #set par(justify: false, first-line-indent: 0pt)
          #grid(
            columns: (1fr, auto),
            align: (left + horizon, right + horizon),
            text(size: {spine_pt}pt, weight: "bold", fill: rgb("#f3efe6"))[{title_esc}],
            text(size: {spine_pt - 0.5}pt, tracking: 0.8pt, fill: rgb("#d4a857"))[{author_esc}],
          )
        ]
      ]
    ]
  ],
  // 3. Front cover (right panel + right/top/bottom bleed)
  [
    {front_box}
  ]
)
"""
    typ_file = work_dir / f"{out_pdf.stem}.typ"
    typ_file.write_text(wrap_typ, encoding="utf-8")
    final_pdf = compile_typst_pdf_safe(typst_bin, typ_file, out_pdf, work_dir)
    return final_pdf, spine_w


# ---------------------------------------------------------------------------
# EPUB 3.3 Renderer & Packager
# ---------------------------------------------------------------------------

EPUB_CSS = """/* Clean, reader-friendly EPUB3 stylesheet */
@namespace epub "http://www.idpf.org/2007/ops";

body {
  font-family: Georgia, "Palatino Linotype", Palatino, serif;
  line-height: 1.58;
  margin: 4% 5%;
}

h1, h2, h3 {
  line-height: 1.25;
  page-break-after: avoid;
  break-after: avoid;
  font-weight: bold;
}

.chapter-header {
  margin-top: 2.2em;
  margin-bottom: 1.8em;
}

.chapter-label {
  display: block;
  font-size: 0.82em;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0.78;
  margin-bottom: 0.35em;
}

h1.chapter-title {
  font-size: 1.65em;
  margin: 0;
}

h2 {
  font-size: 1.24em;
  margin-top: 1.75em;
  margin-bottom: 0.55em;
}

h3 {
  font-size: 1.06em;
  font-style: italic;
  margin-top: 1.35em;
  margin-bottom: 0.4em;
}

p {
  margin: 0;
  text-indent: 1.35em;
  text-align: justify;
}

h1 + p, h2 + p, h3 + p, .chapter-header + p,
blockquote + p, ul + p, ol + p, table + p, pre + p,
p.no-indent {
  text-indent: 0;
}

p + p {
  margin-top: 0.12em;
}

blockquote {
  margin: 1.05em 1.4em;
  padding-left: 0.85em;
  border-left: 2px solid #888888;
  font-style: normal;
}

blockquote p {
  text-indent: 0;
  text-align: left;
  margin-bottom: 0.45em;
}

blockquote p:last-child {
  margin-bottom: 0;
}

ul, ol {
  margin: 0.85em 0 0.95em 1.4em;
  padding: 0;
}

li {
  margin-bottom: 0.38em;
  text-align: left;
}

li ul {
  margin-top: 0.3em;
  margin-bottom: 0.3em;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.15em 0;
  font-size: 0.88em;
}

th, td {
  padding: 0.42em 0.5em;
  text-align: left;
  vertical-align: top;
  border-bottom: 1px solid #cccccc;
}

thead th {
  border-top: 2px solid #444444;
  border-bottom: 1.5px solid #444444;
  font-weight: bold;
}

tbody tr:last-child td {
  border-bottom: 2px solid #444444;
}

code, pre {
  font-family: Consolas, "DejaVu Sans Mono", monospace;
  font-size: 0.88em;
}

pre {
  padding: 0.75em;
  overflow-x: auto;
  white-space: pre-wrap;
  border: 1px solid #cccccc;
  margin: 0.9em 0;
}

.title-page {
  text-align: center;
  margin-top: 16%;
}

.title-page h1 {
  font-size: 2.0em;
  margin-bottom: 0.35em;
}

.title-page .subtitle {
  font-size: 1.05em;
  font-style: italic;
  opacity: 0.85;
  margin-bottom: 2.5em;
  text-indent: 0;
  text-align: center;
}

.title-page .author {
  font-size: 1.15em;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-indent: 0;
  text-align: center;
}

.part-page {
  text-align: center;
  margin-top: 24%;
}

.part-page .part-label {
  font-size: 0.9em;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  opacity: 0.75;
  text-indent: 0;
  text-align: center;
  margin-bottom: 0.5em;
}

.part-page h1 {
  font-size: 1.75em;
  margin: 0;
}

.colophon p {
  text-indent: 0;
  text-align: left;
  font-size: 0.88em;
  margin-bottom: 0.75em;
}

.references-list {
  font-size: 0.9em;
}

.references-list li {
  word-wrap: break-word;
  overflow-wrap: anywhere;
}

.cover-wrap {
  text-align: center;
  margin: 0;
  padding: 0;
}

.cover-wrap img {
  max-width: 100%;
  max-height: 98vh;
  height: auto;
}

nav#toc ol {
  list-style-type: none;
  margin-left: 0;
  padding-left: 0;
}

nav#toc ol ol {
  margin-left: 1.2em;
}

nav#toc li {
  margin-bottom: 0.42em;
}
"""


def add_url_wbr_html(s: str) -> str:
    """Insert zero-width spaces into displayed URLs so narrow screens wrap cleanly."""
    escaped = html.escape(s, quote=True)
    if escaped.startswith(("http://", "https://")):
        escaped = re.sub(r"([/\-._])", "\\1&#8203;", escaped)
    return escaped


def render_inlines_xhtml(spans: Sequence[InlineSpan], included_files: set[str]) -> str:
    out: List[str] = []
    for sp in spans:
        if sp.kind == "text":
            out.append(html.escape(sp.text, quote=True))
        elif sp.kind == "code":
            out.append(f"<code>{html.escape(sp.text, quote=True)}</code>")
        elif sp.kind == "sup":
            out.append(f"<sup>{html.escape(sp.text, quote=True)}</sup>")
        elif sp.kind == "sub":
            out.append(f"<sub>{html.escape(sp.text, quote=True)}</sub>")
        elif sp.kind == "bold":
            out.append(f"<strong>{render_inlines_xhtml(sp.children, included_files)}</strong>")
        elif sp.kind == "italic":
            out.append(f"<em>{render_inlines_xhtml(sp.children, included_files)}</em>")
        elif sp.kind == "bold_italic":
            out.append(f"<strong><em>{render_inlines_xhtml(sp.children, included_files)}</em></strong>")
        elif sp.kind == "link":
            resolved = resolve_internal_link(sp.url, included_files, "epub")
            if len(sp.children) == 1 and sp.children[0].kind == "text" and sp.children[0].text.startswith(("http://", "https://")):
                inner = add_url_wbr_html(sp.children[0].text)
            else:
                inner = render_inlines_xhtml(sp.children, included_files)
            if resolved:
                out.append(f'<a href="{html.escape(resolved, quote=True)}">{inner}</a>')
            else:
                out.append(inner)
    return "".join(out)


def xhtml_shell(title: str, lang: str, body_html: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(title, quote=True)}</title>
  <link rel="stylesheet" type="text/css" href="../styles/book.css" />
</head>
<body>
{body_html}
</body>
</html>
"""


def render_doc_xhtml(doc: ChapterDoc, lang: str, included_files: set[str]) -> str:
    parts: List[str] = ['<section epub:type="chapter">']
    if doc.label:
        parts.append(
            f'<div class="chapter-header">'
            f'<span class="chapter-label">{html.escape(doc.label)}</span>'
            f'<h1 class="chapter-title">{html.escape(doc.title)}</h1>'
            f'</div>'
        )
    else:
        parts.append(
            f'<div class="chapter-header">'
            f'<h1 class="chapter-title">{html.escape(doc.title)}</h1>'
            f'</div>'
        )

    in_references = False
    for blk in doc.blocks:
        if blk.kind == "h2":
            h_txt = inline_plain_text(blk.inlines).strip().lower()
            in_references = h_txt in ("references", "źródła")
            parts.append(f"<h2>{render_inlines_xhtml(blk.inlines, included_files)}</h2>")
        elif blk.kind == "h3":
            parts.append(f"<h3>{render_inlines_xhtml(blk.inlines, included_files)}</h3>")
        elif blk.kind == "para":
            cls = ' class="no-indent"' if in_references else ""
            parts.append(f"<p{cls}>{render_inlines_xhtml(blk.inlines, included_files)}</p>")
        elif blk.kind == "blockquote":
            ps = "".join(f"<p>{render_inlines_xhtml(p, included_files)}</p>" for p in blk.paragraphs)
            parts.append(f"<blockquote>{ps}</blockquote>")
        elif blk.kind == "ul":
            lis: List[str] = []
            for it in blk.items:
                sub_html = ""
                if it.subitems:
                    sub_lis = "".join(
                        f"<li>{render_inlines_xhtml(si, included_files)}</li>" for si in it.subitems
                    )
                    sub_html = f"<ul>{sub_lis}</ul>"
                lis.append(f"<li>{render_inlines_xhtml(it.inlines, included_files)}{sub_html}</li>")
            parts.append(f"<ul>{''.join(lis)}</ul>")
        elif blk.kind == "ol":
            cls = ' class="references-list"' if in_references else ""
            start_attr = (
                f' start="{blk.items[0].number}"'
                if blk.items and blk.items[0].number and blk.items[0].number != 1
                else ""
            )
            lis = [
                f'<li value="{it.number}">{render_inlines_xhtml(it.inlines, included_files)}</li>'
                if it.number is not None
                else f"<li>{render_inlines_xhtml(it.inlines, included_files)}</li>"
                for it in blk.items
            ]
            parts.append(f"<ol{cls}{start_attr}>{''.join(lis)}</ol>")
        elif blk.kind == "table":
            ths = "".join(f"<th>{render_inlines_xhtml(h, included_files)}</th>" for h in blk.headers)
            trs: List[str] = []
            for r in blk.rows:
                tds = "".join(f"<td>{render_inlines_xhtml(c, included_files)}</td>" for c in r)
                trs.append(f"<tr>{tds}</tr>")
            parts.append(
                f"<table><thead><tr>{ths}</tr></thead><tbody>{''.join(trs)}</tbody></table>"
            )
        elif blk.kind == "codeblock":
            parts.append(f"<pre><code>{html.escape(blk.raw_text, quote=True)}</code></pre>")

    parts.append("</section>")
    return xhtml_shell(doc.full_heading, lang, "\n".join(parts))


def build_epub(
    cfg: LangConfig,
    part_titles: List[Tuple[str, str]],
    docs: List[ChapterDoc],
    out_epub: pathlib.Path,
    cover_img_path: pathlib.Path,
    isbn_epub: Optional[str],
    isbn_print: Optional[str],
    publisher: str,
    year: str,
    edition: Optional[str],
    commit_sha: str,
) -> None:
    included_files = {d.filename for d in docs}
    cover_ext = cover_img_path.suffix.lower().lstrip(".")
    cover_media = "image/jpeg" if cover_ext in ("jpg", "jpeg") else "image/png"
    cover_rel_name = f"cover.{'jpg' if cover_media == 'image/jpeg' else 'png'}"

    spine_files: List[Tuple[str, str, str]] = []  # (item_id, filename, nav_title)
    text_pages: List[Tuple[str, str]] = []        # (OEBPS/text/..., content)

    # 1. Cover page
    cover_xhtml = xhtml_shell(
        cfg.title,
        cfg.code,
        f'<div class="cover-wrap"><img src="../images/{cover_rel_name}" alt="{html.escape(cfg.title, quote=True)}" /></div>',
    )
    text_pages.append(("OEBPS/text/cover.xhtml", cover_xhtml))
    spine_files.append(("item-cover-page", "text/cover.xhtml", "Cover" if cfg.code == "en" else "Okładka"))

    # 2. Title page
    title_xhtml = xhtml_shell(
        cfg.title,
        cfg.code,
        f"""<section class="title-page" epub:type="titlepage">
  <h1>{html.escape(cfg.title)}</h1>
  <p class="subtitle">{html.escape(cfg.subtitle)}</p>
  <p class="author">{html.escape(AUTHOR_NAME)}</p>
</section>""",
    )
    text_pages.append(("OEBPS/text/titlepage.xhtml", title_xhtml))
    spine_files.append(("item-titlepage", "text/titlepage.xhtml", cfg.title))

    # 3. Colophon / Copyright page
    colophon_paras: List[str] = []
    for line in cfg.rights_lines:
        colophon_paras.append(f"<p>{html.escape(line.format(year=year))}</p>")
    if edition:
        colophon_paras.append(f"<p>{html.escape(edition)}</p>")
    if publisher:
        pub_lbl = "Publisher" if cfg.code == "en" else "Wydawca"
        colophon_paras.append(f"<p>{pub_lbl}: {html.escape(publisher)}</p>")
    if isbn_epub:
        colophon_paras.append(f"<p>ISBN (EPUB): {html.escape(isbn_epub)}</p>")
    if isbn_print:
        lbl = "ISBN (Print)" if cfg.code == "en" else "ISBN (druk)"
        colophon_paras.append(f"<p>{lbl}: {html.escape(isbn_print)}</p>")
    rev_lbl = "Source revision" if cfg.code == "en" else "Wersja źródłowa"
    colophon_paras.append(f"<p>{rev_lbl}: <code>{html.escape(commit_sha)}</code></p>")

    colophon_xhtml = xhtml_shell(
        cfg.colophon_heading,
        cfg.code,
        f'<section class="colophon" epub:type="copyright-page"><h2>{html.escape(cfg.colophon_heading)}</h2>\n'
        + "\n".join(colophon_paras)
        + "\n</section>",
    )
    text_pages.append(("OEBPS/text/colophon.xhtml", colophon_xhtml))
    spine_files.append(("item-colophon", "text/colophon.xhtml", cfg.colophon_heading))

    # Reserve slot 4 in spine for visible TOC (nav.xhtml)
    # Build body pages & hierarchical TOC structure
    toc_front: List[Tuple[str, str]] = []
    toc_parts: List[Tuple[str, str, List[Tuple[str, str]]]] = []
    toc_back: List[Tuple[str, str]] = []

    emitted_parts: set[int] = set()
    body_spine: List[Tuple[str, str, str]] = []

    for doc in docs:
        if doc.kind == "chapter" and doc.part_index is not None and doc.part_index not in emitted_parts:
            emitted_parts.add(doc.part_index)
            p_lbl, p_title = part_titles[doc.part_index]
            part_file = f"part-{doc.part_index + 1:02d}.xhtml"
            part_xhtml = xhtml_shell(
                f"{p_lbl}. {p_title}",
                cfg.code,
                f"""<section class="part-page" epub:type="part">
  <p class="part-label">{html.escape(p_lbl)}</p>
  <h1>{html.escape(p_title)}</h1>
</section>""",
            )
            text_pages.append((f"OEBPS/text/{part_file}", part_xhtml))
            body_spine.append((f"item-part-{doc.part_index + 1:02d}", f"text/{part_file}", f"{p_lbl}. {p_title}"))
            toc_parts.append((part_file, f"{p_lbl}. {p_title}", []))

        xhtml_name = f"{doc.doc_id}.xhtml"
        doc_xhtml = render_doc_xhtml(doc, cfg.code, included_files)
        text_pages.append((f"OEBPS/text/{xhtml_name}", doc_xhtml))
        item_id = f"item-{re.sub(r'[^a-zA-Z0-9_-]', '-', doc.doc_id)}"
        body_spine.append((item_id, f"text/{xhtml_name}", doc.full_heading))

        if doc.kind in ("preface", "plan"):
            toc_front.append((xhtml_name, doc.full_heading))
        elif doc.kind == "chapter" and toc_parts:
            toc_parts[-1][2].append((xhtml_name, doc.full_heading))
        else:
            toc_back.append((xhtml_name, doc.full_heading))

    # Build OEBPS/text/nav.xhtml (EPUB3 navigation document, also shown in spine)
    nav_items_html: List[str] = []
    for href, lbl in toc_front:
        nav_items_html.append(f'<li><a href="{href}">{html.escape(lbl)}</a></li>')
    for p_href, p_lbl, ch_list in toc_parts:
        sub = "".join(f'<li><a href="{c_href}">{html.escape(c_lbl)}</a></li>' for c_href, c_lbl in ch_list)
        nav_items_html.append(
            f'<li><a href="{p_href}">{html.escape(p_lbl)}</a><ol>{sub}</ol></li>'
        )
    for href, lbl in toc_back:
        nav_items_html.append(f'<li><a href="{href}">{html.escape(lbl)}</a></li>')

    first_body_href = toc_front[0][0] if toc_front else (toc_parts[0][0] if toc_parts else "titlepage.xhtml")
    nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{cfg.code}" lang="{cfg.code}">
<head>
  <meta charset="utf-8" />
  <title>{html.escape(cfg.toc_title)}</title>
  <link rel="stylesheet" type="text/css" href="../styles/book.css" />
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>{html.escape(cfg.toc_title)}</h1>
    <ol>
      {''.join(nav_items_html)}
    </ol>
  </nav>
  <nav epub:type="landmarks" hidden="hidden">
    <h2>Landmarks</h2>
    <ol>
      <li><a epub:type="cover" href="cover.xhtml">Cover</a></li>
      <li><a epub:type="toc" href="nav.xhtml">{html.escape(cfg.toc_title)}</a></li>
      <li><a epub:type="bodymatter" href="{first_body_href}">{html.escape(cfg.title)}</a></li>
    </ol>
  </nav>
</body>
</html>
"""
    text_pages.append(("OEBPS/text/nav.xhtml", nav_xhtml))
    spine_files.append(("item-nav", "text/nav.xhtml", cfg.toc_title))
    spine_files.extend(body_spine)

    # Backwards-compatible NCX for EPUB2 e-readers
    pub_uid = f"urn:isbn:{isbn_epub.replace('-', '')}" if isbn_epub else f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, REPO_URL + '/' + cfg.code)}"
    ncx_points: List[str] = []
    play_order = 1
    for item_id, rel_href, nav_lbl in spine_files[1:]:  # skip raw image cover
        ncx_points.append(
            f"""    <navPoint id="np-{play_order}" playOrder="{play_order}">
      <navLabel><text>{html.escape(nav_lbl)}</text></navLabel>
      <content src="{rel_href}" />
    </navPoint>"""
        )
        play_order += 1

    toc_ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{html.escape(pub_uid, quote=True)}" />
    <meta name="dtb:depth" content="2" />
    <meta name="dtb:totalPageCount" content="0" />
    <meta name="dtb:maxPageNumber" content="0" />
  </head>
  <docTitle><text>{html.escape(cfg.title)}</text></docTitle>
  <navMap>
{chr(10).join(ncx_points)}
  </navMap>
</ncx>
"""

    modified_utc = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest_items: List[str] = [
        '    <item id="css" href="styles/book.css" media-type="text/css" />',
        f'    <item id="cover-img" href="images/{cover_rel_name}" media-type="{cover_media}" properties="cover-image" />',
        '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml" />',
    ]
    spine_refs: List[str] = []
    for item_id, rel_href, _ in spine_files:
        props = ' properties="nav"' if item_id == "item-nav" else ""
        manifest_items.append(
            f'    <item id="{item_id}" href="{rel_href}" media-type="application/xhtml+xml"{props} />'
        )
        linear = ' linear="no"' if item_id == "item-cover-page" else ""
        spine_refs.append(f'    <itemref idref="{item_id}"{linear} />')

    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id" xml:lang="{cfg.code}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">{html.escape(pub_uid)}</dc:identifier>
    <dc:title>{html.escape(cfg.title)}</dc:title>
    <dc:creator>{html.escape(AUTHOR_NAME)}</dc:creator>
    <dc:language>{cfg.code}</dc:language>
    <dc:publisher>{html.escape(publisher)}</dc:publisher>
    <dc:date>{year}-11-28</dc:date>
    <dc:rights>Copyright © {year} {html.escape(AUTHOR_NAME)}. All publishing and distribution rights reserved.</dc:rights>
    <meta property="dcterms:modified">{modified_utc}</meta>
    <meta name="cover" content="cover-img" />
  </metadata>
  <manifest>
{chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine_refs)}
  </spine>
</package>
"""

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/epub+zip" />
  </rootfiles>
</container>
"""

    out_epub.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out_epub, "w") as zf:
        # OCF spec: mimetype MUST be first entry, uncompressed, with no extra fields
        mi = zipfile.ZipInfo("mimetype")
        mi.compress_type = zipfile.ZIP_STORED
        zf.writestr(mi, b"application/epub+zip")

        zf.writestr("META-INF/container.xml", container_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/styles/book.css", EPUB_CSS.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr(f"OEBPS/images/{cover_rel_name}", cover_img_path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/toc.ncx", toc_ncx.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/content.opf", content_opf.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        for arc_path, xhtml_str in text_pages:
            zf.writestr(arc_path, xhtml_str.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)


# ---------------------------------------------------------------------------
# Typst Print-Ready PDF Renderer
# ---------------------------------------------------------------------------

def escape_typst(text: str) -> str:
    """Escape special Typst markup characters safely."""
    out: List[str] = []
    for ch in text:
        if ch in ("\\", "#", "$", "@", "*", "_", "`", "<", ">", "[", "]", "~"):
            out.append("\\" + ch)
        else:
            out.append(ch)
    res = "".join(out)
    # Prevent accidental Typst line/block comments or list markers
    res = res.replace("//", "/\u200b/").replace("/*", "/\u200b*")
    return res


def escape_typst_url_display(url: str) -> str:
    """Escape a displayed URL for Typst and insert zero-width line-break hints."""
    parts: List[str] = []
    for ch in url:
        if ch in ("\\", "#", "$", "@", "*", "_", "`", "<", ">", "[", "]", "~"):
            parts.append("\\" + ch)
        else:
            parts.append(ch)
        if ch in ("/", "-", ".", "_"):
            parts.append("\u200b")
    return "".join(parts).replace("//", "/\u200b/")


def escape_typst_string(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render_inlines_typst(
    spans: Sequence[InlineSpan],
    included_files: set[str],
    print_urls_plain: bool = True,
) -> str:
    out: List[str] = []
    for sp in spans:
        if sp.kind == "text":
            out.append(escape_typst(sp.text))
        elif sp.kind == "code":
            # Use #raw("...") to avoid backtick collisions
            out.append(f'#raw("{escape_typst_string(sp.text)}")')
        elif sp.kind == "sup":
            out.append(f"#super[{escape_typst(sp.text)}]")
        elif sp.kind == "sub":
            out.append(f"#sub[{escape_typst(sp.text)}]")
        elif sp.kind == "bold":
            out.append(f"#strong[{render_inlines_typst(sp.children, included_files, print_urls_plain)}]")
        elif sp.kind == "italic":
            out.append(f"#emph[{render_inlines_typst(sp.children, included_files, print_urls_plain)}]")
        elif sp.kind == "bold_italic":
            out.append(f"#strong[#emph[{render_inlines_typst(sp.children, included_files, print_urls_plain)}]]")
        elif sp.kind == "link":
            is_raw_url = (
                len(sp.children) == 1
                and sp.children[0].kind == "text"
                and sp.children[0].text.startswith(("http://", "https://"))
            )
            if is_raw_url:
                disp = f'#text(size: 0.9em)[{escape_typst_url_display(sp.children[0].text)}]'
            else:
                disp = render_inlines_typst(sp.children, included_files, print_urls_plain)

            if sp.url.startswith(("http://", "https://", "mailto:")):
                out.append(f'#link("{escape_typst_string(sp.url)}")[{disp}]')
            else:
                resolved = resolve_internal_link(sp.url, included_files, "typst")
                if resolved and resolved.startswith("#"):
                    lbl = resolved[1:]
                    out.append(f"#link(<{lbl}>)[{disp}]")
                else:
                    out.append(disp)
    return "".join(out)


def compute_typst_col_specs(headers: List[List[InlineSpan]], rows: List[List[List[InlineSpan]]]) -> str:
    ncols = len(headers)
    max_lens: List[int] = []
    for c_idx in range(ncols):
        lengths = [len(inline_plain_text(headers[c_idx]))]
        for r in rows:
            if c_idx < len(r):
                lengths.append(len(inline_plain_text(r[c_idx])))
        max_lens.append(max(lengths) if lengths else 1)

    specs: List[str] = []
    for ml in max_lens:
        if ml <= 12:
            specs.append("auto")
        elif ml <= 28:
            specs.append("1fr")
        elif ml <= 60:
            specs.append("1.6fr")
        else:
            specs.append("2.3fr")
    # Ensure at least one flexible column so table spans the text block cleanly
    if all(s == "auto" for s in specs) and specs:
        specs[-1] = "1fr"
    return "(" + ", ".join(specs) + ")"


def render_typst_document(
    cfg: LangConfig,
    part_titles: List[Tuple[str, str]],
    docs: List[ChapterDoc],
    trim: TrimSpec,
    bleed_mm: float,
    font_primary: str,
    isbn_print: Optional[str],
    isbn_epub: Optional[str],
    publisher: str,
    year: str,
    edition: Optional[str],
    commit_sha: str,
    include_front_cover: bool = True,
    custom_cover_rel: Optional[str] = None,
) -> str:
    included_files = {d.filename for d in docs}

    page_w = trim.width_mm + bleed_mm
    page_h = trim.height_mm + (2.0 * bleed_mm)
    in_m = trim.inside_mm
    out_m = trim.outside_mm + bleed_mm
    top_m = trim.top_mm + bleed_mm
    bot_m = trim.bottom_mm + bleed_mm

    font_chain = [font_primary]
    for fb in ("Libertinus Serif", "Palatino Linotype", "New Computer Modern Math", "Cambria Math"):
        if fb not in font_chain:
            font_chain.append(fb)
    font_tuple = "(" + ", ".join(f'"{escape_typst_string(f)}"' for f in font_chain) + ")"

    book_title_esc = escape_typst(cfg.title)
    subtitle_esc = escape_typst(cfg.subtitle)
    author_esc = escape_typst(AUTHOR_NAME)
    toc_title_esc = escape_typst(cfg.toc_title)

    out: List[str] = [
        f"""// Generated by tools/build_book.py — {cfg.title} ({trim.description})
#set document(
  title: "{escape_typst_string(cfg.title)}",
  author: "{escape_typst_string(AUTHOR_NAME)}",
)

#let current-chapter = state("current-chapter", "")

#let is-bare-page(p) = {{
  if query(<page-bare>).any(m => m.location().page() == p) {{ return true }}
  let prev-ended = query(<content-end>).any(m => m.location().page() == p - 1)
  let next-opens = (
    query(<page-opening>).any(m => m.location().page() == p + 1)
    or query(<page-bare>).any(m => m.location().page() == p + 1)
  )
  prev-ended and next-opens
}}

#set page(
  width: {page_w:.2f}mm,
  height: {page_h:.2f}mm,
  margin: (
    inside: {in_m:.2f}mm,
    outside: {out_m:.2f}mm,
    top: {top_m:.2f}mm,
    bottom: {bot_m:.2f}mm,
  ),
  header-ascent: 32%,
  footer-descent: 32%,
  header: context {{
    let p = here().page()
    if is-bare-page(p) {{ return none }}
    if query(<page-opening>).any(m => m.location().page() == p) {{ return none }}
    set text(size: 8.2pt, tracking: 0.4pt, fill: luma(85))
    if calc.even(p) {{
      align(left)[#smallcaps[{book_title_esc}]]
    }} else {{
      align(right)[#emph(current-chapter.get())]
    }}
  }},
  footer: context {{
    let p = here().page()
    if is-bare-page(p) {{ return none }}
    let num = counter(page).display()
    set text(size: 8.8pt, fill: luma(60))
    if query(<page-opening>).any(m => m.location().page() == p) {{
      align(center)[#num]
    }} else if calc.even(p) {{
      align(left)[#num]
    }} else {{
      align(right)[#num]
    }}
  }},
)

#set text(
  font: {font_tuple},
  size: {trim.body_pt}pt,
  lang: "{cfg.code}",
  hyphenate: true,
  ligatures: true,
  costs: (widow: 100%, orphan: 100%),
)

#set par(
  justify: true,
  leading: 0.68em,
  spacing: 0.68em,
  first-line-indent: (amount: 1.3em, all: false),
)

#show heading: set block(sticky: true)
#show heading.where(level: 1): it => {{
  set par(justify: false, first-line-indent: 0pt)
  block(above: 0pt, below: 16pt)[
    #text(size: 18pt, weight: "bold")[#it.body]
  ]
}}
#show heading.where(level: 2): it => {{
  set par(justify: false, first-line-indent: 0pt)
  block(above: 19pt, below: 8pt, sticky: true)[
    #text(size: 12.2pt, weight: "bold")[#it.body]
  ]
}}
#show heading.where(level: 3): it => {{
  set par(justify: false, first-line-indent: 0pt)
  block(above: 14pt, below: 6pt, sticky: true)[
    #text(size: 10.6pt, weight: "bold", style: "italic")[#it.body]
  ]
}}

#show link: it => text(fill: luma(20))[#it]
#show raw: set text(font: ("DejaVu Sans Mono", "Consolas"), size: 0.88em)

#let recto-break() = {{
  [#metadata("end") <content-end>]
  pagebreak(to: "odd", weak: true)
}}

"""
    ]

    if include_front_cover:
        if custom_cover_rel:
            cover_inner = f'#image("{escape_typst_string(custom_cover_rel)}", width: 100%, height: 100%, fit: "cover")'
        else:
            c_title_pt = 25.0 if trim.name == "a5" else 28.0
            c_sub_pt = 11.0 if trim.name == "a5" else 12.0
            c_author_pt = 12.0 if trim.name == "a5" else 13.0
            cover_inner = render_front_cover_typst_box(
                cfg,
                panel_w_mm=page_w,
                panel_h_mm=page_h,
                title_pt=c_title_pt,
                sub_pt=c_sub_pt,
                author_pt=c_author_pt,
                pad_x_mm=16.0 + (bleed_mm * 0.5),
                pad_y_mm=19.0 + bleed_mm,
            )
        out.append(
            f"""// 0. Full-bleed Front Cover (physical p. 1, recto) + blank inside-front-cover verso (physical p. 2)
#page(margin: 0pt, header: none, footer: none)[
  #metadata("bare") <page-bare>
  {cover_inner}
]
#metadata("bare") <page-bare>
#v(1pt)
#pagebreak()

"""
        )

    out.append(
        f"""// --- Front Matter (Roman numerals) ---
#set page(numbering: "i")
#counter(page).update(1)

// 1. Half-title page (p. i, recto)
#metadata("bare") <page-bare>
#v(26%)
#align(center)[
  #par(justify: false, first-line-indent: 0pt)[
    #text(size: 16pt, weight: "bold", tracking: 0.4pt)[{book_title_esc}]
  ]
]

// 2. Blank verso (p. ii) + Title page (p. iii, recto)
#recto-break()
#metadata("bare") <page-bare>
#v(22%)
#align(center)[
  #par(justify: false, first-line-indent: 0pt, leading: 0.58em)[
    #text(size: 23pt, weight: "bold")[{book_title_esc}]
  ]
  #v(10pt)
  #par(justify: false, first-line-indent: 0pt, leading: 0.68em)[
    #text(size: 11.2pt, style: "italic", fill: luma(65))[{subtitle_esc}]
  ]
  #v(26pt)
  #line(length: 26mm, stroke: 0.6pt + luma(110))
  #v(24pt)
  #par(justify: false, first-line-indent: 0pt)[
    #text(size: 12pt, tracking: 1.4pt)[#smallcaps[{author_esc}]]
  ]
]
#v(1fr)
#align(center)[
  #par(justify: false, first-line-indent: 0pt)[
    #text(size: 9.5pt, fill: luma(75))[{escape_typst(publisher)} · {escape_typst(year)}]
  ]
]

// 3. Copyright / Colophon page (p. iv, verso directly behind title page)
#pagebreak(weak: true)
#metadata("bare") <page-bare>
#v(1fr)
#block[
  #set text(size: 8.6pt, fill: luma(45))
  #set par(justify: false, first-line-indent: 0pt, leading: 0.62em, spacing: 0.85em)
  #strong[{escape_typst(cfg.colophon_heading)}]
"""
    )

    for rline in cfg.rights_lines:
        out.append(f"\n  {escape_typst(rline.format(year=year))}\n")
    if edition:
        out.append(f"\n  {escape_typst(edition)}\n")
    if publisher:
        pub_lbl = "Publisher" if cfg.code == "en" else "Wydawca"
        out.append(f"\n  {pub_lbl}: {escape_typst(publisher)}\n")
    if isbn_print:
        lbl = "ISBN (print)" if cfg.code == "en" else "ISBN (wydanie drukowane)"
        out.append(f"\n  {lbl}: {escape_typst(isbn_print)}\n")
    if isbn_epub:
        out.append(f"\n  ISBN (EPUB): {escape_typst(isbn_epub)}\n")
    rev_lbl = "Source revision" if cfg.code == "en" else "Wersja źródłowa"
    out.append(f'\n  {rev_lbl}: #raw("{escape_typst_string(commit_sha)}")\n]\n')

    # 4. Table of Contents (recto)
    out.append(
        f"""
#recto-break()
#metadata("opening") <page-opening>
#current-chapter.update("{escape_typst_string(cfg.toc_title)}")
#block(below: 16pt)[
  #set par(justify: false, first-line-indent: 0pt)
  #text(size: 18pt, weight: "bold")[{toc_title_esc}]
]
#outline(
  title: none,
  depth: 1,
  indent: 1.1em,
)
"""
    )

    # 5. Main body (Arabic numerals starting at 1 on recto)
    arabic_started = False
    emitted_parts: set[int] = set()

    for doc in docs:
        if not arabic_started:
            out.append(
                """
#recto-break()
#set page(numbering: "1")
#counter(page).update(1)
"""
            )
            arabic_started = True
        else:
            out.append("\n#recto-break()\n")

        # Emit Part divider page if starting a new Part
        if doc.kind == "chapter" and doc.part_index is not None and doc.part_index not in emitted_parts:
            emitted_parts.add(doc.part_index)
            p_lbl, p_title = part_titles[doc.part_index]
            p_full = f"{p_lbl}. {p_title}"
            out.append(
                f"""#metadata("bare") <page-bare>
#v(28%)
#align(center)[
  #par(justify: false, first-line-indent: 0pt)[
    #text(size: 10pt, tracking: 2pt, fill: luma(85))[#upper[{escape_typst(p_lbl)}]]
  ]
  #v(8pt)
  #place(hide[#heading(level: 1, outlined: true)[{escape_typst(p_full)}]])
  #par(justify: false, first-line-indent: 0pt)[
    #text(size: 20pt, weight: "bold")[{escape_typst(p_title)}]
  ]
]
#recto-break()
"""
            )

        out.append('#metadata("opening") <page-opening>\n')
        out.append(f'#current-chapter.update("{escape_typst_string(doc.full_heading)}")\n')

        # Chapter / section title block with invisible anchor + clean TOC entry
        sec_label = f"sec-{doc.doc_id}"
        if doc.label:
            toc_entry = escape_typst(f"{doc.chapter_num}. {doc.title}" if doc.chapter_num else doc.full_heading)
            out.append(
                f"""#v(14mm)
#block(below: 18pt)[
  #set par(justify: false, first-line-indent: 0pt, leading: 0.56em)
  #text(size: 9.2pt, tracking: 1.6pt, fill: luma(85))[#upper[{escape_typst(doc.label)}]]
  #v(5pt)
  #place(hide[#heading(level: 1, outlined: true)[#h(0.8em){toc_entry}] <{sec_label}>])
  #text(size: 18.5pt, weight: "bold")[{escape_typst(doc.title)}]
]
"""
            )
        else:
            out.append(
                f"""#v(12mm)
#heading(level: 1, outlined: true)[{escape_typst(doc.title)}] <{sec_label}>
"""
            )

        in_references = False
        first_para_after_break = True

        for blk in doc.blocks:
            if blk.kind == "h2":
                h_plain = inline_plain_text(blk.inlines).strip().lower()
                in_references = h_plain in ("references", "źródła")
                out.append(f"\n== {render_inlines_typst(blk.inlines, included_files)}\n\n")
                first_para_after_break = True
            elif blk.kind == "h3":
                out.append(f"\n=== {render_inlines_typst(blk.inlines, included_files)}\n\n")
                first_para_after_break = True
            elif blk.kind == "para":
                rendered = render_inlines_typst(blk.inlines, included_files)
                if in_references:
                    out.append(
                        f"#block[#set text(size: {trim.ref_pt}pt); #set par(first-line-indent: 0pt, justify: false); {rendered}]\n\n"
                    )
                elif first_para_after_break:
                    out.append(f"#par(first-line-indent: 0pt)[{rendered}]\n\n")
                else:
                    out.append(f"{rendered}\n\n")
                first_para_after_break = False
            elif blk.kind == "blockquote":
                out.append("#block(inset: (left: 11mm, right: 4mm), above: 10pt, below: 10pt)[\n")
                out.append("  #set par(first-line-indent: 0pt, justify: false, leading: 0.64em, spacing: 0.55em)\n")
                for p in blk.paragraphs:
                    out.append(f"  {render_inlines_typst(p, included_files)}\n\n")
                out.append("]\n\n")
                first_para_after_break = True
            elif blk.kind == "ul":
                out.append("#block(above: 8pt, below: 9pt)[\n  #set par(first-line-indent: 0pt)\n")
                for it in blk.items:
                    out.append(f"  - {render_inlines_typst(it.inlines, included_files)}\n")
                    for sub in it.subitems:
                        out.append(f"    - {render_inlines_typst(sub, included_files)}\n")
                out.append("]\n\n")
                first_para_after_break = True
            elif blk.kind == "ol":
                if in_references:
                    out.append(
                        f"#block(above: 6pt, below: 10pt)[\n  #set text(size: {trim.ref_pt}pt)\n  #set par(first-line-indent: 0pt, justify: false, leading: 0.58em)\n  #set enum(spacing: 0.58em)\n"
                    )
                else:
                    out.append("#block(above: 8pt, below: 9pt)[\n  #set par(first-line-indent: 0pt)\n")
                for idx_it, it in enumerate(blk.items, start=1):
                    num = it.number if it.number is not None else idx_it
                    out.append(f"  #enum.item({num})[{render_inlines_typst(it.inlines, included_files)}]\n")
                out.append("]\n\n")
                first_para_after_break = True
            elif blk.kind == "table":
                col_spec = compute_typst_col_specs(blk.headers, blk.rows)
                out.append(
                    f"""#block(above: 11pt, below: 12pt, breakable: true)[
  #set text(size: {trim.table_pt}pt)
  #set par(justify: false, first-line-indent: 0pt, leading: 0.54em)
  #table(
    columns: {col_spec},
    stroke: none,
    inset: (x: 4.5pt, y: 4.5pt),
    align: left + top,
    table.hline(stroke: 0.8pt),
    table.header(
"""
                )
                for h in blk.headers:
                    out.append(f"      [#strong[{render_inlines_typst(h, included_files)}]],\n")
                out.append("    ),\n    table.hline(stroke: 0.45pt),\n")
                for r_idx, r in enumerate(blk.rows):
                    for c in r:
                        out.append(f"    [{render_inlines_typst(c, included_files)}],\n")
                    if r_idx + 1 < len(blk.rows):
                        out.append("    table.hline(stroke: 0.2pt + luma(200)),\n")
                out.append("    table.hline(stroke: 0.8pt),\n  )\n]\n\n")
                first_para_after_break = True
            elif blk.kind == "codeblock":
                out.append(
                    f'#block(above: 8pt, below: 8pt, inset: 7pt, stroke: 0.4pt + luma(180), width: 100%)[#raw(block: true, "{escape_typst_string(blk.raw_text)}")]\n\n'
                )
                first_para_after_break = True

    return "".join(out)


# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------

def build_for_language(
    cfg: LangConfig,
    args: argparse.Namespace,
    typst_bin: Optional[pathlib.Path],
    commit_sha: str,
) -> List[pathlib.Path]:
    out_dir = pathlib.Path(args.out_dir).resolve()
    work_dir = pathlib.Path(args.work_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    work_dir.mkdir(parents=True, exist_ok=True)

    isbn_print = getattr(args, f"isbn_print_{cfg.code}", None) or args.isbn_print
    isbn_epub = getattr(args, f"isbn_epub_{cfg.code}", None) or args.isbn_epub

    part_titles, docs = load_edition_docs(
        cfg=cfg,
        include_plan=not args.no_plan,
        include_back_matter=not args.no_back_matter,
        keep_draft_markers=args.keep_draft_markers,
    )

    produced: List[pathlib.Path] = []
    formats = ("epub", "pdf") if args.format == "all" else (args.format,)

    if "epub" in formats:
        if args.cover:
            cover_path = pathlib.Path(args.cover).resolve()
        else:
            cover_path = out_dir / f"{cfg.file_slug}-cover.png"
            generate_typst_cover_png(cfg, cover_path, typst_bin, work_dir)
            produced.append(cover_path)

        out_epub = out_dir / f"{cfg.file_slug}.epub"
        build_epub(
            cfg=cfg,
            part_titles=part_titles,
            docs=docs,
            out_epub=out_epub,
            cover_img_path=cover_path,
            isbn_epub=isbn_epub,
            isbn_print=isbn_print,
            publisher=args.publisher,
            year=args.year,
            edition=args.edition,
            commit_sha=commit_sha,
        )
        produced.append(out_epub)

    if "pdf" in formats or "typ" in formats:
        trim = TRIM_SPECS[args.trim]
        custom_cover_rel: Optional[str] = None
        if args.cover and not args.no_pdf_cover:
            src_cov = pathlib.Path(args.cover).resolve()
            staged_cov = work_dir / f"custom-cover-{cfg.code}{src_cov.suffix.lower()}"
            shutil.copy2(src_cov, staged_cov)
            custom_cover_rel = staged_cov.name

        typ_src = render_typst_document(
            cfg=cfg,
            part_titles=part_titles,
            docs=docs,
            trim=trim,
            bleed_mm=args.bleed,
            font_primary=args.font,
            isbn_print=isbn_print,
            isbn_epub=isbn_epub,
            publisher=args.publisher,
            year=args.year,
            edition=args.edition,
            commit_sha=commit_sha,
            include_front_cover=not args.no_pdf_cover,
            custom_cover_rel=custom_cover_rel,
        )
        typ_path = work_dir / f"{cfg.file_slug}-{trim.name}.typ"
        typ_path.write_text(typ_src, encoding="utf-8")
        if args.format == "typ":
            produced.append(typ_path)
        else:
            if typst_bin is None:
                raise RuntimeError(
                    "Typst binary not found. Install Typst (e.g. `winget install Typst.Typst`) "
                    "or pass --typst-bin /path/to/typst."
                )
            bleed_tag = f"-bleed{args.bleed:g}mm" if args.bleed > 0 else ""
            out_pdf = out_dir / f"{cfg.file_slug}-print-{trim.name}{bleed_tag}.pdf"
            produced.append(compile_typst_pdf_safe(typst_bin, typ_path, out_pdf, work_dir))

            if args.pod_bundle:
                # Also emit the coverless POD interior block + full wrap-around POD cover spread PDF
                pod_int_typ = render_typst_document(
                    cfg=cfg,
                    part_titles=part_titles,
                    docs=docs,
                    trim=trim,
                    bleed_mm=args.bleed,
                    font_primary=args.font,
                    isbn_print=isbn_print,
                    isbn_epub=isbn_epub,
                    publisher=args.publisher,
                    year=args.year,
                    edition=args.edition,
                    commit_sha=commit_sha,
                    include_front_cover=False,
                )
                pod_int_typ_path = work_dir / f"{cfg.file_slug}-pod-interior-{trim.name}.typ"
                pod_int_typ_path.write_text(pod_int_typ, encoding="utf-8")
                pod_int_pdf = out_dir / f"{cfg.file_slug}-pod-interior-{trim.name}{bleed_tag}.pdf"
                pod_int_written = compile_typst_pdf_safe(typst_bin, pod_int_typ_path, pod_int_pdf, work_dir)
                produced.append(pod_int_written)

                interior_page_count = len(re.findall(rb"/Type\s*/Page\b", pod_int_written.read_bytes()))
                pod_cov_pdf = out_dir / f"{cfg.file_slug}-pod-cover-spread-{trim.name}.pdf"
                pod_cov_written, _ = generate_pod_wrap_cover_pdf(
                    cfg=cfg,
                    trim=trim,
                    interior_pages=interior_page_count,
                    paper_thickness_mm=args.paper_thickness_mm,
                    isbn_print=isbn_print,
                    out_pdf=pod_cov_pdf,
                    typst_bin=typst_bin,
                    work_dir=work_dir,
                )
                produced.append(pod_cov_written)

    return produced


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--lang", choices=("all", "en", "pl"), default="all", help="Language edition(s) to compile (default: all)")
    p.add_argument("--format", choices=("all", "epub", "pdf", "typ"), default="all", help="Output format(s) to generate (default: all)")
    p.add_argument(
        "--trim",
        choices=tuple(TRIM_SPECS.keys()),
        default="6x9",
        help="Print PDF trim size preset: 6x9 (KDP/US Trade), b5 (Polish 165x235mm), a5 (148x210mm) (default: 6x9)",
    )
    p.add_argument("--bleed", type=float, default=0.0, help="Print bleed in mm (default: 0 for non-bleed text interior)")
    p.add_argument("--font", default="Libertinus Serif", help="Primary body serif font for PDF (default: 'Libertinus Serif'; e.g. 'Palatino Linotype')")
    p.add_argument("--out-dir", default=str(REPO_ROOT / "dist"), help="Directory for compiled EPUB/PDF files (default: dist/)")
    p.add_argument("--work-dir", default=str(REPO_ROOT / "build"), help="Directory for intermediate Typst files (default: build/)")
    p.add_argument("--cover", help="Optional custom PNG/JPG cover image path for EPUB")
    p.add_argument("--publisher", default=AUTHOR_NAME, help=f"Publisher / imprint name on colophon (default: '{AUTHOR_NAME}')")
    p.add_argument("--year", default="2026", help="Publication / copyright year (default: 2026)")
    p.add_argument("--edition", help="Optional edition note on colophon (e.g. 'First edition' / 'Wydanie I')")
    p.add_argument("--isbn-print", help="ISBN for print edition (when building a single language)")
    p.add_argument("--isbn-epub", help="ISBN for EPUB edition (when building a single language)")
    p.add_argument("--isbn-print-en", help="ISBN for English print edition")
    p.add_argument("--isbn-epub-en", help="ISBN for English EPUB edition")
    p.add_argument("--isbn-print-pl", help="ISBN for Polish print edition")
    p.add_argument("--isbn-epub-pl", help="ISBN for Polish EPUB edition")
    p.add_argument("--no-plan", action="store_true", help="Omit '01-plan.md' from the compiled book")
    p.add_argument("--no-back-matter", action="store_true", help="Omit Contributors / Edit log back matter")
    p.add_argument("--no-pdf-cover", action="store_true", help="Omit the front cover page from the main PDF (for print-block-only uploads)")
    p.add_argument("--pod-bundle", action="store_true", help="Also generate separate Print-on-Demand interior PDF + full wrap-around cover spread PDF (Back + Spine + Front)")
    p.add_argument("--paper-thickness-mm", type=float, default=0.0572, help="Paper thickness per page in mm for POD spine calculation (default: 0.0572 for KDP white paper; ~0.0635 for cream)")
    p.add_argument("--keep-draft-markers", action="store_true", help="Keep repository draft markers and PR submission instructions")
    p.add_argument("--typst-bin", help="Explicit path to typst executable")
    return p.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    typst_bin = find_typst_binary(args.typst_bin)
    commit_sha = git_short_commit()

    langs = ("en", "pl") if args.lang == "all" else (args.lang,)
    all_outputs: List[pathlib.Path] = []

    for code in langs:
        cfg = LANG_PRESETS[code]
        outputs = build_for_language(cfg, args, typst_bin, commit_sha)
        all_outputs.extend(outputs)

    for path in all_outputs:
        size_kb = path.stat().st_size / 1024.0
        print(f"Built: {path} ({size_kb:,.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
