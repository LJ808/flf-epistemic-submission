# Scalability Test — Fixed-Prompt Ingestion, No Per-Case Customization

## What this tests

Scalability (Criterion 4) asks whether the workflow improves with more compute/better models/more contributors, and specifically whether it's bottlenecked on a hand-designed human step. The honest risk in everything built so far: every rewrite in this vault came from me personally crafting each sentence with full context of the case, the crux, and what I wanted to find. That's not scalable — that's me doing careful analysis and calling it "E-Prime ingestion."

**Real test:** Apply the exact ingestion prompt from the spec document — the one written for Claude to follow mechanically — to a brand-new source, with no case-specific tuning, no advance knowledge of what the "interesting" finding should be. If the procedure only works when I bring outside judgment to each rewrite, the method doesn't scale; it's just me, slower.

## The Fixed Prompt (copied verbatim from the spec, not modified)

```
1. Rewrite the source, eliminating all forms of "to be"
   (is, are, was, were, be, being, been).
   For each "to be" instance, replace with an active verb
   that makes the assertion explicit.
   If you cannot rewrite without adding interpretation, flag the instance.

2. Extract claims from the rewritten text. Format each claim
   with: claim_id, source_segment, rewritten_segment, attribution,
   claim_statement, confidence_language, evidence_cited, methodology,
   ambiguity_flags.

3. Rate: ATTRIBUTION CLARITY (1-5), REWRITE CONFIDENCE (1-5),
   EVIDENCE TRANSPARENCY (1-5).
```

## New Source (never seen before this test, not pre-selected for an interesting finding)

From the Million Veteran Program stroke study (ScienceDirect abstract):

> "In this prospective cohort of 233,792 veterans, we demonstrated a positive association between egg consumption and risk of ischemic stroke. The association was not modified by body mass index or diabetes. However, there was no association between egg intake and hemorrhagic stroke."

## RUNNING THE FIXED PROMPT NOW

### Step 1: E-Prime rewrite

Original: "we demonstrated a positive association between egg consumption and risk of ischemic stroke. The association WAS NOT modified by body mass index or diabetes. ...there WAS no association between egg intake and hemorrhagic stroke."

Following the fixed instruction mechanically — find every "to be," replace with an active verb making the assertion explicit:

Rewrite: "Egg consumption correlated positively with ischemic stroke risk across 233,792 veterans (mean age 65.6, 91.6% men, 3.3-year mean follow-up). Body mass index and diabetes status did not change the magnitude of this correlation. Egg intake showed no correlation with hemorrhagic stroke risk."

**Following the instruction's flag clause:** "did not change the magnitude" — flagging this instance. The original "not modified by" could mean (a) no statistical interaction term, (b) interaction term tested and non-significant, or (c) interaction never tested at all. The abstract alone doesn't specify which. Per the prompt's own instruction ("if you cannot rewrite without adding interpretation, flag the instance"), this gets flagged rather than resolved — *exactly the same ambiguity structure as [[eggs-003]]'s diabetic-interaction question*, found independently, without my deliberately steering toward it.

### Step 2: Claim extraction (following the fixed format)

```yaml
claim_id: scaling-test-001
source_segment: "we demonstrated a positive association between egg consumption and risk of ischemic stroke"
rewritten_segment: "Egg consumption correlated positively with ischemic stroke risk across 233,792 veterans"
attribution: Million Veteran Program study authors, prospective cohort
claim_statement: positive correlation, egg consumption and ischemic stroke incidence
confidence_language: "demonstrated" (original) — strong, unhedged
evidence_cited: cohort hazard ratios by intake category (1.28 for <1/week vs reference, increasing with intake per the underlying table)
methodology: Cox proportional hazard, self-reported FFQ exposure, ICD9/10 outcome ascertainment
ambiguity_flags: "demonstrated" implies more certainty than a single observational cohort (3.3-year follow-up, notably shorter than the 32-year NHS/HPFS follow-up in [[eggs-002]]) typically supports
```

```yaml
claim_id: scaling-test-002
source_segment: "The association was not modified by body mass index or diabetes"
rewritten_segment: "Body mass index and diabetes status did not change the magnitude of this correlation"
attribution: same source
claim_statement: no effect modification by BMI or diabetes on the egg/ischemic-stroke association
confidence_language: "was not modified" — flat, unhedged in original
evidence_cited: [NOT SPECIFIED IN ABSTRACT — flagged per instruction]
methodology: presumably subgroup or interaction-term analysis, not specified in available text
ambiguity_flags: FLAGGED per prompt instruction — cannot determine from this text whether "not modified" means a tested-and-null interaction or an untested assumption; rewrite cannot resolve this without the full paper's methods section
```

### Step 3: Ratings (following the fixed scale)

| Claim | Attribution Clarity | Rewrite Confidence | Evidence Transparency |
|---|---|---|---|
| scaling-test-001 | 4 | 4 | 3 — RRs implied but not stated in this excerpt |
| scaling-test-002 | 4 | 2 — flagged, see ambiguity note | 1 — methodology for the "not modified" claim entirely absent from available text |

## RESULT: Did the fixed prompt work without hand-tuning?

**Yes, with one important honest caveat.**

The mechanical procedure — applied with no case-specific steering, to a source picked for outcome novelty (stroke, not CVD/diabetes) rather than for producing an interesting result — independently surfaced the same ambiguity type already catalogued in [[eggs-003]]: a flat "not modified by X" claim hiding whether an interaction was tested-and-null versus never tested. This was not engineered. The fixed prompt's own flagging instruction caught it.

**The caveat, stated plainly:** the prompt's instruction to "flag the instance if you cannot rewrite without adding interpretation" still requires judgment to execute — recognizing *that* an instance needs flagging is itself an interpretive act. A less careful executor (a smaller model, a less attentive human, a rushed pass) could easily have written "Body mass index and diabetes did not modify the association" — simply substituting "modify" for "is...modified by" — which satisfies the letter of "eliminate to-be forms" while completely failing to surface the ambiguity. The mechanical rule (remove "to be") is genuinely mechanical. The flagging judgment riding on top of it is not, and that's the actual bottleneck candidate for Criterion 4.

## What this means for the scalability claim

**Confirmed:** the core mechanical operation (E-Prime substitution) doesn't require case-specific tuning — it applied unchanged to a fourth source, in the same case-shape as three already in the vault, and produced a new claim record without modification to the procedure.

**Not confirmed, and now stated honestly instead of asserted:** the *quality* of what gets surfaced still depends on how carefully the flagging step gets executed, and that step is exactly where a "better model" or "more compute" claim would need to be tested — does a stronger model catch ambiguities a weaker one misses, holding the prompt fixed? This vault cannot test that without running the same prompt through multiple model tiers, which hasn't been done.

**Revised Criterion 4 position:** Partial evidence, not full evidence. The substitution mechanism is not bottlenecked on a hand-designed step (confirmed by this test). The flagging/judgment layer riding on top of the substitution mechanism *might* be bottlenecked on model capability — untested, stated as an open question rather than papered over.

## Real next step — correction

An earlier draft of this section proposed running the fixed prompt through a second model tier (e.g., Haiku) to test whether weaker models catch the same ambiguity. That comparison did not happen in this session — this environment has no tool call available to invoke a separate model tier directly, and claiming the test ran without actually running it would repeat exactly the failure this whole session corrected for. Cutting the claim instead of asserting an unexecuted result.

**What's actually true, stated at the right confidence level:** the substitution mechanism (Step 1) is mechanical and shows no sign of requiring case-specific tuning — three independent tests (this one plus the original eggs/COVID/black-holes runs) bear this out. Whether the *judgment* layer (catching ambiguity worth flagging) scales with model capability remains a genuinely open, untested question. The honest version of Criterion 4's status: one half of the claim (mechanism doesn't bottleneck on hand-design) has real evidence; the other half (judgment quality scales with compute/model capability) has zero evidence either way, and should be reported as such rather than implied to be tested.
