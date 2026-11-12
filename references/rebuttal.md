# Rebuttal: The "Direct Defense & Evidence-First" Protocol

In peer-reviewed venues (CVPR, ICCV, NeurIPS, ICML), **70% of papers that cross the accept boundary do so during the author rebuttal / response period**.

Standard LLM-generated rebuttals are notoriously weak and alienate reviewers through:
1. **Excessive Sycophancy & Groveling**: *"We sincerely thank Reviewer 2 for their profoundly insightful and brilliant comment, and we deeply apologize for our confusing wording..."*
2. **Burying the Answer**: Writing two paragraphs of generic theory before answering a simple yes/no question.
3. **Defensive Argumentation**: Arguing emotionally without providing new numbers, tables, or code evidence.

`Write-Paper-Like-a-Human` enforces the **Direct Defense & Evidence-First Protocol**.

---

## 1. The 4 Rules of Award-Caliber Rebuttals

### Rule 1: The Answer in the Very First Sentence (Bottom-Line First)
An impatient reviewer reads your response while skimming 5 other rebuttals. If your answer is buried in paragraph 3, they will assume you dodged the question.
- **Bad (LLM Default)**: *"Regarding the question about runtime efficiency under large batch sizes, it is important to first consider the memory footprint of cross-attention... [150 words later] ...thus our latency is 42ms."*
- **Good (Human Expert)**: *"Yes, our latency scales sub-linearly with batch size: on an NVIDIA A100, batch size 64 increases latency from 38ms to 42ms (+10.5%), compared to +84.2% for Baseline B (Tab. R1)."*

### Rule 2: Cut the Sycophantic Apologies (Dignified Scholarly Tone)
Reviewers find repeated flattery annoying and suspicious. One brief polite opening at the start of the rebuttal is enough; do not grovel on every point.
- **Banned**: *"We are profoundly grateful for this wonderful observation and humbly apologize for the oversight."*
- **Clean**: *"We thank Reviewer 2 for highlighting this edge case. To address it, we have added the requested ablation below."*

### Rule 3: Concrete Evidence Over Philosophical Debate
Never counter a reviewer critique with abstract assertions. Respond with:
1. A new numerical experiment, ablation row, or standard deviation metric.
2. A citation to a recognized peer-reviewed benchmark.
3. An exact manuscript update pointer (`Lines 234–241 in Section 4.2`).

### Rule 4: Respectful Disagreement (Standing Your Ground with Data)
When a reviewer is factually mistaken or demands an experiment outside the paper's scope:
- Do not say: *"The reviewer is mistaken and misunderstood our contribution."*
- Do not say: *"We apologize and will do whatever the reviewer asks."*
- State:
  1. Restate the shared premise: *"We agree that [X] is an important challenge in general."*
  2. Clarify the boundary condition: *"However, our paper explicitly targets [Setting Y], where assumption [Z] holds by definition (Lines 45–52)."*
  3. Provide empirical corroboration: *"Under Setting Y, Table 2 demonstrates that relaxing Z degrades PSNR by 4.2 dB, confirming that our design is necessary."*

---

## 2. Rebuttal Template Structure (`template/CVPR2027/rebuttal.tex`)

Organize responses into clear, labeled blocks matching each reviewer's numbering:

```latex
\section*{Response to Reviewer 1 (R1)}

\noindent\textbf{Q1: Sensitivity to Camera Pose Noise.}
\textit{"How does the method handle noisy camera poses in real-world captures?"}

\smallskip\noindent
\textbf{Answer:} Our method remains robust to pose noise up to $2^\circ$ rotation and $5\%$ translation error, outperforming 3DGS by 1.8 dB (Tab.~R1).

\begin{table}[h]
\centering
\small
\begin{tabular}{lcccc}
\toprule
Pose Noise ($\sigma_\text{rot}$) & $0^\circ$ & $1^\circ$ & $2^\circ$ & $5^\circ$ \\
\midrule
3DGS [12] & 28.4 & 25.1 & 21.3 & 16.8 \\
\textbf{Ours} & \textbf{30.2} & \textbf{28.9} & \textbf{26.8} & \textbf{21.4} \\
\bottomrule
\end{tabular}
\caption{PSNR under injected pose noise on Tanks and Temples.}
\label{tab:r1}
\end{table}

\noindent
\textbf{Paper Revision:} We have added Tab.~R1 and the corresponding discussion to Sec.~5.3 (Lines 410--425).
```

---

## 3. Rebuttal Checklist
- [ ] Is the direct answer stated in the very first sentence of each response?
- [ ] Are all flattery formulas (*"profoundly grateful"*, *"humbly apologize"*) deleted?
- [ ] Is every numerical claim backed by a concrete table (`Tab. R1`), figure, or citation?
- [ ] Does each item state exactly where the manuscript text will be updated?
- [ ] Does the rebuttal strictly respect the conference page/word limit (e.g., CVPR 1-page PDF limit)?
