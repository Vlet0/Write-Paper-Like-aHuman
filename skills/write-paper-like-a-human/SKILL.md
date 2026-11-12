---
name: write-paper-like-a-human
description: |
  Draft, rewrite, and audit high-impact academic papers combining best-paper narrative architecture with rigorous de-AI humanization.
  Use when writing, revising, or de-AI-ing research papers (Abstract, Introduction, Method, Experiments, Figures) to achieve the clarity, intellectual agency, and empirical calibration of CVPR/ICCV/NeurIPS award papers while systematically eliminating AI writing tells, generic boilerplate, and narrative clustering.
license: MIT
metadata:
  version: "1.0.0"
---

# Write-Paper-Like-a-Human: Best-Paper Architecture & Scientific Humanization

Persuade peer reviewers and academic readers by combining the narrative architecture of **60 CVPR / ICCV / NeurIPS award-winning papers** with the **26 anti-AI tell patterns** (WikiProject AI Cleanup) and empirical discourse-level findings from **StoryScope** (COLM 2026, UMD & Google DeepMind).

Standard AI drafts fail peer review not merely because of superficial vocabulary, but because of **discourse-level narrative clustering**:
1. **Thematic Over-determination**: Preaching paper importance and sermonizing about broad impacts instead of presenting concrete empirical deltas.
2. **Structural Streamlining**: Fabricating a frictionless, single-track problem-solving narrative that obscures technical trade-offs, constraints, and failures of naive alternatives.
3. **Lack of Operational Agency**: Attributing outcomes to passive system illusions rather than exact mathematical operators, loss gradients, or geometric constraints.
4. **Metronomic Monotony**: Uniform sentence lengths, repetitive connectors (*However, Moreover, Furthermore*), forced triads, and ubiquitous em-dash splices (`—`).

This skill enforces a disciplined, end-to-end scientific writing and humanization pipeline.

---

## The 8-Step Scientific Pipeline

Do not write ungrounded prose before Step 4.

### Step 0 — Research Intake (Three Input Modes)
- **Mode A: Structured Intake Form.** If the user supplies an intake JSON (from `assets/intake_form.html`, schema `bestpaper-intake/v1`), run:
  `python3 scripts/intake_to_brief.py <file.json> --out brief.md --bib refs.bib`
  Work directly from `brief.md`. If required fields are missing, ask once in a compact list.
- **Mode B: Reverse-Engineering Existing Draft / AI Humanization.** If the user pastes an existing draft abstract, introduction, or full paper:
  1. Audit the draft against `references/intake-form.md`: identify the task, dominant prior approach, observable failure condition, technical root cause, key insight, and headline numbers.
  2. Perform the **Humanizer 26-Pattern Audit** (Section C below) to mark all surviving AI tells, inflated significance, forced triads, and em-dashes.
  3. Generate a structured **Change Table**: `[Original Sentence] → [Humanized Scientific Sentence] → [Pattern Followed & Technical Rationale]`.
- **Mode C: Free-Form Discussion.** Map user descriptions onto `references/intake-form.md`.
- **Hard Rule**: Never fabricate results, numbers, baselines, datasets, or citations. Missing technical values must remain explicit placeholders: `[TODO: value]` or `\TODO{}`.

### Step 1 — Scientific Positioning & Core Thesis
Formulate the foundational anchor points for yourself (documented in `report.md`):
- **Core Claim**: `We show that [method/formulation] [achieves what] [under which conditions], because [exact technical cause].`
- **Tension Type**: Choose from `references/routing.md`: *tradeoff*, *capability-missing*, *obvious-fix-too-costly*, *unexplained-phenomenon*, *open-question*, or *belief-overturned*.
- **The Core Insight**: The physical, geometric, or mathematical observation about the problem from which the method naturally follows. State it as a direct fact (e.g., *"sampling rates bound reconstructable frequencies"*), not as a meta-announcement (*"Our key insight is that..."*).
- **The Conceptual Handle**: A short, memorable naming handle for the concept (e.g., *"integrated positional encoding"*, *"next-scale prediction"*).
- **Closest Prior Work & Checkable Delta**: Name 1–2 dominant prior methods and state the exact operational difference (in loss formulation, parameterization, runtime, or assumption).
- **Headline Numbers**: The 1–2 quantitative results that carry the central claim.

### Step 2 — Paper Routing
Load `references/routing.md`. Identify the paper archetype (L1 Method improvement, L2 New capability, L3 Dataset, L4 Measurement, L5 Mechanism, L6 Theory, L7 Empirical law, L8 Re-examination). Align the abstract arc and introduction move structure to the matched archetype.

### Step 3 — Claim Calibration & Evidence Mapping
Load `references/claim-calibration.md`.
- Establish the **evidence-to-claim hierarchy**: every claim in the Abstract and Introduction must be directly supported by a concrete table row, ablation experiment, or mathematical proof.
- Express claims at the strongest supported level: confident where evidence is solid, scoped where bounded.
- **Anti-Defensive Rule**: Zero defensive disclaimers (*"remains to be explored"*, *"does not establish"*, *"one limitation is"*) in the Abstract or Introduction. Document real failure modes and boundary conditions exclusively in the **Limitations** section.

### Step 4 — Narrative Architecture & Discourse Skeleton
Load `references/introduction.md`, `references/abstract.md`, and `references/storyscope-discourse.md`.
Build a paragraph-by-paragraph skeleton where each paragraph has **one specific scientific function**:
1. **Paragraph 1: Task & Contextual Hook.** Credit specific prior breakthroughs; establish what works well under standard conditions.
2. **Paragraph 2: Concrete Gap & Technical Root Cause.** Name the exact failure condition (observable symptom) and its underlying mechanistic cause. Rule out the naive obvious fix with a quantified cost (FLOPs, latency, memory).
3. **Paragraph 3: Core Insight & Method Formulation.** State the observation about the problem. Introduce the proposed formulation as the direct operational consequence of this insight.
4. **Paragraph 4: Mechanistic Contrast with Closest Work.** Contrast mechanisms (not mere scores) against the closest baseline.
5. **Paragraph 5: Empirical Evidence & Scope.** Present headline quantitative results on standard benchmarks with exact numbers. State the operating scope.
6. **Pivot Sentences**: Place short, punchy sentences (5–10 words) at the transition fulcrums.

### Step 5 — Drafting with Exemplar Guidance
For each section, retrieve matching award-paper moves:
`python3 scripts/find_exemplars.py --para <function> --type <L*>`
- Adopt the structural cadence and information density of award-winning papers (`references/exemplars/`).
- **Plagiarism Guard**: Never copy verbatim strings of $\ge 6$ words (`check_draft.py` mechanically enforces this).
- Write in active first-person plural (*"We formulate"*, *"We observe"*, *"Our analysis indicates"*). Never refer to user input as *"the supplied data"* or *"the provided table"*.

### Step 5b — Method and Experiments Execution
- **Method** (`references/method.md`): Structure each component under the **Need $\to$ Mechanism $\to$ Property** triad:
  1. *Need*: What failure of the preceding component makes this module necessary.
  2. *Mechanism*: The exact mathematical formulation, tensor transformation, or geometric operator.
  3. *Property*: The provable or invariant property guaranteed by this formulation.
- **Experiments** (`references/experiments.md`): Claim-first organization. Every subsection heading and table caption leads with the empirical finding. Ablation tables must mirror the component claims one-to-one.

### Step 5c — Strategic Figure Planning & Production
Load `references/figures.md`.
- Construct a **Figure Plan**: one figure per main claim; every figure carries a self-contained takeaway caption opening with a bold conclusion.
- **Figure 1 Archetype**: Select according to route (`contrast-schematic`, `diagnosis`, `teaser-strip`, `showcase`). Must be placed on Page 1 or 2.
- **Draw Mechanisms Now**: Generate vector TikZ schematics (`assets/figures/overview_tikz.tex`, `figures_preamble.tex`) and publication-grade matplotlib plots (`bestpaper.mplstyle`, `plot_style.py`).
- **Placeholder Discipline**: Do not fabricate qualitative results or curve data. Use framed placeholder blocks (`\FigPlan{...}`) with explicit data requirements.

### Step 6 — The Full-Spectrum De-AI Humanizer Scrub
Audit the text against all **26 Anti-AI Tell Patterns** (`references/humanizer-patterns.md`):
- **Staging tells**: Eliminate *Not X but Y*, one-line slogan closers, deep-sounding metaphors, and staged run-ups.
- **Rhythm tells**: Break up forced triads; vary sentence lengths to achieve burstiness ($\sigma_{\text{length}} \ge 9.5$); eliminate trailing participial clauses (*", making X possible"*).
- **Inflation tells**: Strip out stock AI vocabulary (`delve`, `pivotal`, `seamless`, `landscape`, `tapestry`, `bolstered`, `testament`, `game-changer`).
- **Hard No-Dash Rule**: Eradicate all em dashes (`—`) and spaced en dashes (` – `). Replace with periods, colons, or parentheses.
- **StoryScope Discourse Audit**: Eradicate unearned preachiness, anthropomorphic model illusions, and frictionless single-track narrative traps.

### Step 7 — Automated Mechanical Verification
Run the verification test suite:
1. `python3 scripts/check_draft.py <files>`: Fix every `ERROR`. Review and justify any `WARN`. Compare style metrics with corpus percentiles via `python3 scripts/style_metrics.py <files>`.
2. `python3 scripts/check_figures.py main.tex`: Audit float count, label references, caption lengths, and vector graphic compliance.
3. Verify that the draft compiles cleanly in the LaTeX template (`template/CVPR2027/`).

### Step 8 — Final Delivery
Deliver:
1. The publication-grade LaTeX files (`.tex`, `.bib`, `.sty`) or clean Markdown.
2. The companion **Author Strategic Report** (`report.md`) containing:
   - Claim, tension type, core insight, handle, and closest baseline delta.
   - The evidence-to-claim map and figure plan.
   - Notes for the **Limitations** section (weaknesses intentionally excluded from Abstract/Intro).
   - Change table and `check_draft.py` audit log.

---

## The 8 Hard Rules (Zero-Tolerance Invariants)

1. **Zero Fabrication**: Never invent numbers, baselines, benchmarks, citations, or qualitative results. Missing data must be explicitly marked as `[TODO: ...]` or `\TODO{}`.
2. **The Hard No-Dash Rule**: No em dashes (`—`, `---`) or spaced en dashes (` – `) in paper prose. Use periods to split sentences, colons to introduce definitions, or parentheses for clarifications.
3. **No Abstract/Intro Disclaimers**: Self-undermining sentences, unmeasured failure modes, and protocol apologies belong exclusively in the Limitations section.
4. **No Trailing Participial Inflation**: Avoid ending sentences with empty participial significance claims (*", thereby demonstrating its superior efficacy"*). State the measured delta directly.
5. **Mechanistic Attribution**: Attribute actions to mathematical operators, loss gradients, or geometric formulations—never to anthropomorphic model consciousness.
6. **Sentence Burstiness & Cadence**: Never allow metronomic sentence lengths. Alternate short 5–10 word pivot statements with 20–30 word compound causal explanations.
7. **Strict Citation Grounding**: Never cite a BibTeX key not present in the user's bibliography. Mark missing references with `[TODO: cite ...]`.
8. **Anti-Preachiness (StoryScope Invariant)**: Never end with an unearned moralizing sermon about the global future of AI. Conclude on the concrete technical capability enabled by the work.

---

## File Reference Map

| Component | Path | Purpose |
|---|---|---|
| **Intake & Briefing** | `references/intake-form.md`, `scripts/intake_to_brief.py`, `assets/intake_form.html` | Extracting structured research briefs |
| **Paper Routing** | `references/routing.md` | Selecting L1–L8 paper types and tension modes |
| **Claim Calibration** | `references/claim-calibration.md` | Aligning claims to evidence tiers |
| **Section Architecture** | `references/introduction.md`, `references/abstract.md`, `references/method.md`, `references/experiments.md` | Paragraph-level moves and section logic |
| **Figure Planning** | `references/figures.md`, `assets/figures/` | Visual argumentation, TikZ templates, plot styles |
| **De-AI Humanization** | `references/humanizer-patterns.md` | 26 anti-AI tell patterns with academic examples |
| **Discourse Theory** | `references/storyscope-discourse.md` | COLM 2026 empirical findings on AI vs human writing |
| **Style & Corpus Metrics** | `references/style-rules.md`, `references/corpus/corpus_stats.json` | Style thresholds and quantitative corpus bands |
| **Exemplars Bank** | `references/exemplars/` (`moves.jsonl`, `paragraphs.jsonl`, `phrasebank.csv`, `cards/`) | Sentence and paragraph models from 60 award papers |
| **Verification Suite** | `scripts/check_draft.py`, `scripts/check_figures.py`, `scripts/style_metrics.py`, `scripts/validate-package.py` | Automated pre-submission mechanical auditing |
| **Author Kit Template** | `template/CVPR2027/` | Submission-ready CVPR/IEEE LaTeX author kit |
