# Candidate D11 · Uncertainty-weighting flips the warmest-decade ranking for ≥N countries

**Claim (registered BEFORE computing any answer).** For at least one (and plausibly several) country, weighting each monthly reading by 1/uncertainty² changes which decade ranks as "warmest," because early high-uncertainty readings pull the unweighted ranking — the ~30× collapse in `AverageTemperatureUncertainty` across the record is **consequential for rankings, not decorative**.

## Registered prior (written before looking)
The warming trend is large relative to early uncertainty for most countries, so I expect uncertainty-weighting to **barely move decade rankings**; I predict **<2 countries** flip their warmest decade. If **≥5 countries** flip, that is outside the prior. Confidence: **medium**.

## Why surprising if outside the prior
It would show that the headline "warmest decade" titles — the currency of climate communication — are partially an artifact of how you weight noisy early data, not just the physics. A reader trusting unweighted rankings would be quietly wrong for those countries.

## Feasibility (from input shape only)
ByCountry has `AverageTemperature` + `AverageTemperatureUncertainty` + `dt`. Decadal mean weighted by Σ(1/u²)·T / Σ(1/u²) vs unweighted mean; compare each country's argmax decade. ~577k rows, per-country. Feasible: **HIGH**. (Foundation seam: uncertainty-weighted vs unweighted decade rankings.)

## Novelty
Unsearched at this specificity ("uncertainty weighting changes warmest decade ranking" → no relevant hit).

## Evidence plan (for the experiment layer, NOT executed here)
- Per country: unweighted decadal mean vs 1/u²-weighted decadal mean; argmax decade under each.
- Metric: # countries whose argmax decade differs; magnitude of the rank change.
- HONEST: report both endpoints (country table ends 2013-09); restrict to countries with enough pre/post data; report the uncertainty regime of flippers (are they pre-1850-dominated?); bootstrap the decadal means to show whether the flip is within noise (a flip within noise is RED, not GREEN).
- Verdict: GREEN if ≥1 country flips *outside* the bootstrap noise; REFUTED if rankings are robust to weighting (still valuable: "uncertainty doesn't move rankings here").

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
