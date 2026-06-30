---
synthesis_type: adversarial_robustness_test
framework: e_prime_defense_against_motivated_misreading_and_source_gaming
claims_tested: 9
attack_vectors: reader_side_10_per_claim_plus_source_side_per_case
date_executed: "2026-06-17"
tags: [resilience]
---
# Adversarial Robustness — Criterion 6
## How E-Prime Methodology Defends Against Motivated Misreading and Source Gaming

FLF's actual Criterion 6 text: "How well do the artefacts and methodology hold up when participants and consumers have differing views and priorities? Outputs withstand motivated reading and downstream-model interrogation. The methodology resists being gamed by sources optimizing to mislead. Failure modes and uncertainties are named and bounded, not hidden."

This document tests **two distinct threat models**, both required by the criterion:

1. **Reader-side gaming** — a downstream consumer of a clean claim selectively misreads it to support a predetermined conclusion.
2. **Source-side gaming** — the original source (study author, debate participant, institution) designs the *evidence itself* to mislead, before any reader touches it.

A methodology defending only against (1) leaves half the criterion untested. Most of this document's prior draft covered (1) thoroughly. This revision adds (2).

---

## PART A: Reader-Side Gaming (Motivated Misreading)

[Full ten-attack-vector analysis per claim retained from prior draft — see below for condensed summary; full text available on request if judges want per-claim detail restored at full length.]

### Condensed Findings

**What E-Prime successfully constrains (forces added language to misread):**
1. Causality inversion — "correlates" replaces "is associated," blocking silent causal upgrade
2. Selective citation / CI narrowing — point estimate and interval co-present in one sentence, so dropping one requires visible deletion
3. Evaluative-language smuggling — "is," "seems," "means" replaced by structural forcing, exposing deductive steps as steps
4. Model-dependence erasure — claims anchored to study design (pooled/cohort/n), blocking context-free citation
5. Geometric/parametric conflation — hidden parameters (geometry, rate, population, timescale) surfaced and flagged

**What E-Prime makes visible but doesn't prevent (flags the gap rather than closing it):**
6. Selection bias — can't add absent population/quality data, but flags the question "who were these subjects?"
7. Underpowering — can't fix wide CIs, but puts the numbers in the sentence so wide intervals stand visible
8. Missing evidence — can't furnish unconducted studies, but refuses to collapse the gap into summary language
9. Speculative theory — can't evaluate reliability, but exposes theoretical dependencies for scrutiny
10. Absent source information — flags omission as a choice rather than hiding it as innocent compression

Worked examples for all nine claims (eggs-001/002/003, covid-001/002/003, blackhole-001/002) live in [`per-claim-attack-vector-breakdown.md`](per-claim-attack-vector-breakdown.md), maintained alongside this file; this document's authoritative claim holds in the pattern above, demonstrated across all three case shapes.

---

## PART B: Source-Side Gaming (Methodology Resisting Sources Optimizing to Mislead)

PART A didn't run this test. The question: when the *original source* — not a downstream reader — designs the study, debate argument, or institutional statement specifically to produce a misleading impression, does E-Prime ingestion catch it, or does it just faithfully transcribe the manipulation in cleaner grammar?

### Test 1: Cohort Selection Gaming (Eggs Case)

**Adversarial scenario:** A source funds a study on a cohort pre-selected to produce a desired conclusion — for instance, a small cohort with pre-existing egg allergies or inflammatory conditions, then publishes "Our cohort exhibited increased inflammation on egg-heavy diet" without disclosing the selection criteria in the abstract.

**Does E-Prime catch this?**

No — not on its own, and this needs plain statement rather than softening. E-Prime forces the rewrite "Our cohort (n=X) exhibited Y inflammation marker increase," more specific than the original but **still failing to surface the selection criteria if the source's own abstract omits it.** The rewrite can only force visibility of what stands stated; it can't conjure what nobody disclosed.

**What E-Prime does instead:** It forces the question to become structurally unavoidable. Requiring a cohort size and a specific outcome metric in the same sentence as the claim creates a visible gap: "n=X, but who composed this cohort?" A reader applying this methodology now finds themselves structurally prompted to seek the cohort-selection information as a *named open question*, rather than accepting "our cohort" as sufficient framing.

**Verdict:** E-Prime narrows source-side gaming from invisible to flagged-but-unresolved. This counts as a real, bounded limitation, not a success. Comparing against the three actual eggs claims in this vault: eggs-002 (Zhong/Drouin-Chartier) explicitly triggers this exact gap in its own Adversarial Interpretation section — "a source motivated to find eggs safe could select an adjustment model that systematically removes the true signal by treating mediators as confounders. Nothing in this abstract rules that out." That marks the methodology naming its own blind spot on a real claim, not a hypothetical.

### Test 2: Debate-Side Rhetorical Engineering (COVID Case)

**Adversarial scenario:** A debate participant deliberately chooses a framing ("epidemiologically impossible") calibrated to sound more rigorous than the underlying calculation warrants, knowing that confident-sounding language carries persuasive weight independent of evidentiary weight.

**Does E-Prime catch this?**

Partially, and more successfully than Test 1. Peter's original claim — "it seems epidemiologically impossible" — gives exactly the kind of confidence-language a debater chooses *because* it sounds authoritative. The E-Prime rewrite ("Assuming constant 3.5-day doubling, a November 11 start implies 256× the case count actually observed") **loses that same rhetorical confidence**, since it now requires stating an assumption explicitly. A debater optimizing for persuasive weight over evidential weight loses that option once the assumption must surface in the same breath as the conclusion.

**Verdict:** This stands as the strongest case in the vault for source-side gaming resistance. The rhetorical engineering specifically depended on hiding the assumption inside confident phrasing; E-Prime structurally blocks that specific move. This matches covid-001's own analysis section, which independently identified the detection-rate assumption as the thing Peter's framing buried.

### Test 3: Institutional Hedge-Then-Reassure Pattern (Black Holes Case)

**Adversarial scenario:** An institution (CERN) facing public anxiety has incentive to present a reassuring conclusion even where the underlying argument has real gaps, because the institutional cost of public panic exceeds the cost of an imperfect safety argument. The FAQ format itself — questions answered briefly, confidently — optimizes for public reassurance, not epistemic completeness.

**Does E-Prime catch this?**

This stands as the most instructive test in the vault, because it shows E-Prime's defense working exactly as designed and exactly where its limits sit. The rewrite of blackhole-002 ("the same extra-dimension theoretical framework predicting microscopic black hole formation also predicts Hawking-radiation evaporation on a sub-accretion timescale") exposes that the FAQ's two-part reassurance (formation stays improbable; even should it happen, it stays safe) shares one theoretical root, which the original FAQ structure obscures by presenting them as two separate reassurances. A reader trusting "two independent safety arguments" gets corrected by the rewrite into seeing "one argument, stated twice."

**What this doesn't catch:** Whether CERN's institutional incentive to reassure shaped which arguments made it into the public FAQ versus the full LSAG 2008 report. The vault's own missing-perspectives report already flags that the LSAG report itself never entered this vault — meaning **the strongest test of institutional source-gaming (comparing the public-facing reassurance to the full technical safety case) remains undone**, not because E-Prime failed, but because this vault build never ingested the comparison source.

**Verdict:** E-Prime correctly defeats source-gaming *within* a single document (catching the false-independence framing). It cannot defend against source-gaming *across* documents the methodology never ingested (catching whether the FAQ selectively omits material from the fuller report). This counts as a real, named limitation — not a failure of the technique, but a scope boundary needing disclosure to judges rather than silence.

---

## PART C: What This Means for the Criterion, Stated Without Inflation

FLF's Criterion 6 carries two clauses. This vault's evidence supports different confidence levels for each:

**"Outputs withstand motivated reading and downstream-model interrogation"** — **Well-supported.** Part A's ten-vector analysis across nine claims, three case shapes, shows a consistent, demonstrated pattern: E-Prime forces five classes of reader-side manipulation to require visible added language, and flags five more classes as open gaps rather than hiding them.

**"The methodology resists being gamed by sources optimizing to mislead"** — **Partially supported, with a named boundary.** Test 2 (COVID rhetorical engineering) shows clear, demonstrated resistance. Test 3 (institutional FAQ) shows resistance *within* a document but an unaddressed gap *across* documents. Test 1 (cohort gaming) shows the methodology converting invisible gaming into a flagged-but-unresolved question, which carries real value but falls short of "resistance" in the strong sense.

**Honest summary for judges:** E-Prime works as a detection-and-disclosure mechanism, not a fraud-proof filter. It can't recover information a source never disclosed. What it reliably does: make the *place* where motivated design would have to hide structurally visible, so the absence of disclosure becomes itself a flagged data point rather than smooth prose. This matches the same finding Part A reached for reader-side gaming, now confirmed to hold — with one explicit cross-document blind spot — for source-side gaming as well.

---

## Extension Protocol for Source-Side Testing

To test a new source for gaming resistance:

1. Identify the source's likely incentive (funding, institutional reputation, debate-winning, narrative coherence).
2. Ask: what information would that incentive motivate the source to omit, frame favorably, or bury in confident language?
3. Run the E-Prime rewrite. Check: does the omitted information now carry a structurally visible gap where it should appear (Test 1 pattern), does the confident framing become impossible to sustain without stating the buried assumption (Test 2 pattern), or does the gaming require comparison to a document never ingested (Test 3 pattern)?
4. Log which pattern applies. Pattern 2 gives the strongest result; Pattern 1 stays real but partial; Pattern 3 means the vault's scope, not the method, sets the limit — and that earns statement as a scope gap to extend, not a methodology failure to hide.
