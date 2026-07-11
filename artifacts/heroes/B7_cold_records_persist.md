# Candidate B7 · New monthly COLD records for individual stations still occur into the 2000s–2010s

**Claim (registered BEFORE computing any answer).** Even as warm records accelerate, new "coldest-on-record-for-that-calendar-month" events for individual countries/cities continue to appear into the 2000s–2010s — the cold-record "last occurrence" is far more recent than the "everything is hottest now" intuition, and the warm/cold record asymmetry is less extreme than commonly assumed.

## Registered prior (written before looking)
Warming should suppress new monthly cold records, so I expect the **last new global cold record to fall before ~2000**. If cold records persist into the 2010s for a **non-trivial share** of stations, that is outside the prior. Confidence: **medium**.

## Why surprising if outside the prior
It complicates the "everything is record-hot, cold is gone" framing: new cold records are still being set at the station level even in the warmest decade. The asymmetry of the record-breaking process is the finding, not the mean trend.

## Feasibility (from input shape only)
ByCountry / ByCity have per-country/city monthly readings over the full dt range. Track, per (station, calendar-month), the running minimum and count the year of the last new minimum. Feasible: **HIGH**. Must fix: "record" = strictly lower than all prior same-calendar-month readings for that station; count the year of the last new record per station; report the share of stations whose last cold record is post-2005.

## Novelty
Wikipedia search returns only generic "List of weather records"; the country-level "monthly cold records still set in the 2010s" claim appears unsearched. NOVEL-ish.

## Evidence plan (for the experiment layer, NOT executed here)
- Per station × calendar month: running min; year of last new cold record; year of last new warm record.
- Metric: share of stations with last-cold-record year ≥ 2005; distribution of last-cold-record years vs last-warm-record years; the warm/cold "last record" asymmetry.
- HONEST: report station counts and the share (denominator matters); control for series length (a short series sets records easily late — restrict to stations with ≥N decades of coverage); report the same on the daily-city dataset as a cross-check; separate exploration (pick the threshold/year) from confirmation on a held-out set.
- Verdict: GREEN if a non-trivial share of well-covered stations set new cold records after 2005; REFUTED if cold records essentially stopped by ~2000 (still valuable: "cold records did stop").

## Verdict pending
NOT EXECUTED (prospect layer — generation only).
