#!/usr/bin/env python3
"""
Single source of truth for CAT Quant practice material.

Each topic lives as one JSON file in _build/topics/. This script emits, for every topic:
  1. <Topic>-Practice.md   — the readable practice set with hints and a full answer key
  2. a BANK entry injected into CAT-Quant-Test.html — the interactive version

Run:  python3 _build/gen_practice.py
"""

import json
import math
import os
import re
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
TOPICS_DIR = os.path.join(HERE, "topics")
HTML = os.path.join(PRACTICE, "CAT-Quant-Test.html")

LET = ["a", "b", "c", "d", "e"]

# Namespace available to the optional "check" expression on each question.
SAFE = {
    "abs": abs, "min": min, "max": max, "sum": sum, "pow": pow, "round": round,
    "range": range, "len": len, "int": int, "float": float, "sorted": sorted,
    "all": all, "any": any, "set": set, "list": list,
    "Fraction": Fraction, "gcd": math.gcd, "comb": math.comb, "perm": math.perm,
    "factorial": math.factorial, "sqrt": math.sqrt, "log": math.log,
    "log10": math.log10, "log2": math.log2, "floor": math.floor, "ceil": math.ceil,
    "pi": math.pi, "e": math.e,
}

# ---------------------------------------------------------------- helpers


def html_to_md(s):
    """Solutions are authored with <b>…</b> so the HTML test can render them."""
    s = re.sub(r"</?b>", "**", s)
    return s


def num_literal(a):
    """Emit a JS numeric literal, preferring exact fractions over rounded decimals."""
    if isinstance(a, str):
        m = re.fullmatch(r"\s*(-?\d+)\s*/\s*(-?\d+)\s*", a)
        if m:
            return f"{m.group(1)}/{m.group(2)}"
        return json.dumps(a)
    if isinstance(a, bool):
        raise ValueError("boolean answer")
    if isinstance(a, int):
        return str(a)
    return repr(float(a))


def answer_value(q):
    """Numeric value of a TITA answer, for verification."""
    a = q["a"]
    if isinstance(a, str):
        m = re.fullmatch(r"\s*(-?\d+)\s*/\s*(-?\d+)\s*", a)
        if m:
            return float(Fraction(int(m.group(1)), int(m.group(2))))
        return float(a)
    return float(a)


def display_answer(q):
    if "ad" in q:
        return q["ad"]
    if q["t"] == "mcq":
        return f"({LET[q['a']]}) {q['o'][q['a']]}"
    if q.get("alt"):
        return q["alt"][0]
    a = q["a"]
    if isinstance(a, float) and a == int(a):
        return str(int(a))
    return str(a)


def js_str(s):
    return json.dumps(s, ensure_ascii=False)


# ---------------------------------------------------------------- markdown


def render_md(topic):
    L = []
    L.append(f"# {topic['name']} — Practice Sets")
    L.append("")
    L.append(f"> Companion to `{topic['notes']}`. Hints point to the section of the notes "
             "that contains the intended method — read the hint only after you've been stuck "
             "for a minute. Answer key with short solutions is at the bottom.")
    L.append(">")
    L.append("> **TITA** = type-in-the-answer (no options). **MCQ** = choose one.")
    L.append(">")
    mins = max(1, round(topic.get("perQ", 90) / 60 * 2) / 2)
    last = topic["sets"][-1]["id"]
    span = f"Sets {topic['sets'][0]['id']}–{topic['sets'][-2]['id']}" if len(topic["sets"]) > 1 else "all sets"
    L.append(f"> Suggested timing: {mins} min/question for {span}, and attempt the "
             f"{'Mixed Set' if last == 'M' else 'final set'} in one timed block.")
    for line in topic.get("intro", []):
        L.append(">")
        L.append(f"> {line}")
    L.append("")
    L.append("---")
    L.append("")

    for st in topic["sets"]:
        L.append(f"## Set {st['id']} — {st['name']}" if st["id"] != "M"
                 else f"## Mixed Set — {st['name']}")
        L.append("")
        for q in st["qs"]:
            kind = "MCQ" if q["t"] == "mcq" else "TITA"
            L.append(f"**{q['id']}.** ({kind}) {q['q']}")
            L.append("")
            if q["t"] == "mcq":
                for i, o in enumerate(q["o"]):
                    L.append(f"- ({LET[i]}) {o}")
                L.append("")
            if st["id"] != "M" and q.get("h"):
                L.append(f"*Hint: {html_to_md(q['h'])}*")
                L.append("")
        L.append("---")
        L.append("")

    L.append("# Answer key")
    L.append("")
    for st in topic["sets"]:
        L.append(f"## Set {st['id']}" if st["id"] != "M" else "## Mixed Set")
        L.append("")
        for q in st["qs"]:
            L.append(f"**{q['id']} — {display_answer(q)}.** {html_to_md(q['s'])}")
            L.append("")

    if topic.get("audit"):
        L.append("---")
        L.append("")
        L.append("**Common error audit** — if you got a question wrong, find it here before moving on:")
        L.append("")
        L.append("| Question | The error it is designed to catch |")
        L.append("|---|---|")
        for qs, err in topic["audit"]:
            L.append(f"| {qs} | {err} |")
        L.append("")

    return "\n".join(L).rstrip() + "\n"


# ---------------------------------------------------------------- javascript


def render_js(topic, indent="  "):
    i1, i2, i3, i4 = indent, indent * 2, indent * 3, indent * 4
    L = [f"{i1}{topic['key']}: {{",
         f"{i2}name: {js_str(topic['name'])},",
         f"{i2}perQ: {topic.get('perQ', 90)},",
         f"{i2}sets: {{"]
    for si, st in enumerate(topic["sets"]):
        head = f"{i3}{st['id']}: {{ name: {js_str(st['name'] if st['id'] != 'M' else 'Mixed Set — ' + st['name'])},"
        if st.get("block"):
            head += f" block: {st['block']},"
        head += " qs: ["
        L.append(head)
        for qi, q in enumerate(st["qs"]):
            parts = [f"id:{js_str(q['id'])}", f"t:{js_str(q['t'])}", f"q:{js_str(q['q'])}"]
            if q["t"] == "mcq":
                parts.append("o:[" + ",".join(js_str(o) for o in q["o"]) + "]")
                parts.append(f"a:{q['a']}")
            else:
                parts.append(f"a:{num_literal(q['a'])}")
                if q.get("alt"):
                    parts.append("alt:[" + ",".join(js_str(x) for x in q["alt"]) + "]")
            line = f"{i4}{{ " + ", ".join(parts) + ","
            L.append(line)
            L.append(f"{i4}  h:{js_str(q.get('h', ''))},")
            tail = "," if qi < len(st["qs"]) - 1 else ""
            L.append(f"{i4}  s:{js_str(q['s'])} }}{tail}")
        L.append(f"{i3}]}}" + ("," if si < len(topic["sets"]) - 1 else ""))
    L.append(f"{i2}}}")
    L.append(f"{i1}}}")
    return "\n".join(L)


# ---------------------------------------------------------------- checks


def validate(topic):
    problems = []
    seen = set()
    for st in topic["sets"]:
        for q in st["qs"]:
            tag = f"{topic['key']}.{q['id']}"
            if q["id"] in seen:
                problems.append(f"{tag}: duplicate id")
            seen.add(q["id"])
            if not q.get("s"):
                problems.append(f"{tag}: missing solution")
            if st["id"] != "M" and not q.get("h"):
                problems.append(f"{tag}: missing hint")
            if q["t"] == "mcq":
                if not isinstance(q.get("o"), list) or len(q["o"]) < 2:
                    problems.append(f"{tag}: bad options")
                elif not isinstance(q["a"], int) or not (0 <= q["a"] < len(q["o"])):
                    problems.append(f"{tag}: answer index out of range")
                elif len(set(q["o"])) != len(q["o"]):
                    problems.append(f"{tag}: duplicate options")
            else:
                try:
                    answer_value(q)
                except Exception:
                    problems.append(f"{tag}: TITA answer is not numeric")
            if "check" in q:
                try:
                    got = eval(q["check"], {"__builtins__": SAFE}, {})
                except Exception as e:
                    problems.append(f"{tag}: check expression failed ({e})")
                    continue
                want = q["a"] if q["t"] == "mcq" else answer_value(q)
                if q["t"] == "mcq":
                    if int(got) != int(want):
                        problems.append(f"{tag}: check gives index {got}, stated {want}")
                else:
                    if abs(float(got) - float(want)) > max(0.005, abs(float(want)) * 1e-6):
                        problems.append(f"{tag}: check gives {got}, stated {want}")
    return problems


# ---------------------------------------------------------------- html patch

BEGIN = "/* == GENERATED TOPICS: do not edit by hand, see _build/gen_practice.py == */"
END = "/* == END GENERATED TOPICS == */"


def patch_html(blocks):
    with open(HTML, encoding="utf-8") as f:
        src = f.read()

    payload = BEGIN + "\n" + ",\n".join(blocks) + "\n" + END

    if BEGIN in src:
        start = src.index(BEGIN)
        end = src.index(END) + len(END)
        return src[:start] + payload + src[end:]

    # First run: splice in just before the closing brace of `const BANK = { … };`
    m = re.search(r"const BANK = \{", src)
    if not m:
        raise SystemExit("could not find `const BANK = {` in the HTML")
    depth = 0
    i = m.end() - 1
    while i < len(src):
        if src[i] == "{":
            depth += 1
        elif src[i] == "}":
            depth -= 1
            if depth == 0:
                break
        i += 1
    # i is the closing brace of BANK; back up over trailing whitespace
    j = i
    while src[j - 1] in " \n\t":
        j -= 1
    return src[:j] + ",\n" + payload + "\n" + src[i:]


# ---------------------------------------------------------------- main


def main():
    files = sorted(f for f in os.listdir(TOPICS_DIR) if f.endswith(".json"))
    if not files:
        raise SystemExit("no topic JSON files found in _build/topics/")

    topics, blocks, problems = [], [], []
    order = []
    for fn in files:
        with open(os.path.join(TOPICS_DIR, fn), encoding="utf-8") as f:
            t = json.load(f)
        topics.append(t)
        problems += validate(t)
        order.append((t.get("order", 999), t))

    if problems:
        print("VALIDATION FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    order.sort(key=lambda x: (x[0], x[1]["key"]))
    for _, t in order:
        blocks.append(render_js(t))
        out = os.path.join(PRACTICE, t["file"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(render_md(t))
        n = sum(len(s["qs"]) for s in t["sets"])
        print(f"  wrote {t['file']:<52} {n:>3} questions")

    new = patch_html(blocks)
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(new)
    total = sum(sum(len(s["qs"]) for s in t["sets"]) for t in topics)
    print(f"  patched CAT-Quant-Test.html with {len(topics)} generated topics "
          f"({total} questions)")


if __name__ == "__main__":
    main()
