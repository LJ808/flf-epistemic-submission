---
claim_id: blackhole-002
case: black-holes
subtopic: evaporation-argument
source_ref: "[[cern-official-faq]]"
confidence_score: 3
rewrite_confidence: medium
methodology: theoretical_self_consistency_argument
relation_type: crux_candidate
tags: [resilience]
---
# LHC safety — black hole evaporation argument (CERN FAQ)

## Ingestion Layer
*Mechanical pass. No interpretation below this point — only the source quote and its forced E-Prime rewrite.*

### Original Quote
"All these theories predict that these particles would disintegrate immediately. Black holes, therefore, would have no time to start accreting matter and to cause macroscopic effects."

### E-Prime Rewrite
The same extra-dimension theoretical framework predicting microscopic black hole formation also predicts Hawking-radiation evaporation on a sub-accretion timescale.

## Assessment Layer
*Checkable pass, run against the ingestion output above. See [[two-layer-architecture-v1]] for the assessment criteria each subsection below must satisfy.*

### Analysis
"Would disintegrate immediately" reads as an independent safety check — a second line of defense if black hole formation somehow occurred. The forced rewrite exposes that formation and evaporation predictions come from the *same theoretical package*, not from two independent facts. A flaw in the extra-dimension theory threatens both predictions simultaneously; this functions as one safety net, not two.

Tracing this further: CERN's actual fuller safety case (LSAG 2008, referenced but not ingested here) supplements this internal-consistency argument with an independent astrophysical-observation check (neutron stars, white dwarfs persisting despite comparable cosmic-ray bombardment). On reflection, the safety-relevant weight likely sits with that independent check, not with the same-theory argument presented in this FAQ excerpt. **This shows the predicted "scope-dependency" resolving into a chain-dependency on closer inspection** — exactly the refinement flagged as a real, falsifiable open question in [[insight-contribution-v1]], not retrofitted after the fact.

### Ambiguity Flags
- FAQ presents formation-prediction and evaporation-prediction as if independently corroborating; they share a theoretical source. Resolving which argument actually carries the safety-relevant weight requires ingesting the LSAG 2008 report directly — not yet done in this vault.

### Adversarial Interpretation
A skeptical reader could note that if the extra-dimension theory turns out wrong about evaporation while remaining right about formation, the FAQ's safety argument collapses. Whether CERN's fuller safety case closes this gap independently remains untested here.

## Related Claims
- [[blackhole-001]] — addresses the formation-energy-regime question; together the two claims cover formation and evaporation, but neither alone constitutes the full safety argument CERN's official position rests on
