#!/usr/bin/env python3
"""
ONE-OFF migration: fold the four hand-written topics into the generator.

Algebra, Means & Weighted Averages, Mixtures & Alligation and Ratio, Proportion
& Variation each existed twice — once as a hand-written .md and once as a
hand-written entry in CAT-Quant-Test.html. This script merges the two copies
into a single _build/topics/*.json so the generator owns them like every other
topic.

Merge rules
  structure, type, answer, alt   <- HTML  (the answer index is tied to the
                                           HTML option order, so it is
                                           authoritative)
  options                        <- .md where it maps 1:1 onto the HTML list,
                                    otherwise HTML
  question text, hint, solution  <- .md   (the fuller of the two wordings)
  display answer (ad)            <- .md answer key
  set names, perQ, block         <- HTML
  intro lines, error audit       <- .md

Run once, from Quant/Practice:  python3 _build/migrate_legacy.py
Then delete the legacy BANK entries and re-run gen_practice.py.
"""

import difflib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
TOPICS = os.path.join(HERE, "topics")
HTML = os.path.join(PRACTICE, "CAT-Quant-Test.html")

# key in BANK, .md basename, output json, sort order, notes file
LEGACY = [
    ("algebra",  "Algebra-Practice.md",
     "algebra.json", 12, "Algebra.md", "Algebra"),
    ("ratios",   "Ratio-Proportion-Variation-Practice.md",
     "ratios.json", 22, "Ratio-Proportion-Variation.md", "Ratio, Proportion & Variation"),
    ("averages", "Means-and-Weighted-Averages-Practice.md",
     "averages.json", 24, "Means-and-Weighted-Averages.md", "Means & Weighted Averages"),
    ("mixtures", "Mixtures-and-Alligation-Practice.md",
     "mixtures.json", 26, "Mixtures-and-Alligation.md", "Mixtures & Alligation"),
]

LET = "abcde"


# ---------------------------------------------------------------- HTML side

def js_unescape(s):
    return json.loads('"' + s + '"')


def parse_bank(src, key):
    """Pull one hand-written topic out of the BANK literal."""
    hand = src.split("/* == GENERATED TOPICS")[0]
    blk = re.search(r"\n  %s: \{(.*?)\n  \},?\n" % key, hand, re.S)
    if not blk:
        raise SystemExit(f"could not locate BANK entry for {key}")
    body = blk.group(1)

    topic = {
        "name": js_unescape(re.search(r'name:\s*"((?:[^"\\]|\\.)*)"', body).group(1)),
        "perQ": int(re.search(r"perQ:\s*(\d+)", body).group(1)),
        "sets": [],
    }

    # each set: "      X: { name: "...", [block: N,] qs: [ ... ]}"
    for sm in re.finditer(
            r'\n      ([A-Z]): \{ name: "((?:[^"\\]|\\.)*)",(?: block: (\d+),)? qs: \[(.*?)\n      \]\}',
            body, re.S):
        sid, sname, block, qs_body = sm.groups()
        st = {"id": sid, "name": js_unescape(sname), "qs": []}
        if block:
            st["block"] = int(block)

        # split into individual question objects
        chunks = re.split(r"\n\s*\{ id:", qs_body)
        for ch in chunks[1:]:
            ch = "{ id:" + ch
            q = {}
            q["id"] = js_unescape(re.search(r'id:"((?:[^"\\]|\\.)*)"', ch).group(1))
            q["t"] = re.search(r't:"(\w+)"', ch).group(1)
            q["q"] = js_unescape(re.search(r'q:"((?:[^"\\]|\\.)*)"', ch).group(1))
            if q["t"] == "mcq":
                opts = re.search(r"o:\[(.*?)\],\s*a:(\d+)", ch, re.S)
                q["o"] = [js_unescape(x) for x in
                          re.findall(r'"((?:[^"\\]|\\.)*)"', opts.group(1))]
                q["a"] = int(opts.group(2))
            else:
                am = re.search(r"\sa:\s*(-?[\d.]+(?:/-?[\d.]+)?)", ch)
                raw = am.group(1)
                q["a"] = raw if "/" in raw else (
                    int(raw) if re.fullmatch(r"-?\d+", raw) else float(raw))
                alt = re.search(r"alt:\[(.*?)\]", ch, re.S)
                if alt:
                    q["alt"] = [js_unescape(x) for x in
                                re.findall(r'"((?:[^"\\]|\\.)*)"', alt.group(1))]
            hm = re.search(r'\n\s*h:"((?:[^"\\]|\\.)*)"', ch)
            sm2 = re.search(r'\n\s*s:"((?:[^"\\]|\\.)*)"', ch)
            q["h"] = js_unescape(hm.group(1)) if hm else ""
            q["s"] = js_unescape(sm2.group(1)) if sm2 else ""
            st["qs"].append(q)
        topic["sets"].append(st)
    return topic


# ---------------------------------------------------------------- markdown side

def parse_md(path):
    txt = open(path, encoding="utf-8").read()
    split = re.split(r"\n#+ Answer [Kk]ey\s*\n", txt, maxsplit=1)
    if len(split) != 2:
        raise SystemExit(f"{os.path.basename(path)}: could not find the answer key heading")
    head, key_part = split

    # intro: blockquote paragraphs after the "Suggested timing" line
    quote = [l[2:].strip() for l in head.split("\n") if l.startswith("> ")]
    intro = []
    seen_timing = False
    for line in quote:
        if line.startswith("Suggested timing"):
            seen_timing = True
            continue
        if seen_timing and line:
            intro.append(line)

    # questions
    qs = {}
    blocks = re.split(r"\n\*\*([A-Z]\d+)\.\*\* \((MCQ|TITA)\) ", "\n" + head)
    for i in range(1, len(blocks), 3):
        qid, _kind, rest = blocks[i], blocks[i + 1], blocks[i + 2]
        rest = rest.split("\n---")[0]
        lines = rest.split("\n")
        qtext = lines[0].strip()
        opts = [m.group(1).strip() for m in
                (re.match(r"- \([a-e]\) (.+)", l.strip()) for l in lines) if m]
        hint = ""
        hm = re.search(r"^\*Hint: (.+)\*$", rest, re.M)
        if hm:
            hint = hm.group(1).strip()
        qs[qid] = {"q": qtext, "o": opts, "h": hint}

    # answer key
    keys = {}
    for m in re.finditer(r"^\*\*([A-Z]\d+) — (.+?)\.\*\*\s*(.*)$", key_part, re.M):
        qid, disp, sol = m.group(1), m.group(2).strip(), m.group(3).strip()
        keys[qid] = {"ad": disp, "s": sol}

    # error audit table
    audit = []
    am = re.search(r"\*\*Common error audit\*\*.*?\n\|[^\n]*\|\n\|[-|\s]*\|\n(.*?)(?:\n\s*\n|$)",
                   key_part, re.S)
    if am:
        for row in am.group(1).strip().split("\n"):
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) == 2:
                audit.append(cells)
    return intro, qs, keys, audit


# ---------------------------------------------------------------- merge

def norm(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("₹", "").replace(",", "").replace("−", "-").replace("’", "'")
    return re.sub(r"\s+", " ", s).strip().lower().rstrip(".:")


def bold_answer(sol, disp):
    """The generated solutions bold their final answer; re-create that where possible."""
    if not sol or not disp or "<b>" in sol:
        return sol
    cand = re.sub(r"^\([a-e]\)\s*", "", disp).strip()
    for form in (cand, cand.replace("₹", ""), cand.replace(",", "")):
        if not form:
            continue
        idx = sol.rfind(form)
        if idx != -1:
            return sol[:idx] + "<b>" + form + "</b>" + sol[idx + len(form):]
    return sol


def main():
    src = open(HTML, encoding="utf-8").read()
    report = []

    for key, mdname, outname, order, notes, _label in LEGACY:
        topic = parse_bank(src, key)
        intro, mdqs, mdkeys, audit = parse_md(os.path.join(PRACTICE, mdname))

        stats = dict(q=0, q_md=0, o_md=0, h_md=0, s_md=0, ad=0, missing=[])
        for st in topic["sets"]:
            for q in st["qs"]:
                stats["q"] += 1
                m = mdqs.get(q["id"])
                k = mdkeys.get(q["id"])
                if not m:
                    stats["missing"].append(q["id"])
                    continue
                # question text: prefer the markdown (fuller) wording
                if m["q"] and norm(m["q"]) != norm(q["q"]):
                    q["q"] = m["q"]
                    stats["q_md"] += 1
                # options: only if they map 1:1 in the same order
                if q["t"] == "mcq" and len(m["o"]) == len(q["o"]):
                    if all(difflib.SequenceMatcher(None, norm(a), norm(b)).ratio() > 0.6
                           for a, b in zip(m["o"], q["o"])):
                        if m["o"] != q["o"]:
                            stats["o_md"] += 1
                        q["o"] = m["o"]
                # hint
                if m["h"] and norm(m["h"]) != norm(q["h"]):
                    q["h"] = m["h"]
                    stats["h_md"] += 1
                # solution + display answer
                if k:
                    if k["ad"]:
                        disp = k["ad"]
                        if q["t"] == "mcq":
                            # generator renders "(x) option" itself
                            plain = re.sub(r"^\([a-e]\)\s*", "", disp).strip()
                            if norm(plain) != norm(q["o"][q["a"]]):
                                q["ad"] = disp
                        else:
                            auto = str(q["a"])
                            if norm(disp) != norm(auto):
                                q["ad"] = disp
                                stats["ad"] += 1
                    if k["s"] and norm(k["s"]) != norm(q["s"]):
                        q["s"] = bold_answer(k["s"], k["ad"])
                        stats["s_md"] += 1

        out = {
            "key": key, "order": order, "name": topic["name"], "notes": notes,
            "file": mdname, "perQ": topic["perQ"], "intro": intro,
            "sets": topic["sets"], "audit": audit,
        }
        with open(os.path.join(TOPICS, outname), "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
            f.write("\n")
        report.append((mdname, stats, len(audit), len(intro)))

    print(f"{'topic':<44}{'qs':>4}{'text':>6}{'opts':>6}{'hint':>6}{'soln':>6}{'audit':>7}")
    for name, s, na, ni in report:
        print(f"  {name:<42}{s['q']:>4}{s['q_md']:>6}{s['o_md']:>6}"
              f"{s['h_md']:>6}{s['s_md']:>6}{na:>7}")
        if s["missing"]:
            print(f"      !! not found in the .md: {s['missing']}")
    print("\n(text/opts/hint/soln = how many took the fuller markdown version)")


if __name__ == "__main__":
    main()
