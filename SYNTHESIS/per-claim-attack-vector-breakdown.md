---
synthesis_type: reader_side_attack_vector_breakdown
framework: e_prime_defense_against_motivated_misreading
claims_covered: 9
companion_to: adversarial-robustness-criterion-6.md
date_executed: "2026-06-17"
tags: [resilience]
---
# Per-Claim Attack-Vector Breakdown
## Part A Detail — Reader-Side Gaming, Worked Per Claim

`adversarial-robustness-criterion-6.md` Part A states a condensed ten-vector pattern and promises this detail file. This document supplies it: for each of the nine claims, which of the ten reader-side attack vectors apply, and how the E-Prime rewrite in that claim's own file actually handles each one — citing the claim file's own Analysis/Ambiguity Flags/Adversarial Interpretation sections rather than restating new analysis.

Not every vector applies with equal force to every claim. Where a vector doesn't meaningfully apply to a given claim, this file says so rather than padding the count.

The ten vectors, as named in the parent document:
1. Causality inversion
2. Selective citation / CI narrowing
3. Evaluative-language smuggling
4. Model-dependence erasure
5. Geometric/parametric conflation
6. Selection bias (flagged, not closed)
7. Underpowering (flagged, not closed)
8. Missing evidence (flagged, not closed)
9. Speculative theory (flagged, not closed)
10. Absent source information (flagged, not closed)

---

## eggs-001 (Li 2013 meta-analysis)

**Strong vectors:**
- **#2 Selective citation/CI narrowing** — rewrite forces RR 1.19 (CI 1.02–1.38) and RR 1.68 (CI 1.41–2.00) into the same sentence as the claim itself, blocking a reader from citing the point estimate alone while dropping the interval.
- **#3 Evaluative-language smuggling** — "there is a dose-response positive association" collapses into a specific pooled RR; the rewrite forces the magnitude question that "is" let the reader skip.

**Flagged-not-closed vectors:**
- **#1 Causality inversion** — claim file's own Ambiguity Flags name this directly: "association" leaves causal direction unaddressed; the rewrite cannot resolve whether egg consumption causes CVD risk or reflects a shared upstream factor — it only prevents the original phrasing from implying causation for free.
- **#10 Absent source information** — the claim file's Adversarial Interpretation notes the pooled analysis shares none of eggs-002's covariate adjustment, making a head-to-head comparison incomplete; the rewrite surfaces this as a named gap rather than letting "association" imply comparability.

**Doesn't meaningfully apply:** #5 (no geometric/parametric content in this claim), #9 (not a speculative-theory claim).

---

## eggs-002 (Zhong/Drouin-Chartier 2020)

**Strong vectors:**
- **#3 Evaluative-language smuggling** — "was not associated" sounds like a stable property; rewrite forces naming the mechanism (multivariable adjustment) that produced the null, the claim file's central move.
- **#4 Model-dependence erasure** — rewrite anchors the null result to "adjustment for lifestyle and dietary factors," blocking citation of "not associated" as if it held independent of model choice.

**Flagged-not-closed vectors:**
- **#6 Selection bias / #10 Absent source information** — claim file's Ambiguity Flags state plainly that the source never specifies whether BMI/statin use got treated as confounders or mediators; the rewrite cannot supply this missing methodological detail, only make its absence visible as the open crux.
- **#1 Causality inversion (source-side variant)** — Adversarial Interpretation section states directly: a source motivated to find eggs safe could select an adjustment model that removes true signal by mistreating mediators as confounders — "nothing in this abstract rules that out." This shows the claim file naming its own blind spot, not claiming a success.

**Doesn't meaningfully apply:** #2 (no CI-narrowing risk; nobody selectively cites the null result's CI), #5, #9.

---

## eggs-003 (Díez-Espino/PREDIMED 2017)

**Strong vectors:**
- **#3 Evaluative-language smuggling** — this gives the vault's clearest single case. "No evidence of interaction" forced into HR 1.33 (CI 0.72–2.46) vs HR 0.96 (CI 0.33–2.76) exposes a 38% point-estimate gap sitting under wide, overlapping intervals. Claim file rates this rewrite_confidence: high and confidence_score: 5 for exactly this reason.
- **#7 Underpowering** — directly named: the claim file's own Analysis states "no evidence of interaction" actually means "underpowered to detect an interaction," not "detected absence of interaction" — flagged, not resolved, since the rewrite cannot manufacture statistical power the original study lacked.

**Flagged-not-closed vectors:**
- **#8 Missing evidence** — claim file notes the ambiguity "lives entirely in the source's plain-language conclusion," meaning a larger, adequately powered subgroup study stands as the only thing that would actually close this gap; the rewrite makes the absence visible, not solved.

**Doesn't meaningfully apply:** #1 (no causal-direction ambiguity here — it's a subgroup-interaction question, not an association claim), #2 (the CI already sits in the rewrite, not selectively dropped), #4, #5, #9, #10.

---

## covid-001 (Peter, epidemiological-timing)

**Strong vectors:**
- **#3 Evaluative-language smuggling** — "seems epidemiologically impossible" forced into "implies 256× the case count actually observed," which the claim file notes "cannot be delivered with the same rhetorical confidence" once the assumption must surface.
- **#4 Model-dependence erasure** — rewrite anchors the argument to "constant 3.5-day doubling," a named assumption the original buried inside "seems."

**Flagged-not-closed vectors:**
- **#6 Selection bias (detection-rate variant)** — claim file's Analysis traces a real internal tension: the same debate transcript elsewhere implies detection rate ran inconstant (post-December-30 wet-market screening), which the 256× argument doesn't address. The rewrite surfaces this as an open question; per the claim file's own Adversarial Interpretation, "neither side, in the actual transcript, runs this calculation explicitly" — the gap stays open, not closed.
- **#10 Absent source information** — the claim file states this plainly: "the argument's force depends entirely on constant detection rate, an assumption Peter doesn't state and doesn't defend."

**Doesn't meaningfully apply:** #2, #5, #9.

---

## covid-002 (Saar, Mr. Chen case)

**Strong vectors:**
- **#3 Evaluative-language smuggling** — "this means" forced into an explicit if/then/contingent-on chain, per the claim file's Analysis. This earns rating as the cleanest single demonstration of vector #3 in the covid case, rewrite_confidence: high.
- **#10 Absent source information** — rewrite explicitly names "the Daily Mail interview's accuracy as the only source for his onset date" as the load-bearing, named dependency — exactly the single point of failure the claim file says the rewrite was built to expose.

**Notable reversal worth flagging directly:** the claim file's own Adversarial Interpretation states this rewrite made the claim more vulnerable to scrutiny, not less — useful for an evaluating reader, double-edged for a debater defending the claim. Listed here because it gives a genuine example of E-Prime cutting against the claim-holder's interest, stronger evidence of non-bias than a rewrite that only ever strengthens claims.

**Doesn't meaningfully apply:** #1, #2, #4, #5, #6, #7, #8, #9 — this claim works structurally as a single-source-reliability case, not a multi-vector one, and the claim file's own Ambiguity Flags state "none remaining after the rewrite."

---

## covid-003 (Peter, furin cleavage site)

**Strong vectors:**
- **#3 Evaluative-language smuggling, with a directional-inversion finding** — "is a mess" and "expected to work poorly" forced into a knowability-at-time-t framing. The claim file's Analysis identifies something beyond the standard pattern: a careless paraphrase of this claim ("shows signs of artificial insertion") doesn't just compress it — it flips which side the evidence supports. This gives the vault's strongest single example of vector #3 doing more than exposing vagueness; it catches a directional error a summary would otherwise launder.
- **#9 Speculative theory** — rewrite anchors the claim to "computational modeling after COVID's emergence," explicitly dating the evidence relative to the event, which the claim file's Adversarial Interpretation uses to frame the real crux: does post-hoc tractability bear on pre-2019 knowability, or not.

**Flagged-not-closed:**
- **#8 Missing evidence** — the crux itself (whether post-2019 computational results say anything about pre-2019 engineering knowledge) remains explicitly unresolved per the claim file's relation_type: crux_candidate tag.

**Doesn't meaningfully apply:** #1, #2, #4, #5, #6, #7, #10.

---

## blackhole-001 (CERN FAQ, energy-equivalence)

**Strong vectors:**
- **#5 Geometric/parametric conflation** — this gives the vault's defining example. The claim file's Analysis identifies that cosmic-ray energy-equivalence (a fast particle striking a stationary target) doesn't automatically establish geometry-equivalence with LHC collisions (two fast particles colliding head-on in the center-of-momentum frame). "Phenomena happen naturally" sounding unrestricted works as exactly evaluative-language smuggling (#3) layered on top of a hidden parameter (#5); the claim file treats this as the first confirmed instance of the "scope-dependency" category predicted in `insight-contribution-v1.md`.

**Flagged-not-closed:**
- **#8 Missing evidence** — claim file states directly that the fuller CERN safety case (LSAG 2008) likely addresses collision geometry but "nothing in this FAQ text closes that gap," and the LSAG report itself never entered this vault.

**Doesn't meaningfully apply:** #1, #2, #4, #6, #7, #9, #10.

---

## blackhole-002 (CERN FAQ, evaporation argument)

**Strong vectors:**
- **#4 Model-dependence erasure** — the claim file's central finding: formation-prediction and evaporation-prediction both derive from the same extra-dimension theoretical package, which the original FAQ presents as two independent safety arguments. The rewrite ("the same...framework predicting...also predicts...") forces the shared dependency into a single sentence, making independence-framing impossible to state without it reading as visibly false.

**Flagged-not-closed, with a genuine refinement worth surfacing honestly:**
- **#8 Missing evidence / #9 Speculative theory** — the claim file's Ambiguity Flags state that resolving which argument (the FAQ's same-theory point, or the LSAG report's independent astrophysical check) "actually carries the safety-relevant weight requires ingesting the LSAG 2008 report directly — not yet done in this vault." Notably, the claim file's own Analysis section goes further and states a tentative conclusion ("the safety-relevant weight likely sits with that independent check, not with the same-theory argument") while explicitly flagging this as the predicted scope-dependency category resolving into a chain-dependency on closer inspection — a real, falsifiable claim the vault states it hasn't closed, not a result dressed up as final.

**Doesn't meaningfully apply:** #1, #2, #6, #7, #10.

---

## Cross-Claim Pattern Summary

| Vector | Strongly demonstrated in | Flagged-only in |
|---|---|---|
| #1 Causality inversion | — | eggs-001, eggs-002 |
| #2 Selective citation/CI narrowing | eggs-001 | — |
| #3 Evaluative-language smuggling | all nine claims, in some form | — |
| #4 Model-dependence erasure | eggs-002, covid-001, blackhole-002 | — |
| #5 Geometric/parametric conflation | blackhole-001 | — |
| #6 Selection bias | — | eggs-002, covid-001 |
| #7 Underpowering | eggs-003 | — |
| #8 Missing evidence | — | eggs-003, covid-003, blackhole-001, blackhole-002 |
| #9 Speculative theory | covid-003 | blackhole-002 |
| #10 Absent source information | covid-002 | eggs-001, eggs-002, covid-001 |

**Honest observation, stated plainly:** vector #3 (evaluative-language smuggling) shows up in every single claim, which makes sense — it gives the mechanism E-Prime targets most directly by construction. The other nine vectors distribute unevenly across the nine claims; no claim demonstrates all ten, and several vectors (geometric/parametric conflation, underpowering) appear strongly in only one claim each. This marks a real limitation of a nine-claim, three-case vault: breadth of vector coverage trades off against depth per claim. A larger vault would let each vector get tested against more than one or two claims, which would matter for judging vector #5 and #7 in particular, where the current evidence rests on a single example each.
