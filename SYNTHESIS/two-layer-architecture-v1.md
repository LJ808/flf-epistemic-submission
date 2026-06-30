---
title: Two-Layer Architecture
type: synthesis
status: active
vault: TRC
date: 2026-06-30
tags: [resilience]
---

# Ingestion Layer / Assessment Layer — Architecture and Criteria

## Why this file exists

Early-feedback review (Oly Sourbut, FLF, 2026-06-30) named a real structural gap in the original nine claim files: each one fused the mechanical E-Prime rewrite together with the nuance-restoration and ambiguity work in one continuous pass — "rhetoric linting," in his phrase, with no separable structure or checking step. This file names the fix and states the criteria the fix runs against, so the split counts as real architecture, not a relabeling.

## The two layers

**Ingestion Layer.** Takes a verbatim source quote and produces an E-Prime rewrite. Purely mechanical: no claim about what the rewrite means, no flagged ambiguity, no adversarial reading. Output stays checkable against one criterion only — does the rewrite eliminate every form of "to be" while preserving the source's actual content?

**Assessment Layer.** Takes an Ingestion Layer output as its only input and runs three checks against it. Each claim file's Assessment section now states these explicitly, so a reader other than the author can verify the assessment against the ingestion output without re-deriving it.

## Assessment-layer criteria

**Analysis** must name the specific word or phrase the E-Prime constraint forced out of the original sentence, then state what that word hid — a missing number, a missing mechanism, a missing direction of causation. A passing Analysis section names the hidden item explicitly; it doesn't just gesture at "more nuance."

**Ambiguity Flags** must state what neither the original source nor the rewrite resolves — not what the rewrite itself left unclear, but what gap survives the rewrite intact. A flag that the rewrite itself actually answers doesn't belong here.

**Adversarial Interpretation** must supply two readings, not one: how a reader motivated to dismiss the claim could misuse the rewrite, and how a reader motivated to accept it could misuse the rewrite. A one-sided adversarial section fails this criterion.

## What this buys

Splitting the layers turns "did the rhetoric-linting work happen correctly" from an unanswerable question (the original fused version asks a reader to evaluate one undifferentiated paragraph) into three answerable ones — does the Analysis name a specific hidden item, does each Ambiguity Flag survive the rewrite, does the Adversarial Interpretation cover both directions. Per-claim quality now resolves to checking eleven yes/no answers (three Assessment subsections × nine claims plus the Ingestion check), not one holistic judgment call.

This also confirms Oly's specific placement suggestion. The Assessment Layer, not the whole submission, constitutes the actual contribution under an epistack architecture that separates ingestion from assessment as named competition layers — the Ingestion Layer here functions as commodity infrastructure (any sufficiently careful E-Prime rewrite would do), while the checkable, criteria-bound restoration work in the Assessment Layer carries the submission's real claim.

## Mechanical enforcement, not just markdown headers

`ingest.py` now runs the two layers as two separate functions, callable independently — `ingest_claim()` returns only the Ingestion Layer output; `assess_claim()` takes that output as its required input and returns the Assessment Layer output, refusing to run without it. The CLI exposes `--ingest-only` to demonstrate the Ingestion Layer running alone. This makes the separation a property of the tool, not a documentation convention layered on top of a fused process.

## Applied to

All nine claim files (`CLAIMS/eggs-cvd-diabetes/eggs-{001,002,003}.md`, `CLAIMS/covid-origins/covid-{001,002,003}.md`, `CLAIMS/black-holes/blackhole-{001,002}.md`), 2026-06-30. `Related Claims` sections stay outside both layers — cross-reference metadata, not ingestion or assessment work.
