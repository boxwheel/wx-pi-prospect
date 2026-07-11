# Candidate J25 · Interannual temperature VARIANCE decreased for some regions while the mean rose

**Claim (registered BEFORE computing any answer).** For some countries/regions, the interannual variance of temperature **decreased** over the record even as the mean rose — so "more extreme / more variable weather" is not supported there; the distribution narrowed.

## Registered prior (written before looking)
The common framing is "more energy in the system → more variability," so I expect variance to **increase or stay flat** as the mean rises. A **decrease** in variance for a non-trivial set of regions is outside the prior. Confidence: **medium**.

## Why surprising if outside the prior
It would push back, with this table's own numbers, on "warming = more variable weather": for some regions the spread shrank while the center rose. The *shape* of the distribution changed, not just its center.

## Feasibility (from input shape only)
ByCountry (or ByCity) annual series → variance in early vs late windows per region. Feasible. The hard part is HONEST: a coverage/station-composition change can mimic a variance change, so the experiment must control for it (e.g., restrict to stations with stable coverage across both windows; use the uncertainty columns). Feasible: **MED-HIGH**.

## Novelty
"Global warming hiatus"/ENSO hits but not "interannual variance decreased in specific countries in this table"; appears unsearched. NOVEL-ish.

## Evidence plan (for the experiment layer, NOT executed here)
- Per region: annual mean (or monthly anomaly) series; early-window (e.g., 1900–1960) vs late-window (e.g., 1961–2013) variance; ratio; bootstrap CI on the ratio.
- Metric: #/share of regions with variance ratio < 1 (decrease) and CI excluding 1.
- HONEST: control for coverage drift (restrict to regions with stable station counts / low missingness in both windows); report the same on residuals after removing the mean trend; report whether the decrease survives using the uncertainty columns (weighted variance); separate exploration (window choice) from confirmation on a held-out window split.
- Verdict: GREEN if a non-trivial set of regions show a real variance decrease after controls; REFUTED if variance only rises/stays flat (still valuable).

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
