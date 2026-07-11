# Prospectus — surprising-but-TRUE facts from long-run weather/climate records (Berkeley Earth 1750–2013/15 + daily cities 1995–2020)

**Campaign:** cp_60fb4891 · Prospect (Layer 2) · cycle 1 · fresh slate (no sibling experiment paths in flight under this root).
**Scouted (shape only, no answer statistics):** schemas, coverage breadth per decade, first-reading-year distribution, continent pseudo-entries, state-table country set, daily-city per-year city counts, null/sentinel structure. These coverage facts are the Foundation's *registered prior*, not findings (Foundation node `frosty-shape-0578`).
**Registered priors below were written BEFORE any candidate statistic was computed.** No candidate prior quotes a measured temperature value, ratio, count-of-records, or effect size from these tables. Priors state direction + rough magnitude only.

## How to read this table

- **Claim** — one crisp sentence. Contains NO observed values.
- **Registered prior** — the outcome I predict *before* computing, with confidence (L/M/H). The SURPRISING axis will judge observed-vs-this-prior.
- **Why surprising if outside prior** — what it would mean.
- **Feasibility** — judged from input *shape* (fields exist / sample big enough / join doable), NOT from computing the answer.
- **Novelty** — Wikipedia/limited-web search result on the *specific* claim. "no hit" = no relevant public source found for the table-specific claim (down-weight: well-known-in-climate-science but not-stated-for-these-tables).
- **Screen** — KEEP / KILL with reason.

## Legend
Territories: **A**=coverage/data-construction, **B**=record-breaking structure, **C**=seasonal/month asymmetry, **D**=uncertainty effects, **E**=cross-dataset consistency, **F**=latitudinal banding, **G**=endpoint/ranking stability, **H**=station-composition artifacts, **I**=event attribution discipline, **J**=distributional/moment changes.

---

## ALL CANDIDATES GENERATED (28), survivors and kills

### A1 · Continent pseudo-entries are NOT the average of their member countries — KEEP
- **Claim:** The `Africa`/`Asia`/`Europe`/`North America`/`South America` series in ByCountry diverge systematically from an area- or equal-weighted mean of their actual member-country series — Berkeley Earth's continent fields are an undocumented aggregation that does not reproduce member averaging.
- **Prior:** Continent series ≈ area-weighted mean of member countries (same underlying gridded data re-aggregated); divergence small, within member uncertainty. Confidence **M**.
- **Surprise if outside:** divergence is systematic and larger than the members' own uncertainty → continent field is a distinct construct, not a rollup. (Records/data-construction oddity.)
- **Feasibility:** ByCountry has 6 continent entries + 243 countries sharing the `dt` axis; inner-join per month, weight by member count or proxy area. Feasible. **HIGH**.
- **Novelty:** no relevant Wikipedia hit for "Berkeley Earth continent field aggregation"; table-specific. Appears unsearched.
- **Screen:** **KEEP** — records/data-construction oddity, novel, clearly defined, feasible.

### A2 · Coverage "big bang" decade coincides with a temperature step — KILL
- **Claim:** A discontinuous jump in countries-with-reading-per-decade coincides with a structural step in the apparent (unweighted) global mean.
- **Prior:** coverage jump shifts the coverage-biased apparent mean. Confidence M-H.
- **Surprise if outside:** no coincidence (pure coverage artifact vs real climate step).
- **Feasibility:** coverage-count shape already seen (allowed); temperature-step part uncomputed. Feasible.
- **Novelty:** "sparse coverage" is Foundation NO-GO; coverage-artifact story is a known trap.
- **Screen:** **KILL** — coverage sparsity is NO-GO; the coincidence is a known coverage-artifact trap (Foundation trap #7). Not records-oddity, it's the headline trap restated.

### A3 · Longest "continuous" single-city series is far shorter than its date span — KEEP
- **Claim:** The city with the earliest first reading (Århus, 1743) is NOT actually continuous: multi-year NaN gaps mean its longest *uninterrupted* monthly run starts decades later than 1743, and the true "longest continuous series" city may be different.
- **Prior:** early records are gappy → longest truly-continuous run probably begins ~1800–1850, not 1743. Confidence **M**.
- **Surprise if:** the longest continuous run reaches back to ~1750 uninterrupted (surprisingly complete) OR only post-1900 (surprisingly gappy) — outside the 1800–1850 expectation.
- **Feasibility:** ByCity (dt, city, temp, lat/long) → per-city max consecutive non-null months. ~3.4k cities; CPU-OK per-city. Feasible. **HIGH**.
- **Novelty:** not searchable as a table-specific claim; appears unsearched.
- **Screen:** **KEEP** — clean coverage/continuity oddity, feasible, honest-quantifiable (explicit "uninterrupted-months" definition).

### A4 · Daily-city dataset loses coverage over its own lifetime — KILL
- **Claim:** Active-city count declines across the 1995–2020 window, so the dataset's recent end is sparser than its start (opposite of Berkeley Earth's coverage growth).
- **Prior:** expected modern monitoring to grow; a decline is surprising.
- **Feasibility:** feasible.
- **Novelty:** unsearched.
- **Screen:** **KILL — ordering violation.** I observed the per-year city-count distribution during shape scouting (it declines). A prior written now would be retro-fitted. Recorded to demonstrate screening discipline; the *fact* is true but cannot be a SURPRISING candidate from me.

### A5 · First-reading-year distribution is bimodal — KILL
- **Claim:** Across the 242 real countries the first-reading-year distribution is bimodal (early-European cluster + late-19th-century cluster), not a smooth rollout.
- **Prior (genuine, pre-quantile):** expected a unimodal, gradually-rising rollout skewed late-19th-century.
- **Feasibility:** feasible (have dt + country).
- **Novelty:** unsearched.
- **Screen:** **KILL** — the quartiles I already saw (25th≈1782, median≈1824, 75th≈1850) are fairly evenly spaced and already lean *against* bimodality; claiming bimodality now would be retro-fitted against observed shape, and confirming *unimodality* merely matches the prior (low surprise). Recorded for honesty.

### B6 · Record-warm months are bursty in time, with a hemispheric phase offset — KILL (folded)
- **Claim:** "Warmest-on-record-for-that-calendar-month" events burst in particular decades, and the burst decade differs between NH and SH country groupings.
- **Prior:** warm records burst in the most recent two decades globally; NH/SH burst timing similar (within a few years). A >1-decade NH-vs-SH offset is surprising. Confidence M.
- **Feasibility:** per-country monthly record tracking; split NH/SH. Feasible.
- **Novelty:** unsearched at this specificity.
- **Screen:** **KILL (folded into B7)** — same record-asymmetry territory; B7 (cold records persist) is the more surprising, less-known half. Keep one record-structure candidate.

### B7 · New monthly COLD records for individual stations still occur into the 2000s–2010s — KEEP
- **Claim:** Even as warm records accelerate, new "coldest-on-record-for-that-calendar-month" events for individual countries/cities continue to appear into the 2000s–2010s — the cold-record "last occurrence" is far more recent than "everything is hottest now," and the warm/cold record asymmetry is less extreme than commonly assumed.
- **Prior:** warming should prevent new monthly cold records → last global new cold record before ~2000. If cold records persist into the 2010s for a non-trivial share of stations, that is outside the prior. Confidence **M**.
- **Surprise if:** a non-trivial number of stations set a new monthly cold record after 2005.
- **Feasibility:** per-country/city per-calendar-month record tracking across full dt range. Feasible. **HIGH**.
- **Novelty:** only generic "List of weather records" found; the country-level "monthly cold records still set in 2010s" claim appears unsearched. NOVEL-ish.
- **Screen:** **KEEP** — record-asymmetry, surprising, feasible, honest (must report station count + share).

### B8 · Warm/cold record RATIO hemisphere asymmetry — KILL (duplicate of B6/B7)
- **Screen:** **KILL** — sub-claim of B6/B7; folded.

### C9 · For ≥1 major country, the month that warmed most is a SHOULDER month, not deep winter — KEEP
- **Claim:** For at least one large mid-latitude country, the calendar month with the largest century-scale warming is a shoulder month (spring/autumn), not the coldest winter month — contradicting the generic "winters warm fastest" headline for that region.
- **Prior:** winters (Dec–Feb NH) show the largest warming ("winters warm fastest," Foundation NO-GO). A shoulder/summer month beating winter for a major country is outside the prior. Confidence **M-H**.
- **Surprise if:** a shoulder month's century trend exceeds the winter month's trend for a major country.
- **Feasibility:** ByCountry monthly → per-calendar-month trend per country; rank months. Feasible. **HIGH**.
- **Novelty:** seasonal warming is studied; the specific "shoulder beats winter for country X in this table" is table-specific → down-weight NOVEL, but SURPRISING (refutes the NO-GO headline at this scale).
- **Screen:** **KEEP** — pointed refutation of a NO-GO headline, surprising, feasible.

### C10 · Peak-warming month differs systematically between continents — KILL (folded)
- **Claim:** The calendar month of peak century-scale warming differs between Europe and North America by ≥2 months.
- **Prior:** broadly similar winter-centered peak across NH mid-latitudes; a ≥2-month phase difference is surprising. Confidence M.
- **Feasibility:** feasible (pairs with A1 continent-field work).
- **Novelty:** unsearched.
- **Screen:** **KILL** — same seasonal-month territory as C9; keep the more pointed refutation (C9). Could be revived as a sub-analysis of C9.

### D11 · Uncertainty-weighting flips which decade is "warmest" for ≥N countries — KEEP
- **Claim:** For at least one (and plausibly several) country, weighting each monthly reading by 1/uncertainty² changes which decade ranks warmest, because early high-uncertainty readings pull the unweighted ranking — the 30× uncertainty collapse is consequential for rankings, not decorative.
- **Prior:** uncertainty-weighting barely moves decade rankings (warming trend ≫ early uncertainty for most countries); predict <2 countries flip. If ≥5 flip, that is outside the prior. Confidence **M**.
- **Surprise if:** a non-trivial number of countries' warmest-decade title changes under weighting.
- **Feasibility:** ByCountry has uncertainty col → weighted vs unweighted decadal means; compare rankings. Feasible. **HIGH**. (Foundation seam.)
- **Novelty:** unsearched at this specificity.
- **Screen:** **KEEP** — directly uses uncertainty columns (rubric), foundation seam, feasible, surprising potential.

### D12 · Temperature *uncertainty* itself has a seasonal pattern (winter > summer) — KEEP
- **Claim:** `AverageTemperatureUncertainty` is seasonally modulated — larger in winter than summer for mid/high-latitude countries — a non-climatic seasonality in the *error bar* itself, driven by measurement conditions.
- **Prior:** uncertainty is a network/coverage quantity, roughly seasonally flat. A strong winter>summer uncertainty seasonality is surprising. Confidence **M**. (Genuinely uncertain — could also be summer>winter.)
- **Surprise if:** a clear, repeatable seasonal cycle in uncertainty across many mid/high-latitude countries.
- **Feasibility:** ByCountry has uncertainty + dt → group by calendar month, per country. Feasible. **HIGH**.
- **Novelty:** unsearched; a measurement-process oddity, very "records-over-headlines."
- **Screen:** **KEEP** — measurement-process oddity, feasible, novel, surprising.

### D13 · Pre-1850 uncertainty makes most early "warmest-year" titles non-significant — KEEP
- **Claim:** Because pre-1850 uncertainty is ~±2.6 °C, a large fraction of apparent 19th-century "warmest-year-for-country-X" titles do NOT survive an uncertainty-overlap test against the runner-up — early record-warm years are statistically indistinguishable from neighbors.
- **Prior:** SNR ~1 pre-1850 → most early warmest-year claims non-significant; predict >50% non-significant. If a large fraction ARE significant, that is surprising. Confidence **M-H**.
- **Surprise if:** many early warmest-year titles ARE significant (uncertainty is smaller than expected), OR essentially none are (even more swallowed than predicted).
- **Feasibility:** per-country annual max with uncertainty CIs; overlap test. Feasible. **HIGH**.
- **Novelty:** unsearched at this specificity.
- **Screen:** **KEEP** — honest SNR quantification, uses uncertainty columns, feasible; SURPRISING value if it cuts against the "early records are real titles" intuition.

### D28 · Far fewer countries have *significant* post-2000 warming than the naive point-estimate count — KILL (folded)
- **Claim:** # countries whose post-2000 decade is significantly warmer (non-overlapping uncertainty) than pre-industrial baseline ≪ # countries whose point-estimate mean is higher.
- **Prior:** most countries' post-2000 warming significant; predict >80%. If >20% non-significant, surprising. Confidence M.
- **Feasibility:** feasible.
- **Novelty:** unsearched.
- **Screen:** **KILL (folded into D13's significance spirit)** — three uncertainty candidates (D11/D13/D28) over-weights one sub-territory. D13 (early non-significance) is the more surprising, less headline-adjacent half; D28 (recent significance) leans toward confirming the warming headline. Drop D28 to balance; keep D11 + D13 + D12.

### E14 · Berkeley Earth monthly vs daily-city disagree with a latitude-dependent (non-constant) bias — KEEP
- **Claim:** Aggregating the daily-city dataset to monthly and converting °F→°C, the per-city monthly mean differs from Berkeley Earth ByMajorCity by a systematic offset that *varies with latitude* (or climate zone) — a cross-dataset bias that is NOT a constant calibration offset.
- **Prior:** two datasets measuring the same cities agree within ~1 °C with a roughly constant offset. A latitude-dependent (non-constant) bias is surprising. Confidence **M**.
- **Surprise if:** the per-city bias correlates with latitude (slope ≠ 0), not a flat offset.
- **Feasibility:** overlap 1995–2013; daily (°F) ↔ Berkeley major-city (°C) share city names (canonical/fuzzy match needed). Feasible; join is the work. **MED-HIGH**. (Foundation seam: cross-dataset consistency.)
- **Novelty:** no relevant Wikipedia hit for "Berkeley Earth versus daily city comparison"; appears unsearched. NOVEL.
- **Screen:** **KEEP** — cross-dataset seam, foundation-recommended, feasible, novel.

### E15 · City ranking flips between the two datasets — KILL (duplicate of E14)
- **Screen:** **KILL** — ranking-flip is a sub-outcome of E14's bias; folded (report as a secondary check inside E14).

### E16 · −99 sentinel missingness is seasonally concentrated → "clean before use" introduces a seasonal bias — KILL (partly known)
- **Claim:** The −99 sentinel is NOT uniform: it concentrates by season, so naively dropping −99 rows shifts those cities' seasonal mean.
- **Prior:** instrument failures roughly uniform across seasons; a strong seasonal concentration is surprising. Confidence M.
- **Feasibility:** feasible.
- **Novelty:** unsearched.
- **Screen:** **KILL** — the Foundation audit already computed "top cities with most −99s" (city-concentration known). The seasonal-concentration half is un-looked but lower-priority than the 10 keeps; recorded. Revivable.

### F17 · Warming-magnitude vs latitude is non-monotonic (warming-hole trough at city level) — KILL (NO-GO known)
- **Claim:** Per-city century warming vs latitude is non-monotonic, with a mid-latitude (≈35–50°N) trough — the "warming hole" localized at city level.
- **Prior:** monotonic "more warming toward poles" (Arctic amplification, NO-GO). A mid-latitude trough is surprising. Confidence M.
- **Feasibility:** feasible (ByMajorCity/ByCity have lat/long).
- **Novelty:** "North Atlantic warming hole" / "Cold blob" has a dedicated Wikipedia article → **KNOWN**, NOVEL fail.
- **Screen:** **KILL** — the warming hole is documented common knowledge (Foundation NO-GO + Wikipedia "Cold blob"); city-level quantification is table-specific but the headline fails NOVEL. Recorded.

### F18 · NH vs SH city warming asymmetry, but SH CI overlaps zero — KILL (NO-GO headline)
- **Claim:** NH major cities warmed more than SH, but the SH sample is so small the SH warming CI overlaps zero.
- **Prior:** NH>SH (Arctic amplification, NO-GO); predict SH warming significant. CI overlapping zero is surprising. Confidence M.
- **Feasibility:** feasible.
- **Novelty:** NH>SH warming is Foundation NO-GO.
- **Screen:** **KILL** — headline (NH>SH) is NO-GO; the SH-CI nuance is honest but thin. Recorded; the small-sample caveat is better folded into any cross-hemisphere experiment as a HONEST note.

### G19 · 2013-vs-2015 endpoint flips a "warmest decade" ranking — KILL
- **Claim:** At least one "warmest decade on record" ranking differs between the global (2015) and country (2013) endpoints.
- **Prior:** most-recent decade warmest under both endpoints; a flip is surprising. Confidence M.
- **Feasibility:** feasible.
- **Novelty:** "recent decades warmest" is NO-GO.
- **Screen:** **KILL** — fishing for an endpoint flip is selection-on-the-answer; endpoint sensitivity is a methodological caveat (report both endpoints inside any ranking experiment) not a standalone finding. Recorded.

### G20 · The warmest single (anomaly) month in the global record is NOT in the most recent decade — KILL (likely confirms)
- **Claim:** The single warmest calendar month by LandAverageTemperature *anomaly* occurred before the most recent decade.
- **Prior:** warmest anomaly month is recent ("everything hottest now," NO-GO intuition). Pre-2005 peak is surprising. Confidence M.
- **Feasibility:** feasible (GlobalTemperatures, monthly anomaly).
- **Novelty:** borderline; likely confirms the NO-GO.
- **Screen:** **KILL** — likely confirms the "everything hottest now" prior (low SURPRISING), and selecting on "the peak month" is cherry-picking one data point. Recorded.

### H21 · Country series changepoints align with geopolitical station reorganizations — KILL (involved + known)
- **Claim:** Specific country series contain step-changepoints aligned with known station-network reorganizations (post-WWII, 1991 Soviet collapse) rather than climate.
- **Prior:** Berkeley Earth homogenization removes most artificial changepoints; predict few survive. Several aligned with geopolitical events is surprising. Confidence M.
- **Feasibility:** changepoint detection per-country annual; more involved. CPU-OK.
- **Novelty:** station-network discontinuity/homogenization is a known subfield; table-specific timing is novel-ish but down-weighted.
- **Screen:** **KILL** — most involved to execute honestly (need event-timing + multiple changepoint methods + coverage controls), lower ROI than the 10 keeps; the homogenization-effect question is better as a critique-layer check on a surviving candidate. Recorded.

### H22 · Tiny/island "countries" have inflated variability — KILL (low surprise)
- **Claim:** Small/island single-station "countries" show much larger interannual variance than large area-averaged countries.
- **Prior:** area-averaging reduces variance → small countries higher variance. Matches prior → low surprise.
- **Screen:** **KILL** — confirms prior; the "some countries are single-station" insight is better as a HONEST caveat inside A1/E14. Recorded.

### I23 · Tambora 1815 cooling survives uncertainty-weighting only in a specific hemisphere×season — KILL (NO-GO + disciplined-re-attribution)
- **Claim:** Tambora's cooling is detectable in the uncertainty-weighted country series only in a specific (hemisphere×season) subset; in the global annual mean the ~2.6 °C pre-1850 uncertainty swallows it.
- **Prior:** expect Tambora detectable globally (famous, NO-GO). Only-in-a-subset is surprising. Confidence M.
- **Feasibility:** feasible (early high-uncertainty data).
- **Novelty:** volcanic cooling is Foundation NO-GO; the disciplined re-attribution is table-specific.
- **Screen:** **KILL** — headline (Tambora cooling) is NO-GO; the uncertainty-swallows-it nuance overlaps D13's SNR theme. Recorded; could be a nice confirmation test inside D13.

### I24 · Pinatubo 1991 cooling sharper in daily than monthly data — KILL (INFEASIBLE)
- **Claim:** Pinatubo's cooling appears as a sharper transient in the daily-city dataset than in monthly Berkeley Earth.
- **Feasibility:** **INFEASIBLE** — Pinatubo erupted 1991; the daily-city dataset starts **1995**. No overlap.
- **Screen:** **KILL — infeasible** (event predates the cross-check dataset). Good feasibility catch; recorded.

### J25 · Interannual temperature VARIANCE *decreased* for some regions while the mean rose — KEEP
- **Claim:** For some countries/regions, interannual temperature variance *decreased* over the record even as the mean rose — "more extreme/more variable weather" is not supported there; the distribution narrowed.
- **Prior:** expect variance to increase or stay flat as mean rises (more-energy→more-variability framing). A decrease is surprising. Confidence **M**.
- **Surprise if:** a non-trivial set of countries show a statistically real variance decrease (not a coverage artifact).
- **Feasibility:** per-country annual series → early/late window variance; paired/bootstrap CI; control for coverage change (HONEST). Feasible. **MED-HIGH**.
- **Novelty:** "global warming hiatus"/ENSO hits but not "variance decreased in specific countries in this table"; appears unsearched. NOVEL-ish.
- **Screen:** **KEEP** — distributional, surprising, feasible, honest-caveated (must rule out coverage artifact).

### J26 · Anomaly-distribution skewness changed sign over the record — KEEP
- **Claim:** The distribution of monthly anomalies (vs each station's own month-of-year climatology) was positively skewed in one era and symmetric/negatively skewed in another — the *shape* of the anomaly distribution changed, not just its center.
- **Prior:** anomalies roughly symmetric (Gaussian-ish) throughout, just shifted warmer. A sign change in skewness is surprising. Confidence **M**.
- **Surprise if:** skewness flips sign between eras for a non-trivial set of stations.
- **Feasibility:** per-station anomaly = monthly − station month-of-year climatology; skewness by era. Feasible (CPU). **MED-HIGH**.
- **Novelty:** unsearched at this specificity. NOVEL-ish.
- **Screen:** **KEEP** — distributional-shape change, surprising, feasible.

### A27 · Antarctica's ByCountry series is anomalously short/sparse — KILL (low surprise)
- **Claim:** The "Antarctica" country series is an outlier — very few months, very high uncertainty, near-stationless.
- **Prior:** Antarctica is known sparse → confirms prior → low surprise.
- **Screen:** **KILL** — confirms "Antarctica is sparse" common knowledge; the continent-entry oddity is better captured by A1. Recorded.

---

## SURVIVORS (10), ranked

| # | ID | Territory | Claim (short) | Cluster |
|---|----|-----------|----------------|---------|
| 1 | A1 | A | Continent pseudo-entries ≠ member-country average | Coverage |
| 2 | A3 | A | Longest "continuous" city series far shorter than its date span | Coverage |
| 3 | E14 | E | Berkeley-monthly vs daily-city disagree with latitude-dependent bias | CrossDataset |
| 4 | D11 | D | Uncertainty-weighting flips the warmest-decade ranking for ≥N countries | Uncertainty |
| 5 | D13 | D | Pre-1850 uncertainty makes most early "warmest-year" titles non-significant | Uncertainty |
| 6 | D12 | D | Temperature *uncertainty* itself has a winter>summer seasonal pattern | Uncertainty |
| 7 | B7 | B | New monthly COLD records still occur into the 2000s–2010s | Records-Asymmetry |
| 8 | C9 | C | For ≥1 major country the fastest-warming month is a shoulder month, not winter | Seasonal |
| 9 | J25 | J | Interannual variance *decreased* for some regions while the mean rose | Distributional |
| 10 | J26 | J | Anomaly-distribution skewness changed sign over the record | Distributional |

## KILL SUMMARY (18, with reasons)

| ID | Reason |
|----|--------|
| A2 | NO-GO coverage-sparsity / known coverage-artifact trap |
| A4 | Ordering violation — coverage counts already observed during shape scouting |
| A5 | Quartiles already seen lean against bimodality; retro-fit / low surprise |
| B6 | Folded into B7 (same record-asymmetry territory) |
| B8 | Sub-claim of B6/B7 |
| C10 | Folded into C9 (same seasonal-month territory) |
| D28 | Folded into D13; recent-significance leans toward confirming warming headline |
| E15 | Sub-outcome of E14 (ranking flip) |
| E16 | City-concentration of −99 partly known (Foundation audit); seasonal half lower-priority |
| F17 | NO-GO — "warming hole"/"Cold blob" is documented common knowledge (Wikipedia) |
| F18 | NO-GO headline (NH>SH); SH-CI nuance is thin |
| G19 | Fishing for an endpoint flip = selection-on-the-answer; methodological caveat, not a finding |
| G20 | Likely confirms "everything hottest now" + cherry-picks one peak month |
| H21 | Most involved to execute honestly; better as critique-layer check |
| H22 | Confirms prior (area-avg reduces variance); fold as caveat |
| I23 | NO-GO headline (Tambora/volcanic cooling); overlaps D13 SNR theme |
| I24 | **Infeasible** — Pinatubo 1991 predates the daily dataset (starts 1995) |
| A27 | Confirms "Antarctica sparse" common knowledge; captured by A1 |

## Funnel intake
- Generated: **28** · Survivors: **10** · Killed: **18** (2 infeasible/ordering, 7 NO-GO/known, 5 folded duplicates, 4 low-surprise/low-ROI)
- Territories covered by survivors: A(coverage/data-construction), E(cross-dataset), D(uncertainty×3 distinct sub-questions), B(records-asymmetry), C(seasonal refutation), J(distributional×2).
- All survivors are feasible on this CPU box from the available tables, use the uncertainty columns where relevant, and are records-over-headlines (none restates "the world is warming").

## Next step (handoff)
ONE gate, parented on this slate, to select 2–4 of these 10 for execution boxes.
