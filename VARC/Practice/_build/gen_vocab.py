#!/usr/bin/env python3
"""
Single source of truth for the VARC vocabulary material.

Reads _build/words.json and emits:
  1. VARC/Vocabulary.md        — the readable word list, grouped by meaning
  2. VARC/Practice/Vocab-Trainer.html — the interactive MCQ trainer

Run:  python3 _build/gen_vocab.py
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PRACTICE = os.path.dirname(HERE)
VARC = os.path.dirname(PRACTICE)
WORDS = os.path.join(HERE, "words.json")
MD_OUT = os.path.join(VARC, "Vocabulary.md")
HTML_OUT = os.path.join(PRACTICE, "Vocab-Trainer.html")
TEMPLATE = os.path.join(HERE, "trainer_template.html")

POS_LONG = {"n": "noun", "v": "verb", "adj": "adjective", "adv": "adverb"}


def validate(data):
    problems, seen = [], {}
    for g in data["groups"]:
        if not g.get("name") or not g.get("words"):
            problems.append(f"group {g.get('name','?')}: empty")
        for w in g["words"]:
            tag = w.get("w", "?")
            if tag in seen:
                problems.append(f"{tag}: duplicate (also in {seen[tag]})")
            seen[tag] = g["name"]
            for field in ("pos", "def", "sent"):
                if not w.get(field):
                    problems.append(f"{tag}: missing {field}")
            if w.get("pos") not in POS_LONG:
                problems.append(f"{tag}: unknown part of speech {w.get('pos')!r}")
            if len(w.get("syn", [])) < 3:
                problems.append(f"{tag}: needs at least 3 synonyms")
            if len(w.get("ant", [])) < 2:
                problems.append(f"{tag}: needs at least 2 antonyms")
            overlap = set(x.lower() for x in w.get("syn", [])) & set(
                x.lower() for x in w.get("ant", []))
            if overlap:
                problems.append(f"{tag}: {sorted(overlap)} listed as both synonym and antonym")
            if w["w"].lower() in [x.lower() for x in w.get("syn", []) + w.get("ant", [])]:
                problems.append(f"{tag}: lists itself as its own synonym or antonym")
            if w["def"].rstrip().endswith("."):
                problems.append(f"{tag}: definition should not end with a full stop")
    return problems


def render_md(data):
    total = sum(len(g["words"]) for g in data["groups"])
    L = [f"# {data['title']}", "",
         f"> {data['note']}", ">",
         f"> {total} words in {len(data['groups'])} groups. "
         "Drill them in `Practice/Vocab-Trainer.html`, which builds definition, "
         "synonym and antonym MCQs from this same list and remembers what you miss.", "",
         "---", "", "## Groups", "", "| Group | Words |", "|---|---|"]
    for g in data["groups"]:
        L.append(f"| {g['name']} | {', '.join(w['w'] for w in g['words'])} |")
    L += ["", "---", ""]

    for g in data["groups"]:
        L += [f"## {g['name']}", ""]
        for w in g["words"]:
            L.append(f"**{w['w']}** *({POS_LONG[w['pos']]})* — {w['def']}.")
            L.append("")
            L.append(f"Syn: {', '.join(w['syn'])} · Ant: {', '.join(w['ant'])}")
            L.append("")
            L.append(f"*“{w['sent']}”*")
            L.append("")
        L.append("---")
        L.append("")
    return "\n".join(L).rstrip() + "\n"


def render_html(data):
    with open(TEMPLATE, encoding="utf-8") as f:
        tpl = f.read()
    total = sum(len(g["words"]) for g in data["groups"])
    payload = json.dumps(data["groups"], ensure_ascii=False, separators=(",", ":"))
    return (tpl
            .replace("/*__GROUPS__*/null", payload)
            .replace("__TOTAL__", str(total))
            .replace("__NGROUPS__", str(len(data["groups"]))))


def main():
    with open(WORDS, encoding="utf-8") as f:
        data = json.load(f)

    problems = validate(data)
    if problems:
        print("VALIDATION FAILED:")
        for p in problems:
            print("  -", p)
        sys.exit(1)

    with open(MD_OUT, "w", encoding="utf-8") as f:
        f.write(render_md(data))
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(render_html(data))

    total = sum(len(g["words"]) for g in data["groups"])
    print(f"  wrote Vocabulary.md        {total} words in {len(data['groups'])} groups")
    print(f"  wrote Vocab-Trainer.html   definition + synonym + antonym MCQs")


if __name__ == "__main__":
    main()
