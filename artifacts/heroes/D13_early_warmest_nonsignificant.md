# Candidate D13 · Pre-1850 uncertainty makes most early "warmest-year" titles non-significant

**Claim (registered BEFORE computing any answer).** Because `AverageTemperatureUncertainty` is ~±2.6 °C before 1850, a large fraction of apparent 19th-century "warmest-year-for-country-X" titles do NOT survive an uncertainty-overlap test against the runner-up — early record-warm years are statistically indistinguishable from their neighbors.

## Registered prior (written before looking)
Pre-1850 signal-to-noise is ~1 (uncertainty ≈ interannual swing), so I expect **>50%** of pre-1850 "warmest-year" titles to be **non-significant** under an uncertainty-overlap test. If a large fraction ARE significant, that is surprising (uncertainty smaller than expected). Confidence: **medium-high**.

## Why surprising if outside the prior
Either direction is informative: if early titles are mostly non-significant, the "X was the warmest year on record in 18xx" framing is statistically hollow; if many ARE significant, the early uncertainty is less crippling than the headline ±2.6 °C suggests. Either way it quantifies how much the measurement-error regime eats early record claims — a HONEST-axis contribution.

## Feasibility (from input shape only)
ByCountry has annual max temperature + uncertainty per country-month. Per country: find argmax year (pre-1850 window); test whether its ±u CI overlaps the runner-up's ±u CI. Feasible: **HIGH**.

## Novelty
Unsearched at this specificity.

## Evidence plan (for the experiment layer, NOT executed here)
- Per country, pre-1850: candidate warmest year (max monthly or annual mean) with ±u; runner-up; overlap test.
- Metric: fraction of (country, pre-1850) "warmest-year" titles that are non-significant; distribution across countries.
- HONEST: define "warmest year" up front (annual mean vs max-month — pick one, report both as sensitivity); report how the fraction changes with the endpoint and with the window (pre-1850 vs pre-1900); separate exploration (definition choice) from confirmation.
- Verdict: GREEN if the non-significance fraction is large AND robust to definition; the prior is on the *fraction*, so SURPRISING is judged by observed-fraction vs the >50% prediction.

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
