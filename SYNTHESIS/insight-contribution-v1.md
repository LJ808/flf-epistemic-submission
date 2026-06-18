# Insight Contribution — The Hidden-Dependency Typology

## What this document does

The two worked examples (eggs/CVD, COVID debate) didn't just demonstrate that E-Prime ingestion works. Read against each other, they surfaced something neither one shows alone: **the kind of error E-Prime exposes changes predictably with the source's epistemic shape, and that change is itself diagnostic of what kind of investigation a case requires.**

This document states that finding directly, tests whether it holds beyond the two examples already run, and names what would falsify it.

---

## The finding, stated plainly

Standard summaries fail in a specific, recurring way: they compress a claim's *dependency* — the thing the claim actually rests on — into a "to be"-verb construction that reads as a property of the world rather than a property of the argument.

"There is an association" reads as a fact about eggs. It actually means: *given this specific covariate-adjustment model.*

"This means X happened" reads as a logical fact. It actually means: *given this one source's accuracy, with no corroboration.*

E-Prime rewriting forces every such claim to name its dependency, because "is an association" and "this means" both resist E-Prime rewrite without naming what stands behind them. That much held across both worked examples. What differed is **what kind of dependency got exposed**:

| Case-shape | What "to be" was hiding | What got exposed |
|---|---|---|
| Pooled epidemiological meta-analysis (eggs) | A *methodological choice* — which covariates the analysts adjusted for, and whether those covariates were confounders or mediators | **Model-dependency**: the claim is true *of this model*, not true *of eggs* |
| Adversarial point-counterpoint debate (COVID) | A *conditional chain* — a deduction's validity resting on one link (one source, one timing claim, one assumption held constant) | **Chain-dependency**: the claim is true *if this one link holds*, and the debate's real action is attacking that link |

These aren't two examples of the same thing. They're two different failure modes that happen to share a grammatical signature (a "to be" verb absorbing the hedge). That's the actual discovery: **the grammatical tell stays uniform even though the underlying epistemic problem doesn't.** E-Prime works as a *detector* across shapes precisely because it doesn't care what kind of dependency it's exposing — it only cares whether a sentence can survive having "is/was/are" removed. But what an investigator does *after* detection differs completely by shape: in the epidemiology case, the next move asks whether the adjustment was appropriate (a statistics question). In the debate case, the next move finds and attacks the single dependent link (an evidentiary question).

## Why this matters more than "E-Prime helps clarity"

A submission claiming "E-Prime forces precision" makes a true but unremarkable claim — clarity-via-constraint sits as the original justification for E-Prime in general semantics, not a new one. What's not obvious, and what the two-case comparison actually shows, holds that **the same mechanical detector generalizes across epistemically distinct failure modes without modification, while the diagnostic output tells you which failure mode you're looking at.**

That matters for exactly the reason FLF's own framing names: a workflow that requires reconfiguration per case-shape doesn't scale or compound. A workflow whose detection mechanism stays fixed while its diagnostic output adapts to the case *does* — because adding a third, fourth, or fortieth case-shape doesn't require redesigning the ingestion step, only building a typology of what dependency-types tend to show up where.

## A third prediction, stated before testing it (so it can be falsified)

If this finding holds, the **black holes / CERN case** — the competition's third case study, an essentially settled-consensus topic — should produce a *third* dependency type, distinct from model-dependency and chain-dependency. Prediction, made now, before running the ingestion:

**Predicted dependency type: scope-dependency.** Consensus claims ("CERN will not generate a dangerous black hole") typically hide not a model choice or a single evidentiary link, but a *scope restriction* — the claim holds within a stated parameter range (collision energy, black hole evaporation timescale assumptions) that the plain-language version drops silently. "Black holes will evaporate before causing harm" reads as a settled fact; the E-Prime-forced version needs to state *which* evaporation mechanism (Hawking radiation) and *under which untested energy regime* the claim holds, surfacing whether the consensus rests on extrapolation beyond direct observation rather than on direct evidence.

**This prediction stands as falsifiable.** If running the actual ingestion on CERN FAQ material produces a model-dependency or chain-dependency instead of a scope-dependency, the typology needs revision — either a fourth category, or evidence that the three-case-shape framing collapses into fewer categories than predicted. Either outcome adds real information; this isn't a hedge, it's a test condition specified in advance of running it.

**Result, confirmed after running the ingestion (see [[blackhole-001]] and [[blackhole-002]]):** the prediction held, with a refinement the prediction itself didn't anticipate. Both CERN FAQ claims exposed a scope-dependency on first rewrite, exactly as predicted. But tracing each scope-dependency one level deeper revealed it resolving into a chain-dependency underneath — [[blackhole-002]]'s safety argument ultimately depends on whether an independent astrophysical-observation check (not the same-theory-predicts-both-formation-and-evaporation argument) carries the actual safety-relevant weight. This means the three categories may not partition cleanly — scope-dependency, examined closely enough, can resolve into chain-dependency one inference-step removed from the surface. A genuine, falsifiable open question follows from this: does a fourth case-shape (a values-disagreement, or a pure-math dispute) produce a dependency type clearly *not* reducible to chain-dependency, or does everything eventually reduce to "which single link, if broken, changes the conclusion"?

## What this typology is for, downstream

If it holds across all three FLF case studies (and ideally beyond them), the typology becomes the actual reusable artifact — more reusable than the Obsidian schema itself. A future investigator approaching a new case could ask, before doing any ingestion: *what shape does this dispute take — pooled-quantitative, adversarial-chain, or consensus-scope?* — and use that to predict where the hidden dependencies will cluster, before reading a single source. That holds as a testable, falsifiable claim about how to triage an unfamiliar epistemic dispute, closer to what Criterion 7 asks for ("surfaces sub-problems, framings, or considerations we'd missed") than anything claimed in the original submission draft.

## What this document does not claim

- It does not claim three dependency types exhaust the space. A fourth case-shape (e.g., a purely mathematical proof dispute, or a values-disagreement dressed as a factual one) might produce a dependency type not yet seen.
- It does not claim the typology derives from theory. It derives from two executed examples and one stated, tested prediction. The prediction held, with a refinement neither example anticipated — a different outcome than simple confirmation, and worth naming as such rather than smoothing into "the prediction was correct."
- It does not claim this typology stands unique to E-Prime as a detection method. It claims E-Prime works as a *cheap, mechanical* way to trigger the detection, not the only possible one. Whether other constraints (e.g., forbidding modal verbs, forbidding nominalizations) would surface the same typology faster or more reliably remains untested and stands as a reasonable adversarial question for judges to raise.
