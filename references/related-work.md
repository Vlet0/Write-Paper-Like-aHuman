# Related Work: The "Battle of Assumptions" Protocol

Most AI-generated Related Work sections read like a tedious chronological laundry list:
> *"In recent years, deep learning has attracted increasing attention. Pioneering works such as [1, 2] proposed X. Subsequently, [3, 4] improved Y. More recently, [5] introduced Z. Despite their impressive success, they all suffer from W."*

Top-tier award-winning papers (CVPR, ICCV, NeurIPS) never write laundry lists. They structure Related Work as a **battle of competing technical assumptions**.

---

## 1. The 3 Structural Principles of Award-Caliber Related Work

### Principle 1: Group by Core Technical Assumption (Not by Date or Author)
Organize paragraphs around the **fundamental design hypothesis** that unites a family of approaches, rather than citing papers individually.

*Weak AI Organization*:
- 2.1 Deep Learning for Novel View Synthesis
- 2.2 Neural Radiance Fields
- 2.3 3D Gaussian Splatting

*Strong Academic Architecture*:
- 2.1 Continuous Volumetric Representations (Implicit Neural Fields)
  *(Assumption: Scene geometry can be queried at arbitrary coordinate resolutions via dense ray marching.)*
- 2.2 Explicit Discrete Primitives (Point Clouds and Gaussians)
  *(Assumption: Projected screen-space splats decouple geometric density from ray-tracing overhead.)*
- 2.3 Anti-Aliasing and Multi-Scale Sampling
  *(The Tension: How both implicit and explicit models handle Nyquist band-limiting under varying view distances.)*

### Principle 2: The "Credit $\to$ Assumption Boundary" Move
Reviewers often authored the papers cited in Related Work. An abrasive or dismissive tone (*"Method A is limited and flawed"*) generates immediate hostility. A sycophantic tone (*"Pioneering and brilliant Method A..."*) sounds like AI slop.

Use the two-step **Credit $\to$ Boundary** move:
1. **Credit**: State precisely what the baseline made possible under its intended setting.
2. **Boundary**: Identify the mathematical or physical assumption required for that success, and explain why that assumption breaks in your target scenario.

*Example*:
> *"Mip-NeRF [2] elegantly resolves multiscale aliasing by replacing infinitesimal rays with conical frustums. However, its closed-form integrated positional encoding assumes an isotropic multivariate Gaussian, an assumption that degrades when rendering elongated or specular surfaces at grazing angles."*

### Principle 3: The Checkable Contrast Matrix
Every subsection in Related Work must conclude with a 1–2 sentence crisp contrast between existing paradigms and your approach, focused on **operational mechanics** (loss formulation, parameterization, runtime complexity, or required input modalities)—never on generic performance claims.

*Example*:
> *"Unlike optimization-based bundle adjustment pipelines [14, 28] that require hundreds of iterations per scene, our formulation operates in a single forward pass, predicting camera poses and dense depth concurrently without post-processing."*

---

## 2. Banned Related Work Clichés & AI Tells

| Banned AI Phrasing | Why Reviewers Hate It | Human Award-Paper Replacement |
|---|---|---|
| *"In recent years, [X] has become a hot topic / attracted extensive attention"* | Empty filler opening; says nothing about the scientific problem. | Jump straight to the task: *"Novel view synthesis requires reconstructing continuous radiance from sparse photographs."* |
| *"Pioneering works [1, 2] have laid a solid foundation..."* | Puffed sycophancy. | State the mechanism directly: *"Early coordinate-based networks [1, 2] parameterized radiance via multi-layer perceptrons."* |
| *"Extensive literature exists on this topic, which we briefly review."* | Meta-commentary about the writing process. | Delete the sentence entirely. |
| *"Despite their remarkable success, they all fail to..."* | Sweepingly unfair dismissal; alienates reviewer. | Scope the specific boundary: *"While these approaches excel on isolated objects under controlled lighting, they struggle with unbounded outdoor scenes."* |
| Citing 8 papers in a single generic bracket `[1, 2, 3, 4, 5, 6, 7, 8]` without differentiation | Indicates the author (or LLM) did not read the papers. | Differentiate: *"While [1, 3] optimize coordinate grids, [4, 6] rely on octree hierarchies to bound memory."* |

---

## 3. Related Work Checklist
- [ ] Are subsections titled by technical paradigm rather than generic terms?
- [ ] Does each cited group receive credit for its specific success before its boundary is identified?
- [ ] Are all contrasts stated at the level of mechanics and assumptions, not mere scores?
- [ ] Is there zero generic filler (*"has attracted much attention"*, *"pioneering works"*")?
- [ ] Are citations differentiated rather than dumped in massive uniform brackets?
