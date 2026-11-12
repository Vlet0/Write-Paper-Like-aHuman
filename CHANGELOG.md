# Changelog

All notable changes to `Write-Paper-Like-a-Human` will be documented in this file.

## 1.0.2 (2026-11-12)

### Voice Diversification, False-Positive Protections & Emergency Triage Mode
- **Anti-Meta-Clustering Architecture**: Added `references/diversity-and-voice.md` formulating 4 distinct rhetorical stances (*Empirical Conflict*, *Theoretical Paradox*, *Systems Pragmatism*, *Historical Linchpin*) and 3 authorial personas to prevent the "100 papers like one" template trap.
- **Emergency Deadline Triage Mode (`--triage`)**: Upgraded `scripts/check_draft.py` with the `--triage` flag, delivering an instant 3-minute diagnostic audit for authors facing imminent conference deadlines (<24–48 hours).
- **Context-Aware False Positive Immunity**: Enhanced `check_draft.py` regex engines to recognize legitimate scientific and physical terminology (exempting *loss landscape*, *optimization landscape*, *energy landscape*, and allowing mathematical theorem proofs to use *prove*).
- **Related Work & Rebuttal Protocols**:
  * Added `references/related-work.md`: The "Battle of Assumptions" protocol for structuring prior work without chronological laundry lists.
  * Added `references/rebuttal.md`: The "Direct Defense & Evidence-First" protocol for peer review response letters.
- **Sleek 2-Row SVG Vector Visualizations**: Replaced fragile Mermaid rendering with custom vector SVG pipeline graphics (`assets/pipeline.svg` and `assets/pipeline_vi.svg`).

## 1.0.0 (2026-11-12)

### Initial Unified Release
- **Unified Methodology**: Synthesized Best-Paper Writing architecture (60 CVPR/ICCV/NeurIPS award papers) with Humanizer (26 anti-AI tell patterns) and StoryScope (COLM 2026 empirical discourse analysis).
- **The 8-Stage Scientific Pipeline**: End-to-end framework covering Intake, Scientific Positioning, Routing, Claim Calibration, Narrative Architecture, Exemplar-Guided Drafting, De-AI Scrubbing, and Verification.
- **Deep Discourse De-AI Rules**: Enforced elimination of thematic over-determination (moralizing/preaching), structural streamlining (frictionless progress), and passive anthropomorphic agency.
- **Auditing Suite**: Upgraded `check_draft.py` to mechanically audit against corpus statistics, all 26 Humanizer patterns, and StoryScope discourse anomalies.
- **Figure Planning & Vector Assets**: Included TikZ overview schematics, teaser strip templates, and publication-ready matplotlib styling.
- **LaTeX Author Kit**: CVPR 2027 IEEE-format full paper template.
