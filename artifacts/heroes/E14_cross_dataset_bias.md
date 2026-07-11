# Candidate E14 · Berkeley-monthly vs daily-city disagree with a latitude-dependent bias

**Claim (registered BEFORE computing any answer).** Aggregating the daily-city dataset (`city_temperature.csv`, °F) to monthly means and converting to °C, the per-city monthly mean differs from Berkeley Earth `GlobalLandTemperaturesByMajorCity.csv` by a systematic offset that **varies with latitude** (or climate zone) — a cross-dataset bias that is NOT a constant calibration offset.

## Registered prior (written before looking)
The two datasets measure the same cities in the same overlap window (1995–2013), so I expect them to **agree within ~1 °C with a roughly constant offset** (a fixed unit/calibration difference). A latitude-dependent (non-constant, sloping) bias is outside the prior. Confidence: **medium**.

## Why surprising if outside the prior
A latitude-correlated bias means the two datasets disagree in a structured way about *where* it is warmer — "which city is warmer" can flip by latitude band. A reader cross-checking datasets would assume a flat offset; a slope would be a real consistency problem.

## Feasibility (from input shape only)
Overlap window: Berkeley major-city monthly ends 2013-09; daily covers 1995–2020. Both have city + country names (need canonical/fuzzy city-name matching; daily has `Region, Country, State, City`, Berkeley has `City, Country, Latitude, Longitude`). Daily is in °F (convert), has −99 sentinels (drop) and Year=200/Day=0 corrupt rows (drop). Berkeley has °C. Feasible; the city-name join is the main work. Feasible: **MED-HIGH**. (Foundation seam: cross-dataset consistency.)

## Novelty
Wikipedia search for "Berkeley Earth versus daily city temperature comparison" → no relevant hit. Appears unsearched. NOVEL.

## Evidence plan (for the experiment layer, NOT executed here)
- Match cities (canonical name + country); aggregate daily→monthly; convert °F→°C; align on (city, year, month).
- Metric: per-city mean Δ = daily_monthly_C − Berkeley_monthly_C; regress Δ on |latitude|; test slope ≠ 0 (bootstrap CI on slope).
- HONEST: report the city-match yield (# matched / # possible), the sentinel/corrupt-row drop rate per city, and BOTH the warmest-city and coldest-city rank under each dataset (does ranking flip?). Separate exploration (pick the latitude model) from confirmation (test slope on a held-out subset of cities).
- Verdict: GREEN if slope ≠ 0 with CI excluding 0; RED if flat offset (still a recorded finding: datasets agree within a constant).

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
