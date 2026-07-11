# Candidate J26 · Anomaly-distribution skewness changed sign over the record

**Claim (registered BEFORE computing any answer).** The distribution of monthly temperature anomalies (vs each station's own month-of-year climatology) was **positively skewed in one era and symmetric or negatively skewed in another** — the *shape* of the anomaly distribution changed, not just its center.

## Registered prior (written before looking)
I expect anomalies to be **roughly symmetric (≈Gaussian) throughout**, merely shifted warmer over time. A **sign change in skewness** between eras for a non-trivial set of stations is outside the prior. Confidence: **medium**.

## Why surprising if outside the prior
A change in skewness means the tails behaved asymmetrically over time — e.g., the warm tail fattened while the cold tail thinned — a distributional change invisible to any mean/linear-trend analysis. It is a "shape of the record" fact.

## Feasibility (from input shape only)
Per station: anomaly = monthly T − station's month-of-year climatology (computed over a fixed baseline window). Skewness by era (e.g., early vs late half). Feasible (CPU, per-station). Feasible: **MED-HIGH**. Must fix the baseline window and the era split up front; report sensitivity.

## Novelty
Unsearched at this specificity. NOVEL-ish.

## Evidence plan (for the experiment layer, NOT executed here)
- Per station: anomalies vs a fixed 1961–1990 climatology; skewness in early (e.g., 1850–1960) vs late (e.g., 1961–2013) era; sign of skewness in each.
- Metric: #/share of stations whose skewness sign flips between eras; magnitude of the change with bootstrap CI.
- HONEST: report sensitivity to baseline window and era split; restrict to well-covered stations (full annual coverage in both eras); rule out that the flip is a coverage/station-composition artifact; separate exploration (era choice) from confirmation.
- Verdict: GREEN if a non-trivial share of stations show a sign flip outside noise; REFUTED if skewness is stable (still valuable).

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
