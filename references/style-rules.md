# Unified Style Rules: Best-Paper Architecture & Humanizer Discipline

Derived from the empirical sentence-by-sentence annotation of **55 award papers** (CVPR, ICCV, NeurIPS 2021–2025), the **26 anti-AI tell patterns** (WikiProject AI Cleanup / Humanizer), and the **StoryScope** discourse-level findings (Russell et al., COLM 2026).

`scripts/check_draft.py` enforces the mechanical subset of these rules.

---

## 1. Word Choice & Vocabulary Discipline

### 1.1 Use Freely (Authoritative Scientific Precision)
`present`, `introduce`, `propose`, `show`, `find`, `observe`, `indicate`, `suggest`, `rely on`, `assume`, `be limited to`, `struggle to`, `in contrast`, `whereas`, `rather than`, `specifically`, `in particular`, `to this end`, `note that`, `intuitively`, `at the cost of`, `without requiring`, `allows us to`, `enables`, `bounds`, `reparameterizes`, `halves`.

### 1.2 Use Only with a Concrete Follow-up in the Same Sentence
| Word | Mandatory Condition |
|---|---|
| **novel / new** | Prefer stating *what* is new; never write "novel and effective" or "simple yet novel". |
| **efficient / fast** | Give the quantified runtime, FLOPs, or memory footprint in the same sentence. |
| **robust / general / scalable** | Explicitly state the tested range or distribution shift. |
| **significantly** | Use only when citing a formal statistical hypothesis test; otherwise give the exact numerical $\Delta$. |
| **state-of-the-art / SOTA** | Name the specific benchmark and the baselines outperformed in the same clause. |
| **notably / remarkably** | Must be followed by a concrete number or contrast; limit to at most once per paper. |
| **the first** | Strictly scope the claim; prefer describing the technical difference over asserting temporal priority. |
| **plays a ... role** | Follow immediately with the physical or algorithmic mechanism ("as it determines..."). |

### 1.3 Strictly Prohibited (Boilerplate, LLM Slop & StoryScope Discourse Tells)
- **Generic Openers**:
  * `has attracted (increasing|growing|much) attention`
  * `in recent years, ... has become a hot topic / active area of research`
  * `plays an important/vital/crucial role in` (without immediate mechanism)
- **Inflated Self-Praise & Unearned Superlatives**:
  * `extensive experiments demonstrate the effectiveness/superiority`
  * `superiority`, `groundbreaking`, `pioneering`, `unprecedented`, `transformative`
  * `simple yet effective`, `paradigm shift`, `unlocks the full potential of`
  * `stands as a testament`, `a pivotal moment`, `enduring legacy`
- **Stock AI Tells & Clichés**:
  * `delve`, `delving`, `delve into`
  * `pivotal`, `crucial` (more than once per section)
  * `seamless`, `seamlessly`, `harmonize`, `intricate`, `intricacies`
  * `a myriad of`, `landscape` (metaphorical), `tapestry`, `realm`, `in the realm of`
  * `it is worth noting that`, `it can be seen that`, `it is crucial to understand`
  * `actually`, `bolstered`, `garner`, `showcase`, `underscore` (as generic verb)
  * `comprehensive experiments`, `meticulously crafted`
- **Thematic Over-determination & Preaching (StoryScope Tell)**:
  * Ending an abstract or introduction with an unearned moralizing sermon about "paving the way for safe, ethical, and universally accessible artificial intelligence".
  * Preaching why the task matters instead of demonstrating why prior methods fail.

### 1.4 Prohibited in Abstract & Introduction (Workflow Traces & Premature Disclaimers)
- **Workflow Traces**: Words describing the drafting process or the user's input: *supplied*, *provided results*, *the reported evaluation*, *according to the input*.
- **Draft Apparatus**: Move tags left in text (`[intro.insight]`, `[TODO]`, `History → gap`).
- **Table Citations as Subject**: Never write *"Table 1 shows that our model outperforms X"*. Write the claim and cite the table parenthetically: *"Our model outperforms X by 1.8 dB (Tab. 1)"*.
- **Premature Defensive Disclaimers**: Phrases like *does not establish*, *does not imply*, *remains to be evaluated*, *we leave ... for future work*, *one limitation is* belong strictly in the **Limitations** section, not the Abstract or Introduction.
- **Downgrading the Core Idea**: Do not weaken the central insight with *our hypothesis is*, *we take the view*, *we conjecture*. State the observation as a direct physical or geometric fact.

---

## 2. Quantitative Corpus Statistics (55 Award Papers)

Every draft evaluated by `scripts/check_draft.py` is compared against the empirical distribution of 55 best papers from CVPR, ICCV, and NeurIPS (2021–2025):

| Metric | Abstract Median (p90) | Introduction Median (p90) | Enforcement |
|---|---|---|---|
| **Numbers** | 1 (5.6) | 4 (14.6) | WARN if Introduction has 0 numbers |
| **Logical Connectors** per 100 words (*however, therefore, thus, moreover, yet, whereas, in contrast, instead, specifically*) | 0.6 (1.6) | 0.9 (1.4) | WARN if > 2.0 (AI drafts frequently hit 3.5+) |
| **Sentences with Colons** | 5% (15%) | 8% (18%) | Use colons for technical expansions |
| **Sentences with Em/En Dashes (—, –)** | **0% (0%)** | **0% (0%)** | **ERROR** in this skill (Hard Rule: No Dashes) |
| **Trailing Participial Clauses** (*", making X possible"*) | 8% (20%) | 8% (18%) | WARN if > 20% (AI drafts frequently hit 35%+) |
| **Hedges** (*may, might, could, likely, suggest*) | 0 (1) | 1 (3.6) | WARN if > p90 |
| **Boosters** (*significantly, remarkably, notably*) | 0 (1) | 1 (3.0) | WARN if > p90 |
| **Evaluative Words** (*outperforms, efficient, novel*) | 1 (3.0) | 3 (7.6) | NOTE if 0 (award papers do promote their wins) |
| **"Key Insight"-type formulaic labels** | 0 | 0 (only 4 of 55 papers use the literal phrase) | WARN if used as an explicit bold subhead |
| **Sentence Length (Words)** | 24 words | 23 words | WARN if sentence > 60 words |
| **Sentence Length Burstiness** ($\sigma_{\text{length}}$) | $\ge 9.5$ | $\ge 9.8$ | Healthy mix of 6-word pivots and 28-word explanations |

---

## 3. Structural & Rhetorical Rules

### 3.1 The Hard No-Dash Rule
Award papers communicate relationships through precise grammatical syntax rather than em dashes (`—`) or spaced en dashes (` – `).
- **Rewrite Rule**: Replace every dash with:
  1. A period, splitting a rambling thought into two crisp sentences.
  2. A colon, when the second half directly defines or enumerates the first.
  3. Parentheses, for secondary technical clarifications.
  4. Commas, for appositives.
- Hyphenated technical compounds (*scale-invariant*, *3D-aware*, *cross-entropy*) and numerical ranges (*2–3x*) are fully preserved.

### 3.2 Dynamic Sentence Burstiness (Anti-Metronome)
AI models produce a metronomic cadence where almost every sentence is 18–24 words long.
- Human award papers employ **rhythmic burstiness**:
  * **Short Pivot Sentences (5–10 words)**: Placed at the rhetorical fulcrums (the gap, the root cause, the main insight).
    * *Example*: *"This assumption breaks down under multiscale viewing."*
    * *Example*: *"The bottleneck is computational, not representational."*
  * **Compound Causal Sentences (22–32 words)**: Used to unpack the mechanism, carrying reasons through *because*, *while*, *by*, *which*, or *whereby*.

### 3.3 The Single Aphorism Constraint
Use at most **one** contrastive maxim (*"X is not Y"*) for the central thesis of the paper. Avoid turning the entire Introduction into a manifesto of negations. State the remaining technical findings as positive empirical facts.

### 3.4 Mechanistic Integrity (Zero Invented Content)
- If the user has not specified a mathematical formulation, loss weight, or hyperparameter, write `[TODO: loss formulation]` or `\TODO{}`.
- Never invent baselines, synthetic benchmarks, or speculative numbers to fill a table.
- Schematics show only mechanisms explicitly affirmed by the user; unconfirmed blocks are rendered with dashed borders.
