#!/usr/bin/env python3
"""Mechanical checks for an Abstract/Introduction draft (.tex, .md or .txt).

Style checks compare the draft with:
1. The empirical distribution of 55 CVPR/ICCV/NeurIPS award papers (corpus_stats.json)
2. The 26 anti-AI tell patterns from WikiProject AI Cleanup / Humanizer
3. Discourse-level narrative and agency signatures from StoryScope (COLM 2026)
4. Context-aware exemptions to prevent false positives in mathematics and physical terminology

Levels:
  ERROR: Must fix before submission (hard rules, dashes, banned boilerplate, workflow traces)
  WARN:  Outside the p10-p90 range of award papers, known AI habits, or discourse anomalies
  NOTE:  Information and strategic recommendations

Usage:
  python3 scripts/check_draft.py FILE [FILE ...] [--max-words 60] [--triage]
Exit code 1 if any ERROR is found.
"""
import argparse, csv, json, re, statistics, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import style_metrics as sm

ROOT = Path(__file__).resolve().parent.parent
BANK = ROOT / "references/exemplars/moves.jsonl"
PARAS = ROOT / "references/exemplars/paragraphs.jsonl"
PHRASES = ROOT / "references/exemplars/phrasebank.csv"

# ============================================================================
# ERROR PATTERNS: Zero-tolerance violations
# ============================================================================
ERROR_PHRASES = {
    # 1. Punctuation & Formatting (Hard Rule: No Dashes)
    r"—|---|(\s–\s)|(\s--\s)": "em/en dash used as connector (No Dashes rule; use colon, comma, or split sentence)",

    # 2. Boilerplate, Stock AI Openers & Inflated Claims (§12, §13)
    r"has attracted (increasing|growing|more and more|much) attention": "boilerplate opening",
    r"hot topic": "boilerplate opening",
    r"plays an? (important|vital|key|crucial|significant) role\s*(in [^.,;]*)?[.;]": "bare 'plays an important role' (provide mechanism or delete)",
    r"extensive experiments (demonstrate|show|verify|validate) the (effectiveness|superiority)": "boilerplate claim",
    r"\bsuperiority\b": "self-praise",
    r"\bdelve(s|d|ing)?\b": "LLM tell ('delve')",
    r"\bpivotal\b": "LLM tell ('pivotal')",
    r"paradigm shift": "LLM tell ('paradigm shift')",
    r"unlock(s|ing)? the (full )?potential": "LLM tell ('unlock potential')",
    r"\bseamless(ly)?\b": "LLM tell ('seamless')",
    r"a myriad of": "LLM tell ('a myriad of')",
    r"\blandscape\b": "LLM tell (metaphorical 'landscape'; valid only in loss/optimization landscape)",
    r"in the realm of": "LLM tell ('in the realm of')",
    r"\btapestry\b": "LLM tell (metaphorical 'tapestry')",
    r"it is worth noting that": "filler phrase",
    r"it can be seen that": "filler phrase",
    r"simple yet effective": "cliché phrase",
    r"comprehensive experiments": "boilerplate phrase",
    # Context-aware: experiments/evaluations do not 'prove' (mathematical theorems do!)
    r"(?:experiments?|results?|benchmarks?|evaluations?|data)\s+(?:prove|proves)\b|\bthis proves\b": "empirical experiments do not 'prove' (use demonstrates, indicates, establishes)",

    # 3. Humanizer Specific Tells (§1, §2, §3, §4, §16, §18)
    r"\bnot merely\b.*?\bbut rather\b|\bnot just\b.*?\bbut also\b": "staged antithesis ('not just X but Y'; state point directly)",
    r"(that is the (true|real) win|efficiency achieved|let that sink in|read that again)\b": "dramatic one-line closer / slogan",
    r"\bat its core,?\b": "pseudo-profound saying ('at its core')",
    r"\bhere is the (key )?takeaway\b|\bto understand why this happens, we must\b": "staged run-up before point",
    r"\b(breathtaking|groundbreaking|stunning)\b": "sales language / promotional puffery",
    r"\bserves as a (foundation|cornerstone|testament|bridge)\b": "avoiding plain copula ('serves as')",

    # 4. StoryScope Tells: Anthropomorphism & Preachy Moralizing
    r"\bthe model (understands|perceives|contemplates|desires|believes)\b": "anthropomorphic agency (attribute to loss, gradient, or formulation)",
    r"\bpaving the way for safe, ethical(,| and) universally accessible\b": "thematic moralizing / preachiness",

    # 5. Workflow Traces & Leaked Apparatus (§22, §25)
    r"\bsupplied\b": "workflow trace ('supplied')",
    r"\bprovided (results|evaluation|numbers|data|facts|input)\b|\bthe provided\b": "workflow trace ('provided …')",
    r"\bthe reported (evaluation|results|experiments)\b|\bin the reported\b": "workflow trace ('reported …')",
    r"according to the (input|user|notes)": "workflow trace",
    r"\[(intro|abstract|relwork|method|exp)\.[a-z\-.]+\]": "move tag left in text",
    r"→": "arrow (likely a move label) left in text",
    r"\b(i hope this helps|as requested|below is the revised)\b": "chatbot residue",

    # 6. Disclaimers & Self-Undermining (Forbidden in Abstract/Intro; move to Limitations)
    r"does not (establish|imply|guarantee|isolate|prove)\b|do not (establish|imply|isolate)\b": "disclaimer (move to Limitations)",
    r"remains? to be (evaluated|tested|seen|explored)": "disclaimer (move to Limitations)",
    r"\bone limitation\b|\blimitations? of (our|this)\b|\bour (method|approach|model) (still )?(fails|is limited)\b": "limitation in abstract/introduction",
    r"\bleave [^.]* (for|to) future work\b": "future-work disclaimer",

    # 7. Defensive Protocol Qualifiers
    r"\bin our comparisons?\b|\bwithin the tested\b|\bunder the tested\b|\bin the evaluated setting\b|\bscores? (are|is) computed on\b|\bunder identical hyperparameters\b": "defensive qualifier (move to experiments)",

    # 8. Downgraded Core Idea
    r"\bour hypothesis is\b|\bwe take the view\b|\bwe conjecture\b": "core idea downgraded to a hypothesis (state as direct observation)",
}

# ============================================================================
# WARN PATTERNS: Review needed (known LLM habits or borderline phrasing)
# ============================================================================
WARN_PHRASES = {
    r"\bto the best of our knowledge\b": "only use with a strictly scoped claim",
    r"\btables? \d+ (reports|shows)\b|\btab\.\s*\d+ (reports|shows)\b": "put the claim first and cite the table parenthetically",
    r"\bin our setup\b": "hedge-like phrase; state exact benchmark parameters instead",
    r"\bbolstered\b": "overused AI verb ('bolstered')",
    r"\bintricate\b|\bintricacies\b": "overused AI word ('intricate')",
    r"\binterplay\b": "overused AI word ('interplay')",
    r"\btestament\b": "inflated significance ('testament')",
    r"\bgarner(ed|s|ing)?\b": "overused AI verb ('garner')",
    r"\bshowcase(s|d|ing)?\b": "overused AI verb ('showcase')",
    r"\bunderscore(s|d|ing)?\b": "overused AI verb ('underscore')",
    r"\bvibrant\b": "overused AI adjective ('vibrant')",
    r"\bto be clear,?\b|\bdon't get us wrong\b": "phantom defense / arguing with no one (§5)",
}

# ============================================================================
# NOTE PATTERNS: Informational guidance
# ============================================================================
NOTE_PHRASES = {
    r"\b(very|extremely|outstanding)\b": "intensifier; a number or mechanism is usually stronger",
    r"\bin order to\b": "'to' is usually sufficient",
    r"\bnovel\b": "fine if the sentence also specifies what is new",
    r"\bsignificant(ly)?\b": "fine with a number or statistical test nearby",
    r"state[- ]of[- ]the[- ]art|\bSOTA\b": "name the benchmark/baselines in the same sentence",
    r"\bthe first\b|\bfor the first time\b": "ensure the scope is strictly defined",
    r"\beliminat(e|es|ing)\b": "absolute claim; verify with claim calibration",
}

DETAIL = r"\b\d+ (layers?|heads?|views?|steps?|epochs?|tokens? per)\b|\d+\s*[×x]\s*\d+\s*[×x]\s*\d+|\bbatch size\b|\blearning rate of\b|\bhidden (size|dimension)\b"
NUMBER = r"(?<![A-Za-z\d.])\d+(?:[.,]\d+)*(?![A-Za-z\d])"
SECNAME = {"abstract": "abstract", "intro": "introduction"}
COMPARE = r"\b(outperform\w*|surpass\w*|better than|improv\w+|reduc\w+|faster|higher|lower|exceed\w*)\b"

# Trailing participle checker
TRAILING_PARTICIPLE = re.compile(r",\s*(?:thereby\s+)?(making|enabling|unlocking|extending|allowing|bringing|yielding|demonstrating|highlighting|paving|opening|setting|underscoring|emphasizing|fostering|ensuring)\b[^.?!;]*[.?!;]?$", re.I)

# Context-aware exemption for legitimate mathematical concepts
VALID_LANDSCAPE = re.compile(r"\b(?:loss|optimization|energy|fitness|rugged|complex|surface)\s+landscape\b", re.I)

BODY_SKIP = {
    "disclaimer (move to Limitations)", "limitation in abstract/introduction",
    "future-work disclaimer", "defensive qualifier (move to experiments)",
    "core idea downgraded to a hypothesis"
}


def strip_latex(t):
    t = re.sub(r"(?<!\\)%.*", "", t)
    t = re.sub(r"\\(begin|end)\{[^}]*\}", "", t)
    t = re.sub(r"\\(cite[tp]?|citep|citet|ref|eqref|label)\*?(\[[^\]]*\])?\{[^}]*\}", " [c] ", t)
    t = re.sub(r"\\(section|subsection|paragraph)\*?\{([^}]*)\}", r"\n# \2\n", t)
    t = re.sub(r"\\item\s*", "\n- ", t)
    t = t.replace("\\times", "×").replace("~", " ").replace("---", "—").replace("--", "–")
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?\{([^{}]*)\}", r"\2", t)
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    t = t.replace("$", "").replace("{", "").replace("}", "")
    return t


def load_lines(path):
    raw = Path(path).read_text(encoding="utf-8")
    labels = 0
    if path.endswith(".tex"):
        labels = len(re.findall(r"\\paragraph\*?\{|^\s*\\textbf\{[^}]{1,80}\}", raw, flags=re.M))
        raw = strip_latex(raw)
    lines = []
    for ln in raw.splitlines():
        s = ln.strip()
        if s.startswith("<!--") or s.startswith("|") or s.startswith("```") or s.startswith("#"):
            lines.append("")
            continue
        if re.match(r"^\s*\*\*[^*]{2,80}\*\*", ln):
            labels += 1
        if re.match(r"^\s*([-*]|\d+\.)\s+", ln):
            lines.append("")
            ln = re.sub(r"^\s*([-*]|\d+\.)\s+", "", ln)
        lines.append(ln)
    return lines, labels


def sentences(lines):
    text = "\n".join(lines)
    out, start = [], 0
    for m in re.finditer(r"(?<=[.!?])\s+(?=[A-Z\[])|\n\s*\n", text):
        out.append((text[start:m.start()], text.count("\n", 0, start) + 1))
        start = m.end()
    out.append((text[start:], text.count("\n", 0, start) + 1))
    return [(re.sub(r"\s+", " ", s).strip(), n) for s, n in out if s.strip()]


def ngrams(s, n=6):
    w = re.findall(r"[a-z0-9]+", s.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def bank_ngrams():
    bank = set()
    if BANK.exists():
        for l in BANK.open(encoding="utf-8"):
            bank |= ngrams(json.loads(l)["quote"])
    if PARAS.exists():
        for l in PARAS.open(encoding="utf-8"):
            bank |= ngrams(json.loads(l)["text"])
    if PHRASES.exists():
        for r in csv.DictReader(PHRASES.open(encoding="utf-8")):
            bank |= ngrams(r["example"])
    for p in (ROOT / "references/exemplars/cards").glob("*.md"):
        for ln in p.read_text(encoding="utf-8").splitlines():
            if ln.startswith("> ") and not ln.startswith("> —"):
                bank |= ngrams(ln)
    return bank - {
        "in this paper we propose a", "the rest of the paper is",
        "the main contributions of this", "our main contributions are as follows",
        "we make the following contributions", "code and models are publicly available"
    }


def line_kinds(path, n_lines):
    raw = Path(path).read_text(encoding="utf-8")
    if path.endswith(".tex"):
        k = "body" if sm.file_kind(raw) == "body" else "front"
        return {i: k for i in range(1, n_lines + 2)}
    kinds, cur = {}, "front"
    for i, ln in enumerate(raw.splitlines(), 1):
        h = re.match(r"^#+\s*(?:\d+\.?\s*)?(.*)", ln)
        if h:
            title = h.group(1).lower().strip()
            if any(k in title for k in ["method", "experiment", "result", "discussion", "related", "conclusion"]):
                cur = "body"
            elif any(k in title for k in ["abstract", "introduction"]):
                cur = "front"
        kinds[i] = cur
    return kinds


def corpus_checks(path):
    stats = sm.load_stats()["style"]
    issues = []
    for sec, paras in sm.sections(path).items():
        if not paras:
            continue
        m, _ = sm.metric(paras)
        d = stats[sec]
        name = SECNAME[sec]

        def over(key, msg, level="WARN"):
            if m[key] > d[key]["p90"]:
                issues.append((level, 0, f"{name}: {msg} ({m[key]:.2f}; 90% of award papers ≤ {d[key]['p90']})", ""))

        over("numbers", "more numbers than most award papers; keep headline numbers, move the rest to experiments")
        over("connector_per_100w", "logical connectors per 100 words (therefore/thus/however/…); let sentence order carry the logic")
        over("colon_or_dash_sentences", "share of sentences with a colon; keep colons for lists, examples or the handle")
        if m["sent_len_mean"] > d["sent_len_mean"]["p75"]:
            issues.append(("NOTE", 0, f"{name}: mean sentence length {m['sent_len_mean']:.1f} words is heavier than 75% of award papers; let the pivots stand as short sentences", ""))
        over("antithesis_ratio", "share of aphoristic contrasts ('X is not Y', 'rather than'); keep one or two that carry the thesis and state the rest as plain facts")
        over("short_sent_ratio", "share of short sentences (≤ 12 words); keep 3–4 short pivots and let the rest carry a relation")
        over("participle_tail_ratio", "share of sentences ending in a participial clause (', making …', ', extending …'); merge with because/while/by/which or end the sentence")
        over("hedge_count", "hedging words (may/could/suggest/…)")
        over("booster_count", "boosters (significantly/remarkably/…)")

        if m["sent_len_mean"] < d["sent_len_mean"]["p10"]:
            issues.append(("WARN", 0, f"{name}: mean sentence length {m['sent_len_mean']:.1f} words is below 90% of award papers (p10 = {d['sent_len_mean']['p10']:.1f}); merge bare-fact sentences", ""))

        run_limit = 3 if sec == "intro" else 2
        if m["short_run_max"] >= run_limit:
            level = "WARN" if m["short_run_max"] >= 3 else "NOTE"
            issues.append((level, 0, f"{name}: {m['short_run_max']} consecutive sentences under 15 words; merge them", ""))

        if sec == "abstract" and m["self_praise_count"] == 0:
            issues.append(("NOTE", 0, "abstract makes no evaluative claim (outperforms, first, efficient, …); add one that evidence supports", ""))
        if sec == "abstract" and m["insight_formula_count"] >= 1:
            issues.append(("WARN", 0, "abstract uses a formula such as 'key insight'/'key idea'; state the insight directly", ""))
        if sec == "intro" and m["insight_formula_count"] >= 2:
            issues.append(("WARN", 0, f"introduction uses 'key insight'-type formulas {m['insight_formula_count']}×; state the observation directly", ""))
    return issues


def check(path, bank, max_words=60):
    lines, labels = load_lines(path)
    kinds = line_kinds(path, len(lines))
    issues = []
    is_body_file = all(k == "body" for k in kinds.values())
    if not is_body_file:
        issues.extend(corpus_checks(path))

    for s, n in sentences(lines):
        body = kinds.get(n, "front") == "body"
        for pat, msg in ERROR_PHRASES.items():
            if body and msg in BODY_SKIP:
                continue
            if pat == r"\blandscape\b" and VALID_LANDSCAPE.search(s):
                continue  # Exempt scientific concepts (e.g. loss landscape)
            if re.search(pat, s, flags=re.I):
                issues.append(("ERROR", n, msg, s))
        for pat, msg in WARN_PHRASES.items():
            if re.search(pat, s, flags=re.I):
                issues.append(("WARN", n, msg, s))
        for pat, msg in NOTE_PHRASES.items():
            if re.search(pat, s, flags=re.I):
                issues.append(("NOTE", n, msg, s))

        # Check for trailing participle clauses
        if TRAILING_PARTICIPLE.search(s):
            issues.append(("WARN", n, "trailing participial clause restating significance (merge with because/which or end sentence)", s))

        # Check for implementation detail in abstract/intro
        if not body and re.search(DETAIL, s, flags=re.I):
            issues.append(("WARN", n, "implementation detail in abstract/introduction", s))

        # Check sentence length
        if len(s.split()) > max_words:
            issues.append(("WARN", n, f"long sentence ({len(s.split())} words)", s))

        # Exemplar verbatim copying check
        ov = ngrams(s) & bank
        if ov:
            issues.append(("ERROR", n, f"copies exemplar wording: '{sorted(ov)[0]}'", s))

    # Check paragraph openers diversity
    paras = [p.strip() for p in "\n".join(lines).split("\n\n") if p.strip()]
    firsts = [w[0].lower() for w in (re.findall(r"[A-Za-z]+", p)[:1] for p in paras) if w]
    for w in set(firsts):
        if firsts.count(w) > 3 and w not in {"the", "a", "in"} and not is_body_file:
            issues.append(("WARN", 0, f"{firsts.count(w)} paragraphs start with '{w}'", ""))

    return issues


def triage(path):
    """Emergency 3-minute triage audit for authors facing imminent deadlines."""
    print(f"\n=======================================================")
    print(f"🚨 EMERGENCY DEADLINE TRIAGE AUDIT: {Path(path).name}")
    print(f"=======================================================")
    lines, _ = load_lines(path)
    sents = [s for s, _ in sentences(lines)]
    words_per_sent = [len(s.split()) for s in sents if s]

    # 1. Burstiness check
    if len(words_per_sent) > 3:
        mean_len = statistics.mean(words_per_sent)
        std_len = statistics.stdev(words_per_sent)
        burstiness_status = "✅ HEALTHY BURSTINESS" if std_len >= 9.0 else "⚠️ MONOTONOUS CADENCE (inject 5-10 word pivot sentences)"
        print(f"Sentence Cadence: mean={mean_len:.1f} words, std={std_len:.1f} ({burstiness_status})")
    
    # 2. Fatal tells count
    fatal_errors = []
    text = "\n".join(lines)
    for pat, desc in ERROR_PHRASES.items():
        if pat == r"\blandscape\b":
            # Check only non-exempted landscape
            matches = [m for m in re.finditer(pat, text, flags=re.I) if not VALID_LANDSCAPE.search(text[max(0, m.start()-20):m.end()+20])]
        else:
            matches = list(re.finditer(pat, text, flags=re.I))
        if matches:
            fatal_errors.append((desc, len(matches)))

    print(f"\n--- 1. Top Fatal AI Tells ({len(fatal_errors)} categories found) ---")
    if not fatal_errors:
        print("  ✅ Zero fatal AI tells detected!")
    else:
        for desc, cnt in fatal_errors[:6]:
            print(f"  ❌ [{cnt}x] {desc}")

    # 3. Dashes audit
    dashes = len(re.findall(r"—|---|(\s–\s)|(\s--\s)", text))
    print(f"\n--- 2. Hard No-Dash Rule Audit ---")
    if dashes == 0:
        print("  ✅ Clean: 0 em/en dashes found.")
    else:
        print(f"  ❌ CRITICAL: Found {dashes} dash(es)! Replace immediately with periods, colons, or parentheses.")

    # 4. Numbers check
    numbers = re.findall(NUMBER, text)
    print(f"\n--- 3. Quantitative Evidence Audit ---")
    print(f"  Numbers detected: {len(numbers)} numerical values across draft.")
    if len(numbers) < 2:
        print("  ⚠️ WARNING: Introduction has fewer than 2 numbers. Add at least 1 headline result delta!")
    else:
        print("  ✅ Evidence grounded with quantitative numbers.")

    print(f"\n--- 4. Rapid Triage Action Plan ---")
    print("  1. Search-and-replace all dashes ('—' -> '.' or ':').")
    print("  2. Purge flagged AI tells: delve, pivotal, seamless, not-X-but-Y.")
    print("  3. Insert 1-2 short punchy pivot sentences (5-10 words) at the gap and the core insight.")
    print("  4. Verify that each main contribution mirrors an ablation table row.")
    print(f"=======================================================\n")


def main():
    ap = argparse.ArgumentParser(description="Audit academic paper drafts against award-paper & humanizer standards.")
    ap.add_argument("files", nargs="+", help="Draft files (.tex, .md, .txt)")
    ap.add_argument("--max-words", type=int, default=60, help="Max sentence words warning threshold")
    ap.add_argument("--triage", action="store_true", help="Run fast emergency triage audit for urgent deadlines")
    a = ap.parse_args()

    if a.triage:
        for f in a.files:
            triage(f)
        return 0

    bank = bank_ngrams()
    total_e = total_w = total_n = 0
    for f in a.files:
        issues = check(f, bank, a.max_words)
        print(f"== {f}")
        if not issues:
            print("OK: no issues found. Clean publication-ready draft.")
        order = {"ERROR": 0, "WARN": 1, "NOTE": 2}
        for level, n, msg, s in sorted(issues, key=lambda x: (order[x[0]], x[1])):
            print(f"{level:5s} line {n:>3}: {msg}")
            if s:
                print(f"           > {s[:160]}")
        total_e += sum(1 for i in issues if i[0] == "ERROR")
        total_w += sum(1 for i in issues if i[0] == "WARN")
        total_n += sum(1 for i in issues if i[0] == "NOTE")

    print(f"\nAudit Result: {total_e} error(s), {total_w} warning(s), {total_n} note(s)")
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main())
