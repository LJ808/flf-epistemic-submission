---
claim_id: eggs-001
case: eggs-health
subtopic: cvd-risk
source_ref: "[[li-2013-meta-analysis]]"
confidence_score: 4
rewrite_confidence: high
methodology: pooled_observational_meta_analysis
relation_type: contested_by
tags: [resilience]
---
# Egg intake and CVD risk — pooled meta-analysis (Li 2013)

## Ingestion Layer
*Mechanical pass. No interpretation below this point — only the source quote and its forced E-Prime rewrite.*

### Original Quote
"there is a dose-response positive association between egg consumption and the risk of CVD and diabetes"

### E-Prime Rewrite
Egg intake correlates with CVD risk at RR 1.19 (CI 1.02–1.38) and diabetes at RR 1.68 (CI 1.41–2.00), pooled across 14 studies, n=320,778.

## Assessment Layer
*Checkable pass, run against the ingestion output above. See [[two-layer-architecture-v1]] for the assessment criteria each subsection below must satisfy.*

### Analysis
The rewrite forces a number into a sentence that originally needed none. "There is an association" cannot survive E-Prime without specifying *what the association consists of* — direction, magnitude, and confidence interval become mandatory rather than optional once "is" disappears.

What this claim entails: a positive correlation across the pooled sample. What would falsify it: a properly powered cohort with covariate adjustment producing a null or reversed estimate — exactly what [[eggs-002]] reports.

### Ambiguity Flags
- "Association" leaves causal direction unaddressed — neither the source nor the rewrite resolves whether this reflects egg consumption causing CVD or some shared upstream factor.

### Adversarial Interpretation
A reader motivated to dismiss this finding could note the pooled analysis doesn't control for the same covariates as [[eggs-002]], making the comparison incomplete rather than contradictory. A reader motivated to accept it could ignore that the "dose-response" framing in the conclusion oversells what a single highest-vs-lowest comparison actually shows.

## Related Claims
- [[eggs-002]] — directly contests this finding using covariate-adjusted cohort design
- [[eggs-003]] — addresses whether the diabetes-specific signal here generalizes
