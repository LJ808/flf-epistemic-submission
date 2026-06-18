---
claim_id: eggs-002
case: eggs-health
subtopic: cvd-risk
source_ref: "[[zhong-drouin-chartier-2020-bmj]]"
confidence_score: 3
rewrite_confidence: medium
methodology: prospective_cohort_multivariable_adjusted
relation_type: contests
---

# Egg intake and CVD risk — 3-cohort pooled analysis (Zhong/Drouin-Chartier 2020)

## Original Quote
"consumption of at least one egg per day was not associated with incident cardiovascular disease risk after adjustment for updated lifestyle and dietary factors associated with egg intake"

## E-Prime Rewrite
Multivariable adjustment for lifestyle and dietary factors removed the association between daily egg consumption and incident CVD across 215,618 subjects, up to 32 years follow-up.

## Analysis
"Was not associated" sounds like a stable property of eggs. The forced rewrite must name what *produced* the null result — adjustment — surfacing that this finding is conditional on a specific covariate model, not source-independent.

This matters directly for [[eggs-001]]: the two studies don't disagree about a raw fact, they disagree about which covariates belong in the model. If BMI and statin use sit downstream of egg consumption (mediators), adjusting for them removes part of the true causal pathway along with the confounding — which would make this null result an artifact of over-adjustment, not evidence of safety.

## Ambiguity Flags
- Source doesn't fully specify which covariates carried the adjustment weight, or whether the authors treated BMI/statin-use as confounders or mediators — this is the open methodological crux.

## Adversarial Interpretation
A source motivated to find eggs safe could select an adjustment model that systematically removes the true signal by treating mediators as confounders. Nothing in this abstract rules that out.

## Related Claims
- [[eggs-001]] — the pooled meta-analysis this result contests
- [[eggs-003]] — PREDIMED's diabetic-subgroup analysis, partially reconciling the disagreement
