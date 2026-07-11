# Candidate D12 · Temperature *uncertainty* itself has a winter>summer seasonal pattern

**Claim (registered BEFORE computing any answer).** `AverageTemperatureUncertainty` is seasonally modulated — larger in winter than in summer for mid/high-latitude countries — a **non-climatic seasonality in the error bar itself**, driven by measurement conditions, not by temperature.

## Registered prior (written before looking)
Uncertainty is a station-network/coverage quantity, so I expect it to be **roughly seasonally flat** within a country. A strong, repeatable winter>summer (or summer>winter) uncertainty seasonality is outside the prior. Confidence: **medium**. (Genuinely uncertain about the sign — which is good for an honest test.)

## Why surprising if outside the prior
A seasonal *error bar* means the data are not equally informative year-round: confidence in a winter temperature is structurally weaker than in a summer one, a fact hidden in a column everyone treats as a constant. It is a measurement-process oddity — "records over headlines."

## Feasibility (from input shape only)
ByCountry has `AverageTemperatureUncertainty` + `dt` (month). Group uncertainty by calendar month, per country; test for a seasonal cycle. No temperature value needed. Feasible: **HIGH**.

## Novelty
Unsearched; a measurement-process oddity, squarely "records over headlines."

## Evidence plan (for the experiment layer, NOT executed here)
- Per country: mean uncertainty by calendar month; amplitude of the annual cycle (max−min month); sign (which season peaks).
- Metric: #/share of mid-high-latitude countries with a cycle amplitude > some fraction of the mean uncertainty; the modal peak season.
- HONEST: restrict to countries with full annual coverage (drop those missing whole seasons); report whether the cycle is an artifact of which stations report in which season (coverage seasonality) vs genuine per-reading uncertainty; bootstrap the amplitude.
- Verdict: GREEN if a repeatable seasonal cycle exists across many countries *after* controlling for coverage seasonality; REFUTED if uncertainty is seasonally flat.

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
