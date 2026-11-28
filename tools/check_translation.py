"""Compare a translation folder with book/ file by file.

Usage: python3 tools/check_translation.py book translations/pl

Checks structure (paragraphs, headings, lists, tables), citation numbers per
paragraph, links and numbers. Number formats are normalised for Polish
(decimal comma, space as thousands separator); adapt nums_pl for other
languages. It cannot judge wording.
"""
import re, sys, pathlib
src_dir, tr_dir = map(pathlib.Path, sys.argv[1:3])
def body(p):
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"^<!--.*?-->\s*", "", t, flags=re.S)
    return t
def nonempty(t): return [l for l in t.split("\n") if l.strip()]
def cites(t): return re.findall(r"\((\d+(?:, \d+)*)\)", t)
def urls(t): return re.findall(r"https?://\S+", t)
def nums_en(t):
    t = re.sub(r"https?://\S+", "", t)
    out = []
    for m in re.findall(r"\d[\d,]*(?:\.\d+)?", t):
        m = m.rstrip(",")
        m = re.sub(r",(?=\d{3}\b)", "", m)
        out += [x for x in m.split(",") if x]
    return sorted(out)
def nums_pl(t):
    t = re.sub(r"https?://\S+", "", t)
    t = re.sub(r"(?<=\d)[  ](?=\d{3}\b)", "", t)
    out = []
    for m in re.findall(r"\d+(?:,\d+)?", t):
        out.append(m.replace(",", "."))
    return sorted(out)
ok = True
for s in sorted(src_dir.glob("*.md")):
    if s.name in ("contributors.md", "edit-log.md"): continue
    t = tr_dir / s.name
    if not t.exists(): print("MISSING", s.name); ok = False; continue
    a, b = body(s), body(t)
    la, lb = nonempty(a), nonempty(b)
    probs = []
    if len(la) != len(lb): probs.append(f"lines {len(la)} vs {len(lb)}")
    for lvl in ("# ", "## ", "### "):
        ca = sum(l.startswith(lvl) for l in la); cb = sum(l.startswith(lvl) for l in lb)
        if ca != cb: probs.append(f"headings '{lvl}' {ca} vs {cb}")
    for kind, f in (("table rows", lambda l: l.startswith("|")), ("bullets", lambda l: l.startswith("- ")), ("numbered", lambda l: re.match(r"\d+\. ", l)), ("quotes", lambda l: l.startswith(">"))):
        ca = sum(bool(f(l)) for l in la); cb = sum(bool(f(l)) for l in lb)
        if ca != cb: probs.append(f"{kind} {ca} vs {cb}")
    if cites(a) != cites(b): 
        probs.append(f"citations differ: {len(cites(a))} vs {len(cites(b))}")
    if urls(a) != urls(b): probs.append("urls differ")
    if a.count("**") != b.count("**"): probs.append(f"bold markers {a.count('**')} vs {b.count('**')}")
    na, nb = nums_en(a), nums_pl(b)
    if na != nb:
        from collections import Counter
        d1 = Counter(na) - Counter(nb); d2 = Counter(nb) - Counter(na)
        probs.append(f"numbers only-in-src {dict(d1)} only-in-pl {dict(d2)}")
    if "—" in b: probs.append("em dash present")
    if re.search(r'“', b) : probs.append("English opening quote")
    # line-by-line kind alignment
    if len(la) == len(lb):
        for i,(x,y) in enumerate(zip(la,lb)):
            kx = re.match(r"(#+ |\| |- |\d+\. |> |\*\*|\*)?", x).group(0); ky = re.match(r"(#+ |\| |- |\d+\. |> |\*\*|\*)?", y).group(0)
            if kx != ky: probs.append(f"line {i} kind '{kx}' vs '{ky}': {y[:50]}")
            if cites(x) != cites(y): probs.append(f"line {i} cites {cites(x)} vs {cites(y)}: {y[:50]}")
    print(("OK  " if not probs else "DIFF"), s.name)
    for p in probs: print("     ", p); ok = False
sys.exit(0 if ok else 1)
