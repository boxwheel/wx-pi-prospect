# Candidate A1 · Continent pseudo-entries ≠ member-country rollup

**Claim (registered BEFORE computing any answer).** The `Africa`/`Asia`/`Europe`/`North America`/`South America` series in `GlobalLandTemperaturesByCountry.csv` diverge systematically from an area- or equal-weighted mean of their actual member-country series — Berkeley Earth's continent fields are an undocumented aggregation that does not reproduce member averaging.

## Registered prior (written before looking at any temperature value)
I expect the continent series to closely match an area-weighted mean of their member countries (same underlying gridded data re-aggregated), so divergence is **small — within the member countries' own uncertainty**. Confidence: **medium**.

## Why surprising if outside the prior
If the divergence is systematic and *larger* than the members' own uncertainty, the continent field is a distinct construct, not a rollup — a data-construction oddity invisible without checking. A reader who assumed "Europe = average of European countries" would be silently wrong.

## Feasibility (from input shape only)
ByCountry has 6 continent pseudo-entries (`Africa, Asia, Europe, North America, South America, Antarctica`) plus 243 real countries, all sharing the monthly `dt` axis. Inner-join per month; weight members by member-count or a proxy area. No statistic computed yet. Feasible: **HIGH**.

## Novelty
Wikipedia/limited-web search for "Berkeley Earth continent field aggregation" → no relevant hit. Table-specific construction oddity; appears unsearched. (Well-known that continents are aggregations; NOT known whether this table's continent field reproduces member averaging.)

## Evidence plan (for the experiment layer, NOT executed here)
- Build area-weighted member rollup for each continent-month; compare to the table's continent series.
- Metric: mean |Δ|, fraction of months where |Δ| > member mean uncertainty, and the temporal/spatial pattern of Δ.
- HONEST controls: report both equal-weight and area-proxy-weight; report which countries are excluded/zero-reading; note Antarctica is near-empty.
- Verdict scale: GREEN if divergence systematic & > uncertainty; RED if within uncertainty (still a recorded finding: "continent field ≈ rollup").

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
