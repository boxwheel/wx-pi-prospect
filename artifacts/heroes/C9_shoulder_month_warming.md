# Candidate C9 · For ≥1 major country, the fastest-warming month is a shoulder month, not winter

**Claim (registered BEFORE computing any answer).** For at least one large mid-latitude country, the calendar month with the largest century-scale warming is a **shoulder month (spring or autumn), not the coldest winter month** — contradicting the generic "winters warm fastest" headline for that region.

## Registered prior (written before looking)
"Winters warm fastest" is the common-knowledge framing (Foundation NO-GO), so I expect **December–February (NH) to show the largest century warming** for mid-latitude countries. If a shoulder or summer month beats winter for a **major** country, that is outside the prior. Confidence: **medium-high**.

## Why surprising if outside the prior
It would localize, in this table, a *refutation* of a NO-GO headline: the seasonal *phase* of warming is not universally winter-peaked. The common statement "winters warm fastest" is true on average but not country-by-country; finding where it breaks is the discovery.

## Feasibility (from input shape only)
ByCountry has monthly `AverageTemperature` + `dt` per country. Per country: OLS trend (or early-vs-late mean) per calendar month; rank months by warming. Feasible: **HIGH**. Must fix: "largest warming" = largest slope of monthly anomaly vs year, over a stated window (e.g., 1900–2013 to avoid the sparsest pre-1850 data); report sensitivity to the window.

## Novelty
Seasonal warming asymmetry is studied in climate science, so NOVEL is **down-weighted**; the table-specific "shoulder beats winter for country X in Berkeley Earth country table" appears unsearched. The SURPRISING axis (refuting a NO-GO headline at this scale) is the value.

## Evidence plan (for the experiment layer, NOT executed here)
- Per country: per-calendar-month warming slope (1900–2013); argmax month; classify month as winter/shoulder/summer by hemisphere.
- Metric: list of countries whose argmax-warming month is a shoulder or summer month; the margin over the winter month.
- HONEST: report the slope CIs (uncertainty columns / bootstrap); report sensitivity to the window (1850–2013, 1900–2013, 1950–2013); restrict to well-covered countries; don't cherry-pick — report ALL major countries' argmax month, then note which (if any) refute the prior.
- Verdict: GREEN if ≥1 *major* country's argmax month is a shoulder/summer month with a margin exceeding its noise; REFUTED if winter peaks everywhere (still valuable: "winters do peak everywhere here").

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
