# Candidate A3 · Longest "continuous" single-city series ≪ its date span

**Claim (registered BEFORE computing any answer).** The city with the earliest first reading (Århus, Denmark, 1743) is NOT actually continuous: multi-year NaN gaps mean its longest *uninterrupted* monthly run begins decades later than 1743, and the city holding the true "longest continuous series" may be different from the one with the earliest first reading.

## Registered prior (written before looking)
Early instrumental records are gappy → I expect the longest truly-continuous (no-NaN) monthly run across all cities to **begin around 1800–1850**, not 1743. Confidence: **medium**.

## Why surprising if outside the prior
If the longest continuous run reaches back to ~1750 uninterrupted (surprisingly complete early network) OR only begins post-1900 (surprisingly gappy), the truth lies outside my 1800–1850 expectation — and the common shorthand "longest record = earliest start" is shown to be wrong either way.

## Feasibility (from input shape only)
`GlobalLandTemperaturesByCity.csv` has `dt, AverageTemperature, City, Country, Latitude, Longitude`. Per-city max consecutive non-null months is a pure coverage/continuity computation (no temperature values used). ~3,448 cities; CPU-OK grouping one city at a time. Feasible: **HIGH**. Definition must be fixed up front: "uninterrupted" = consecutive monthly rows with non-null `AverageTemperature` AND non-null `AverageTemperatureUncertainty`.

## Novelty
Not findable as a table-specific claim in public sources; appears unsearched.

## Evidence plan (for the experiment layer, NOT executed here)
- For each city: max-run of consecutive non-null months; record start date and length.
- Rank cities by run length; compare to rank by earliest first-reading.
- HONEST: report the gap structure of Århus; report how many "early" cities are dominated by early NaN stretches; sensitivity to the "uninterrupted" definition (allow vs disallow single-month gaps).
- Verdict: GREEN if the longest-continuous city ≠ earliest-start city, or if Århus's continuous run starts ≫1743.

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
