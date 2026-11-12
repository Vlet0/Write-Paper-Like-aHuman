<div align="center">

# 🖋️ Write-Paper-Like-a-Human
### High-Impact Best-Paper Architecture & Rigorous Scientific De-AI Humanization

**Persuade reviewers by combining award-winning academic narrative structure with authentic human voice and discourse discipline**

[![License: MIT & CC BY 4.0](https://img.shields.io/badge/License-MIT%20%2F%20CC%20BY%204.0-blue.svg)](LICENSE)
[![Corpus: 60 Award Papers](https://img.shields.io/badge/Corpus-60%20Award%20Papers-orange.svg)](PAPER_LIST.md)
[![StoryScope COLM 2026](https://img.shields.io/badge/Grounding-StoryScope%20COLM%202026-purple.svg)](references/storyscope-discourse.md)
[![Humanizer Patterns](https://img.shields.io/badge/De--AI%20Patterns-26%20Tells-green.svg)](references/humanizer-patterns.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Plugin-8A63D2.svg)](.claude-plugin/plugin.json)
[![Cursor](https://img.shields.io/badge/Cursor-Plugin-000000.svg)](.cursor-plugin/plugin.json)

[🇻🇳 Tiếng Việt (README.md)](README.md) · [60 Award Paper Corpus](PAPER_LIST.md) · [Changelog](CHANGELOG.md) · [Notice & Citations](NOTICE.md)

</div>

---

## 🎯 Motivation & Core Philosophy

When researchers prompt large language models to draft scientific papers, the resulting manuscripts frequently face **immediate desk rejection or severe reviewer skepticism**.

### Why Surface "Humanizers" Fail
The foundational paper **StoryScope: Investigating idiosyncrasies in AI fiction** (Russell et al., COLM 2026, UMD & Google DeepMind, arXiv:2604.03136v6) revealed that:
> *"Surface-level lexical/syntactic signals account for less than 3% of discriminative power. Over 97% of detection signals stem from **Discourse-Level Narrative Architecture**."*

AI models (Claude, GPT, Gemini, DeepSeek, Kimi) consistently exhibit telltale discourse anomalies:
1. **Thematic Over-determination & Moralizing**: Preaching paper importance and sermonizing about broad impacts ("paving the way for the future of AI") rather than letting empirical deltas carry conviction.
2. **Structural Streamlining**: Creating a frictionless, single-track problem-solving narrative that conceals technical trade-offs, scope constraints, and the failure modes of naive alternatives.
3. **Lack of Operational Agency**: Attributing outcomes to passive system illusions ("the model understands the geometry") rather than exact mathematical operators, loss gradients, and architectural invariants.
4. **Metronomic Monotony**: Uniform sentence lengths (18–24 words), overused transition formulas (*However, Moreover, Furthermore*), forced triads, and ubiquitous em-dash splices (`—`).

### The Unified Synthesis
`Write-Paper-Like-a-Human` bridges three rigorous foundations into one coherent system:
- 🏛️ **Best-Paper Architecture**: Distilled from sentence-by-sentence analysis of **60 CVPR, ICCV, and NeurIPS award papers (2021–2025)**. Provides sharp motivation, 8 paper archetypes (L1–L8), strict claim-to-evidence calibration, and vector figure planning (Figure 1 typology, TikZ).
- 🧹 **26 Anti-AI Tell Patterns**: Derived from WikiProject AI Cleanup and `humanizer` (v4.0.0), eradicating *Not X but Y* staging, dramatic slogan closers, universal dashes, and AI vocabulary (`delve`, `pivotal`, `seamless`, `landscape`, `tapestry`, `bolstered`).
- 🔬 **StoryScope Discourse Discipline (COLM 2026)**: Restores authentic scientific agency, operational causal attribution, technical friction, and dynamic sentence burstiness ($\sigma_{\text{length}} \ge 9.5$).

---

## ⚡ The 8-Step Scientific Pipeline

Do not write ungrounded prose before Step 4.

```mermaid
flowchart TD
    Step0["Step 0: Research Intake (Intake Brief / Reverse-Engineering)"] --> Step1["Step 1: Scientific Positioning (Claim, Tension, Insight, Handle, Numbers)"]
    Step1 --> Step2["Step 2: Paper Routing (L1–L8 Paper Types & Motivation Modes)"]
    Step2 --> Step3["Step 3: Claim Calibration & Evidence Mapping (Evidence-to-Claim Hierarchy)"]
    Step3 --> Step4["Step 4: Discourse Architecture & Skeleton (Anti-Thematic Preaching & Pivots)"]
    Step4 --> Step5["Step 5: Drafting with Exemplars (60 Award Paper Corpus)"]
    Step5 --> Step5b["Step 5b: Method (Need → Mechanism → Property) & Experiments Execution"]
    Step5b --> Step5c["Step 5c: Strategic Figure Planning & Vector Production (TikZ / matplotlib)"]
    Step5c --> Step6["Step 6: The Full-Spectrum 26-Pattern De-AI Scrub (Humanizer Pass)"]
    Step6 --> Step7["Step 7: Automated Mechanical Verification (check_draft.py, check_figures.py)"]
    Step7 --> Step8["Step 8: Final Delivery (Publication LaTeX Template + Strategic report.md)"]
```

### Step 0 — Research Intake & Briefing
- **Mode A: Structured Intake Form.** Complete the local offline HTML form `assets/intake_form.html` (exports `bestpaper-intake/v1` JSON), then run:
  ```bash
  python scripts/intake_to_brief.py intake.json --out brief.md --bib refs.bib
  ```
- **Mode B: Reverse-Engineering Existing Drafts / De-AI Scrubbing.** Reverse-engineer an existing draft into the intake schema, audit against the 26 Humanizer patterns, and output a structured change table: `[Original] → [Humanized Scientific] → [Pattern Applied & Technical Rationale]`.
- **Invariant**: Never fabricate numbers, baselines, or citations. Mark missing items as `[TODO: ...]` or `\TODO{}`.

### Step 1 — Scientific Positioning & Core Thesis
Formulate six strategic anchors (saved in `report.md`, not paper text):
1. **Core Claim**: `We show that [method] [achieves what] [under which setting], because [exact technical cause].`
2. **Tension Type**: Choose from `references/routing.md` (*tradeoff*, *capability-missing*, *obvious-fix-too-costly*, *unexplained-phenomenon*, *open-question*, *belief-overturned*).
3. **Core Insight**: The underlying physical, geometric, or mathematical observation stated as a direct fact (e.g., *"sampling rates bound reconstructable frequencies"*).
4. **Conceptual Handle**: A short name for the idea (e.g., *"integrated positional encoding"*, *"next-scale prediction"*).
5. **Closest Baseline & Checkable Difference**: Name the closest work and state the exact operational distinction (in loss, parametrization, or assumption).
6. **Headline Numbers**: The 1–2 key metrics carrying the central claim.

### Step 2 — Paper Routing
Match the research against the 8 paper archetypes in `references/routing.md`:
- **L1**: Method improvement (43% of award papers)
- **L2**: New capability / new task (e.g., DreamBooth, VGGT)
- **L3**: Dataset / benchmark
- **L4**: Measurement / large-scale empirical study
- **L5**: Mechanism analysis
- **L6**: Theoretical foundation (e.g., DPO)
- **L7**: Empirical / scaling law
- **L8**: Re-examination / constructive critique

### Step 3 — Claim Calibration & Evidence Mapping
Load `references/claim-calibration.md`.
- Map: **Claim $\to$ Method Component $\to$ Experiment Table/Figure $\to$ Ablation**.
- State claims at the strongest supported level: confident where backed by data, scoped where bounded.
- **Anti-Defensive Rule**: Zero defensive disclaimers (*"remains to be explored"*, *"does not establish"*, *"one limitation is"*) in Abstract or Introduction. Real limitations belong exclusively in the **Limitations** section.

### Step 4 — Discourse Architecture & Skeleton
Build a 5-paragraph Introduction skeleton (`references/introduction.md`, `references/storyscope-discourse.md`):
1. **Paragraph 1 (Context & Credit)**: Credit specific prior work; define what works well in standard settings.
2. **Paragraph 2 (Gap & Root Cause)**: Name the exact observable failure condition and its underlying mechanism. Rule out the naive fix with quantified costs (FLOPs/hours).
3. **Paragraph 3 (Insight & Formulation)**: State the problem observation; present the method as its natural consequence.
4. **Paragraph 4 (Mechanistic Contrast)**: Contrast mechanisms against the closest baseline.
5. **Paragraph 5 (Empirical Evidence & Scope)**: Present headline results with exact numbers and boundary conditions.
6. **Pivot Sentences**: Place short, punchy sentences (5–10 words) at transition points.

### Step 5 — Drafting with Exemplars
Retrieve matching moves from `references/exemplars/`:
```bash
python scripts/find_exemplars.py --para contrast --type L1
python scripts/find_exemplars.py intro.insight -n 3
```
- Emulate the structural flow and information ordering; never copy $\ge 6$ consecutive words (`check_draft.py` enforces this).
- Use active first-person plural (*"We formulate"*, *"We observe"*).

### Step 5b — Method & Experiments Execution
- **Method** (`references/method.md`): Describe each component through **Need $\to$ Mechanism $\to$ Property**.
- **Experiments** (`references/experiments.md`): Claim-first organization. Ablation tables mirror method claims one-to-one.

### Step 5c — Strategic Figure Planning & Vector Graphics
Load `references/figures.md`.
- **Figure 1**: Select by route archetype (`contrast-schematic`, `diagnosis`, `teaser-strip`). Placed full-width on Page 1 or 2.
- **Draw Mechanisms**: Generate vector TikZ schematics (`assets/figures/overview_tikz.tex`) and publication-grade matplotlib plots (`assets/figures/plot_style.py`, `bestpaper.mplstyle`).
- **Placeholder Discipline**: Do not fabricate results. Use framed placeholder blocks with caption plans (`\FigPlan{...}`).

### Step 6 — Full-Spectrum De-AI Scrubbing Pass
Audit text against all 26 Humanizer patterns (`references/humanizer-patterns.md`):
- Strip out *Not X but Y*, one-line slogan closers, and staged run-ups.
- **Hard No-Dash Rule**: Eradicate all em dashes (`—`) and spaced en dashes (` – `). Replace with periods, colons, or parentheses.
- Purge AI vocabulary: *delve, pivotal, seamless, landscape, tapestry, bolstered, testament, revolutionize, intricate*.
- Eliminate moralizing sermons (StoryScope).

### Step 7 — Automated Mechanical Verification
Run the verification test suite:
```bash
# Check prose for AI tells, banned phrases, and statistical bounds
python scripts/check_draft.py template/CVPR2027/sec/0_abstract.tex template/CVPR2027/sec/1_intro.tex

# Check LaTeX figure placements, captions, and vector formats
python scripts/check_figures.py template/CVPR2027/main.tex

# Measure style metrics against the 55 award-paper distribution
python scripts/style_metrics.py template/CVPR2027/sec/0_abstract.tex
```
- Resolve all `ERROR`s; justify any `WARN`.

### Step 8 — Final Delivery
Deliver:
1. Complete LaTeX project (`template/CVPR2027/`) compiling cleanly to PDF.
2. Companion **Author Strategic Report** (`report.md`) detailing the claim map, insight, handle, figure plan, and limitations notes.

---

## 🚫 The 8 Hard Rules

| # | Rule | Requirement & Solution |
|---|---|---|
| **1** | **Zero Fabrication** | Never invent numbers, baselines, or citations. Mark missing items with `\TODO{}`. |
| **2** | **No Dashes** | Strictly forbid em dashes (`—`) and spaced en dashes. Use periods, colons, or parentheses. |
| **3** | **No Intro Disclaimers** | Keep self-undermining disclaimers out of Abstract/Intro. Place in Limitations. |
| **4** | **No Trailing Participles** | Ban empty trailing participial clauses (*", making real-time rendering possible"*). State measured deltas. |
| **5** | **Mechanistic Attribution** | Attribute actions to mathematical operators and loss gradients, not anthropomorphic models. |
| **6** | **Sentence Burstiness** | Alternate short pivot sentences (5–10 words) with compound causal explanations (22–32 words). |
| **7** | **Citation Hygiene** | Cite only keys present in the user's bibliography. |
| **8** | **Anti-Preachiness (StoryScope)** | Never conclude with moralizing sermons about the future of humanity. Conclude on concrete technical capability. |

---

## 🛠️ Installation & Usage

### 1. Claude Code
Install directly as a plugin:
```bash
claude plugin marketplace add Vlet0/write-paper-like-a-human
claude plugin install write-paper-like-a-human@write-paper-like-a-human
```
Invoke in your session:
```text
/write-paper-like-a-human "Draft this paper from brief.md following CVPR Best Paper guidelines"
```

### 2. Cursor IDE
The repository includes `.cursor-plugin/plugin.json`. Open the workspace in Cursor or reference the skill prompt in your `.cursorrules`.

### 3. Codex & OpenAI CLI
Install via npm/npx:
```bash
npx skills add Vlet0/Write-Paper-Like-aHuman --global --agent codex
```

### 4. Direct CLI Usage
```bash
# Convert intake JSON to drafting brief
python scripts/intake_to_brief.py my_intake.json --out brief.md --bib refs.bib

# Query real award-paper exemplars
python scripts/find_exemplars.py --para insight --type L1
python scripts/find_exemplars.py intro.gap -n 3

# Audit draft for AI tells and statistical bounds
python scripts/check_draft.py draft_intro.tex

# Validate package integrity
python scripts/validate-package.py
```

---

## 📜 License & Citation

This project is released under a clear dual-licensing model:
- 💻 **Software, Scripts, and Templates (`scripts/`, `template/`)**: Licensed under the **[MIT License](LICENSE)**.
- 📖 **Documentation, Prompts, and Reference Guides (`references/`, `SKILL.md`)**: Licensed under the **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)**.
- 💡 **Acknowledgments**: See [`NOTICE.md`](NOTICE.md) for detailed attribution to `Best-Paper-Writing-Skill`, `humanizer`, and `StoryScope` (COLM 2026).

---

<div align="center">
<b>Dedicated to scientific integrity, rigorous clarity, and authentic human scholarship.</b><br>
If you find this project valuable, please star ⭐️ our repository on <a href="https://github.com/Vlet0/Write-Paper-Like-aHuman.git">GitHub</a>!
</div>
