# StoryScope Discourse Foundations for Academic Writing

This document details the theoretical and empirical bridge between **StoryScope** (Russell et al., COLM 2026, UMD & Google DeepMind, arXiv:2604.03136v6) and publication-grade academic writing.

---

## 1. Why Surface Humanization Fails in Academic Papers

Most standard "AI humanizers" operate purely at the surface level:
- Swapping words with synonyms.
- Introducing artificial typos or perplexity jitter.
- Toggling punctuation.

StoryScope establishes that **surface-level signals retain less than 3% of the unique discriminative power**:
> *"Narrative features alone achieve 93.2% macro-F1 for human vs. AI detection... retaining over 97% of the performance of models that include stylistic cues."*

Both peer reviewers (Area Chairs, Reviewers at CVPR, ICCV, NeurIPS, ICML) and automated classifiers evaluate **underlying discourse structure, intellectual agency, and thematic construction**. A paper that swaps words but keeps an AI discourse arc will still read like an LLM draft and get rejected.

---

## 2. The 10 Discourse Dimensions Applied to Scientific Writing

StoryScope adapts NarraBench's literary theory dimensions. In `Write-Paper-Like-a-Human`, we map these directly to academic scientific papers:

| StoryScope Dimension | Fiction Definition | Scientific Academic Translation |
|---|---|---|
| **Agent / Agency** | Character motivations, roles, decisions | **Algorithmic Operators & Experimental Agency**: What technical component causes what transformation. Models do not "magically decide"; mathematical loss gradients and geometric projections enforce constraints. |
| **Plot / Progression** | Problem resolution, conflict arc | **The Scientific Evidence Chain**: Bottleneck $\to$ Root Cause $\to$ Insight $\to$ Method Formulation $\to$ Empirical Validation $\to$ Ablation. |
| **Event Escalation** | Intensity and variation of events | **Rhetorical Cadence**: Balancing dense technical definitions with short, punchy, memorable pivot sentences. Avoiding flat, monotonous paragraph weights. |
| **Temporal Structure** | Chronological order, flashbacks, anachrony | **Lineage & Recontextualization**: Placing work within historical evolution (Stage 1 $\to$ Stage 2 $\to$ Unresolved Tension), then recontextualizing the problem after presenting the core insight. |
| **Perspective / Voice** | Narrator distance, focalization | **Authorial Stance**: Confident, empirical, active first-person plural ("We observe", "We formulate", "Our analysis reveals") without defensive posturing or false humility. |
| **Setting / Scope** | Physical environment, world-building | **Problem Setting & Boundary Conditions**: Rigorously specifying the task constraints, resolution, assumptions, input modalities, and compute budgets. |
| **Thematic Weighting** | Moralizing, explicitness of themes | **Significance & Claims**: Grounded empirical deltas vs. unearned preachy claims ("pivotal", "paradigm shift"). Stating what the numbers mean without moralizing. |
| **Intertextual Richness** | References to other texts and myths | **Literature Positioning**: Explicit, respectful, and mechanistically precise citations of prior baselines—crediting their exact strengths before isolating the specific failure mode. |
| **Social / Dialectic** | Social dynamics, gossip, dialogue | **Scientific Dialectic**: The dialogue between the proposed formulation and the established consensus; ruling out obvious counter-proposals with quantitative evidence. |
| **Revelation** | Timing and depth of surprise/insight | **The Core Insight / "Aha!" Moment**: Presenting the mathematical or physical insight not as a generic assertion, but as an observation that alters how the reader views the problem. |

---

## 3. Top AI Discourse Tells in Academic Writing (StoryScope Empirical Data)

Table 14 and Table 16 in StoryScope reveal the exact behavioral traps that LLMs fall into when generating text. Here is how they manifest in academic drafts:

### Tell 1: Thematic Over-Determination & Moralizing (AI Gap: -0.65 to -0.42)
- **The AI habit**: LLMs cannot resist telling the reader how important the work is, how crucial the field is, and why everyone should care. They add empty introductory and concluding sentences declaring "profound implications for the future of AI".
- **The Human Award-Paper fix**: Zero preaching. The significance is carried by **one or two headline numbers** and an exact statement of what is now possible that failed before. Let the empirical result create the conviction.

### Tell 2: Structural Streamlining & Frictionless Problem-Solving (AI Gap: -0.28 to -0.21)
- **The AI habit**: LLMs construct a tidy, single-track narrative: "Problem exists $\to$ We propose Model $\to$ Model solves problem perfectly on all fronts." There is no friction, no trade-off, no discarded naive alternative. Reviewers immediately detect this as an ungrounded synthetic pitch.
- **The Human Award-Paper fix**: Award papers explicitly present the **tension**:
  1. The dominant baseline works well under condition $A$, but fails under realistic condition $B$.
  2. The obvious naive fix (e.g., brute-force supersampling, scaling up layers) exists, but is prohibitively expensive (quantified with FLOPs/hours).
  3. Our insight eliminates the cost by rethinking the formulation.

### Tell 3: Lack of Operational Agency (AI Gap: -0.23 to -0.42)
- **The AI habit**: The paper uses passive constructions and anthropomorphic language: *"The framework intuitively understands spatial relationships and seamlessly harmonizes representations."*
- **The Human Award-Paper fix**: Exact mathematical operators: *"Minimizing Eq. 4 constrains the conical frustum volume, bounding the reconstructable Nyquist frequency to match the sensor pixel pitch."*

### Tell 4: Discourse Space Clustering (Model Fingerprinting)
StoryScope proves that Claude, GPT, Gemini, DeepSeek, and Kimi all cluster into a narrow region of narrative space:
- **Claude fingerprint**: Notably flat event escalation (every paragraph has the exact same uniform density and sentence rhythm).
- **GPT fingerprint**: Over-reliance on formulaic transitions and staged signposting ("To achieve this, we... Furthermore, we... Finally, we...").
- **Gemini fingerprint**: Excessive external descriptive labeling without operational mechanisms.
- **Human writing**: Wide dispersion across narrative space, idiosyncratic rhetorical decisions, bursty sentence rhythm (short 6-word punchlines mixed with 30-word causal explanations), and deep causal specificity.

---

## 4. The Humanizer Synthesis Checklist

To transform an academic draft from an AI-clustered artifact into an award-caliber human scientific paper:

1. [ ] **Kill the Sermon**: Cut every sentence that explains "why this matters to the broader landscape of AI" unless backed by a specific application constraint.
2. [ ] **Name the Naive Alternative**: Show that you considered the obvious solution and explain why it fails or costs too much.
3. [ ] **Mechanistic Attribution**: Replace every adjective praising the model (*"our elegant/novel/powerful module"*) with the specific algebraic or algorithmic operation (*"our closed-form reparameterization"*).
4. [ ] **Discourse Burstiness**: Ensure paragraph openers and pivot sentences vary in length. A 5-word pivot sentence (*"This assumption fails in practice."*) followed by a 25-word mechanistic breakdown creates authentic human pacing.
5. [ ] **Honest Boundary Conditions**: State the exact assumptions and operating ranges. A paper that knows its boundaries sounds like an expert; a paper that claims universal perfection sounds like an LLM.
