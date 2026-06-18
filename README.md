# FLF Epistemic Case Study Submission
## E-Prime as Structural Epistemic Enforcement

**Case studies:** Eggs/CVD/Diabetes · COVID Origins · Black Holes/LHC Safety
**Core contribution:** E-Prime as a detection-and-disclosure mechanism for evaluative-language smuggling, tested for both reader-side misreading and source-side gaming across three structurally different epistemic domains.

---

## Quick start (try the code in under a minute)

```
cd flf-vault
pip install -r requirements.txt
python3 ingest.py --demo
```

No API key needed for `--demo`. With a key set (`export ANTHROPIC_API_KEY=...`), run `python3 ingest.py "your claim here"` to ingest a new source live.

---

## Where to Start

### For judges with 15 minutes
1. Read [`INDEX.md`](flf-vault/INDEX.md) — overview of the nine claims and the vault structure
2. Pick one case and read 1–2 claim files to see the before/after E-Prime rewrite
3. Skim [`adversarial-robustness-criterion-6.md`](flf-vault/SYNTHESIS/adversarial-robustness-criterion-6.md) — Part C gives the honest, non-inflated summary

### For judges with 45 minutes
1. Read one claim from each case (e.g., `eggs-001.md`, `covid-001.md`, `blackhole-001.md`)
2. Open the Obsidian vault and follow the wiki-links to see real cross-claim relationships
3. Read [`crux-analysis-v1.md`](flf-vault/SYNTHESIS/crux-analysis-v1.md) — real crux ranking across all nine claims

### For judges who want to run it
1. `pip install -r requirements.txt && python3 ingest.py --demo`
2. With your own API key, run `ingest.py` on a new source in your own domain
3. Compare the structural pattern against the worked examples in `adversarial-robustness-criterion-6.md`'s Extension Protocol

---

## Submission Structure

```
flf-vault/
├── INDEX.md
├── ingest.py                                  ← Minimal prototype (one-click demo)
├── requirements.txt
├── CLAIMS/
│   ├── eggs-cvd-diabetes/{eggs-001,002,003}.md
│   ├── covid-origins/{covid-001,002,003}.md
│   └── black-holes/{blackhole-001,002}.md
├── SOURCES/  (six source files)
└── SYNTHESIS/
    ├── crux-analysis-v1.md
    ├── scalability-test-v1.md
    ├── per-claim-attack-vector-breakdown.md         ← Part A detail, all nine claims
    └── adversarial-robustness-criterion-6.md  ← Criterion 6, both clauses tested
```

---

## The Core Claim, Stated Honestly

**E-Prime ingestion makes evaluative-language smuggling structurally visible — it does not make misreading or source gaming impossible.**

Standard-summary language ("is," "seems," "means," "no evidence of") permits the actual epistemic work — confounding decisions, statistical power, theory-choice, source incentive — to collapse invisibly into a confident-sounding sentence. E-Prime forces that work into view. A motivated reader or a motivated source can still attempt to mislead; the difference is that doing so now requires adding visible language or leaving a visible gap, rather than hiding inside a verb.

This submission tested that claim against ten reader-side attack classes across all nine claims, and three source-side gaming scenarios (cohort selection, rhetorical engineering, institutional hedge-then-reassure) across all three cases. Results, including the places where the method does *not* fully hold, are in `adversarial-robustness-criterion-6.md`.

---

## Honest Gaps (Stated, Not Hidden)

- **Secondary/tertiary sources throughout.** All three cases ingested a meta-analysis abstract, a journalist's debate writeup, or an institutional FAQ — not primary data, full transcripts, or the full LSAG 2008 safety report. This is a build-scope limitation, not a method limitation.
- **Cross-document source-gaming untested.** Criterion 6 testing shows E-Prime defeats false-independence framing *within* a document (blackhole-002) but cannot, on its own, catch selective omission *across* documents the vault never ingested (the public FAQ vs. the fuller LSAG report).
- **Three open cruxes, not resolved:** whether PREDIMED's null interaction reflects true absence or underpowering (eggs-003); whether post-2019 computational tractability says anything about pre-2019 engineering knowability (covid-003); which CERN safety argument actually carries the weight (blackhole-002). These are named as the vault's real, current open questions — not papered over.
- **Judgment-scales-with-compute claim:** drafted during the scalability test, caught as unexecuted before shipping, corrected to state the gap honestly.

---

## Submission Contact

James Greathouse — james@senecacommons.com
Early-feedback check-in: June 21, 2026 (optional, per competition rules)
Main deadline: July 19, 2026
