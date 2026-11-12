# The 26 Anti-AI Tell Patterns in Scientific & Academic Writing

Derived from Wikipedia's WikiProject AI Cleanup ("Signs of AI writing"), calibrated against 60 CVPR/ICCV/NeurIPS award papers, and reinforced by StoryScope (COLM 2026).

Every pattern represents a default, generic choice made by LLMs when generating text. Human academic experts write with specific intent, variance, and rigorous economy.

---

## Section A: Staging Instead of Stating (§1–§5)
*Act on one sighting. These immediately signal an AI generator.*

### §1 — Not X, but Y (The Antithetical Preach)
- **The Tell**: *"Our goal is not merely to improve benchmark accuracy, but rather to fundamentally rethink the paradigm of spatial representations."* Or clipped negative tails: *"fast, reliable, and with no guessing."*
- **Academic Human Fix**: State the claim directly. Keep the contrast only when correcting a widespread technical misconception held by the community.
- **Before**: *"It is not a matter of simply adding more parameters, but of reparameterizing the loss."*
- **After**: *"Reparameterizing the loss directly on the policy eliminates the need for a separate reward model."*

### §2 — One-Line Closers & Dramatic Fragments
- **The Tell**: Ending a paragraph with a dramatic one-liner: *"That is the true power of latent diffusion."* Or fragmented telegraphic sentences: *"No retraining. No complex pipeline. Just clean representations."*
- **Academic Human Fix**: Cut the empty closer. State the concrete takeaway or number.
- **Before**: *"By decoupling the heads, training converges in half the epochs. Efficiency achieved."*
- **After**: *"Decoupling the heads halves the required training epochs from 120 to 60."*

### §3 — Sayings That Sound Deep
- **The Tell**: Pseudo-philosophical academic fluff: *"At its core, visual understanding is the language of geometry."*, *"Attention is the currency of modern transformers."*
- **Academic Human Fix**: Replace the metaphor with the mathematical or operational fact.
- **Before**: *"At its core, diffusion represents the delicate dance between noise and structure."*
- **After**: *"Diffusion models reverse a discrete forward Gaussian perturbation process via score matching."*

### §4 — Staged Run-Up Before the Point
- **The Tell**: Standalone meta-openers: *"To understand why this happens, we must first look at...", "Here is the key takeaway:", "It is instructive to examine..."*
- **Academic Human Fix**: Delete the run-up and start directly with the finding.
- **Before**: *"To see why existing methods struggle, consider the following observation. When camera zoom diverges..."*
- **After**: *"When camera zoom diverges from the training distribution, screen-space dilation causes severe aliasing (Fig. 1)."*

### §5 — Arguing with No One (Phantom Defenses)
- **The Tell**: Defensive pre-emptive hedges against imaginary critics: *"To be clear, we are not suggesting transformers are obsolete...", "One might wonder if this is just overfitting, but..."*
- **Academic Human Fix**: Remove the defensive apology. Only address specific baseline comparisons or empirical failure modes in the Limitations section.
- **Before**: *"Don't get us wrong, standard SGD is effective, but our optimizer behaves differently."*
- **After**: *"While SGD converges stably on convex objectives, our adaptive schedule prevents oscillatory divergence in non-convex saddle regions."*

---

## Section B: Rhythm by Rule (§6–§11)

### §6 — Forced Triads (The Symmetrical Rule of Three)
- **The Tell**: Forcing three parallel adjectives, clauses, or nouns everywhere: *"Our model is scalable, efficient, and robust."*, *"It handles occlusions, preserves details, and generates photorealistic textures."*
- **Academic Human Fix**: Keep only the properties you actually benchmark. Vary the list length (two distinct points or four detailed benchmarks).
- **Before**: *"The framework provides seamless integration, unprecedented speed, and superior fidelity."*
- **After**: *"The framework runs at 140 FPS on a single RTX 4090 while improving PSNR by 2.4 dB over 3DGS."*

### §7 — Repeated Sentence Openings
- **The Tell**: Three consecutive sentences starting with "We...", "Our approach...", or "This...".
- **Academic Human Fix**: Vary the grammatical subject: lead with the mechanism, the data, or the condition.
- **Before**: *"We propose a new filter. We evaluate it on seven scenes. We observe substantial improvements."*
- **After**: *"A 3D smoothing filter restricts the gaussian footprint according to the Nyquist limit. On seven multi-scale scenes, this formulation reduces rendering error by 60%."*

### §8 — Em Dashes (—) as the Universal Crutch
- **HARD RULE**: Award papers and clean academic prose avoid em dashes (`—`) and en dashes (`–`) as lazy parenthetical splices.
- **Academic Human Fix**: Replace with a period (splitting into two concise sentences), a colon, parentheses, or commas.
- **Before**: *"The core mechanism—integrated positional encoding over conical frustums—eliminates aliasing artifacts."*
- **After**: *"The core mechanism (integrated positional encoding over conical frustums) eliminates aliasing artifacts."*

### §9 — Stacked Qualifiers & Over-Hedging
- **The Tell**: *"This might arguably suggest that the model could potentially achieve..."*
- **Academic Human Fix**: State the empirical finding directly: *"This indicates that the model achieves..."*

### §10 — Hyphenated Pairs Everywhere
- **The Tell**: Hyphenating predicate adjectives after nouns: *"the representation is end-to-end"* instead of *"the representation is end to end"*.
- **Academic Human Fix**: Keep hyphens for compound modifiers before nouns (*"an end-to-end model"*), drop after nouns.

### §11 — Passive Voice & Missing Subjects
- **The Tell**: Hiding the actor: *"It was observed that performance deteriorated when..."*
- **Academic Human Fix**: Use active voice: *"Performance drops by 3.1 dB when the sampling stride doubles."*

---

## Section C: Inflation and Borrowed Authority (§12–§18)

### §12 — Overused AI Vocabulary
- **Banned Words & Tells**:
  `actually`, `additionally`, `align with`, `bolstered`, `crucial`, `delve`, `enduring`, `enhance`, `garner`, `game-changer`, `highlight` (verb), `interplay`, `intricate`, `intricacies`, `key` (adj, overused), `landscape`, `meticulous`, `pivotal`, `quietly`, `realm`, `revolutionize`, `robust` (without range), `seamless`, `seamlessly`, `showcase`, `tapestry`, `testament`, `underscore` (verb), `valuable`, `vibrant`.
- **Academic Human Fix**: Use precise technical terms: *computes, bounds, matches, reduces, formulates, measures*.

### §13 — Inflated Significance & Boilerplate
- **The Tell**: *"This paper stands as a testament to the transformative power of attention mechanisms..."*, *"Extensive experiments demonstrate the unprecedented superiority of our model."*
- **Academic Human Fix**: Delete all self-praise. State the metric delta.
- **Before**: *"Our pioneering method unlocks the full potential of diffusion, setting a new milestone."*
- **After**: *"Our method achieves a state-of-the-art FID of 1.78 on ImageNet 512x512, outperforming DiT-XL/2 by 0.49 points."*

### §14 — Vague Technical Connection
- **The Tell**: *"Module A is closely associated with Module B, facilitating efficient feature exchange."*
- **Academic Human Fix**: Name the mathematical connection: *"Module A passes concatenated multi-scale feature maps directly to Module B via residual cross-attention."*

### §15 — Shallow Trailing -ing Phrases
- **The Tell**: Ending sentences with participial significance claims: *", making real-time rendering possible"*, *", thereby underscoring its efficacy"*, *", paving the way for future exploration"*.
- **Academic Human Fix**: Make the consequence an independent clause with cause (*"because"*, *"which"*, *"whereby"*) or state it as an empirical measurement.

### §16 — Sales Language & Marketing Hype
- **The Tell**: *"A breathtaking array of qualitative results demonstrates the profound versatility of our groundbreaking tool."*
- **Academic Human Fix**: Plain factual reporting: *"Qualitative comparisons across six outdoor scenes show consistent recovery of high-frequency foliage textures."*

### §17 — Borrowed Authority & Phantom Consensus
- **The Tell**: *"Researchers widely agree that 3D reconstruction is difficult."*, *"Experts have long argued..."*
- **Academic Human Fix**: Cite specific foundational papers: *"View synthesis under varying focal distances introduces scale-dependent aliasing (Mildenhall et al., 2020)."*

### §18 — Avoiding Is, Are, and Has
- **The Tell**: Replacing basic copulas with ornate substitutes: *"Our architecture boasts three branches"*, *"The loss serves as a regularizer"*.
- **Academic Human Fix**: Use plain verbs: *"Our architecture has three branches"*, *"The loss regularizes the latent space"*.

---

## Section D: Formatting and Visual Slop (§19–§21)

### §19 — Bold as Inline Decoration
- **The Tell**: Spraying bold font inside sentences as visual caffeine: *"Our model is **fast**, **accurate**, and **general**."*
- **Academic Human Fix**: Plain text. Use bold only for paragraph lead-ins (run-in headings) like **Preliminaries.** or in table headers.

### §20 — Decorative Headings & Emojis
- **The Tell**: Headings with emojis or marketing taglines: *"### 🚀 3. Methodology: Unleashing the Power of Cones"*.
- **Academic Human Fix**: Standard clean academic section titles: *"3. Method"*, *"3.1. Conical Frustum Formulation"*.

### §21 — Punctuation Consistency
- Use straight ASCII quotes in code and standard LaTeX quotes (` ``text'' `) in `.tex` files.

---

## Section E: Leftovers from Chat & Workflow Traces (§22–§25)

### §22 — Chatbot Residue
- Remove all conversational scaffolding: *"Sure, here is the draft"*, *"As requested, below is the revised method"*.

### §23 — Knowledge-Limit Disclaimers
- Avoid writing: *"As of recent developments..."*, *"While specific details are limited..."*. State facts authoritatively.

### §24 — Heading Repeated in First Sentence
- Do not repeat the section header as the opening words:
  *Header*: `### 3.2 Loss Formulation`
  *Bad*: *"In this subsection, we describe the loss formulation."*
  *Good*: *"We train the network using a composite objective combining photometric reconstruction and geometric consistency."*

### §25 — Writing About the Writing Process
- Banned phrases: *"The authors note that..."*, *"As supplied in the intake form..."*, *"According to the provided data..."*. Write directly as the researcher: *"We measure..."*.

---

## Section F: Writing for the Wrong Reader (§26)

### §26 — Re-explaining Textbook Basics
- **The Tell**: Spending three paragraphs re-explaining standard convolutional layers or basic Bayes rule to expert CVPR/NeurIPS reviewers.
- **Academic Human Fix**: Assume an expert colleague. Jump straight to the unique technical delta, citing standard background in one sentence.
