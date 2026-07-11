# wx-pi-prospect — Prospect (Layer 2) slate for the climate-records campaign

Campaign `cp_60fb4891`, root `d8fba110`. Prospect lane, cycle 1, fresh slate.

## What this repo holds

- `artifacts/prospectus.md` — the **full ranked candidate table**: 28 hypotheses generated, 10 survivors, 18 kills (with reasons: NO-GO known, infeasible, ordering-violation, duplicate, low-surprise). Every candidate carries a **registered prior** (direction + rough magnitude, written *before* any answer statistic was computed), a feasibility assessment from input *shape* only, a novelty-search result, and a surprise justification.
- `artifacts/coverage_shape.json` — the **scouting artifact**: schemas, coverage breadth per decade, continent pseudo-entries, state-table country set, daily-city structure. Coverage shape only — **no answer statistics** (no trends, no record-counts-by-value, no warming magnitudes).
- `code/scout_coverage_shape.py` — reproduces `coverage_shape.json` from the Kaggle tables.
- `code/novelty_search.py` — Wikipedia/DDG novelty-search helper used per candidate.

## Data (NOT committed — re-fetch from Kaggle)

```
kaggle datasets download -d berkeleyearth/climate-change-earth-surface-temperature-data -p data/ --unzip
kaggle datasets download -d sudalairajkumar/daily-temperature-of-major-cities        -p data/ --unzip
python3 code/scout_coverage_shape.py
```

## Reproduce the slate

The slate and all 10 surviving candidate idea nodes live in the Flywheel graph under the campaign root. Read `artifacts/prospectus.md` for the full reasoning. The hero artifact of the slate node IS `prospectus.md`.

## The 10 survivors (ranked)

1. **A1** — Continent pseudo-entries (Africa/Asia/Europe…) in ByCountry diverge from a member-country rollup. [Coverage]
2. **A3** — The longest *continuous* single-city monthly series is far shorter than its 1743 date span implies (multi-year NaN gaps). [Coverage]
3. **E14** — Berkeley Earth monthly vs daily-city disagree by a *latitude-dependent* (non-constant) bias in the 1995–2013 overlap. [CrossDataset]
4. **D11** — Uncertainty-weighting flips which decade is "warmest" for ≥N countries. [Uncertainty]
5. **D13** — Pre-1850 (~±2.6 °C) uncertainty makes most early "warmest-year" titles statistically non-significant. [Uncertainty]
6. **D12** — Temperature *uncertainty* itself has a winter>summer seasonal pattern (non-climatic seasonality in the error bar). [Uncertainty]
7. **B7** — New monthly COLD records for individual stations still occur into the 2000s–2010s. [Records-Asymmetry]
8. **C9** — For ≥1 major country, the fastest-warming month is a shoulder month, not deep winter. [Seasonal]
9. **J25** — Interannual temperature *variance decreased* for some regions while the mean rose. [Distributional]
10. **J26** — Anomaly-distribution *skewness changed sign* over the record. [Distributional]

## Graph location (Flywheel)

- **Slate node (terminal):** `e2faef06-49e7-5f1f-a7f0-1950cc117e57` — carries the handoff block for the campaign daemon; parented on all four Foundation nodes.
- **10 candidate idea nodes** are children of the slate, each multi-parented on the Foundation nodes it draws on (data-manifest / landscape / rubric), each with its own `Cluster:` lane tag.
- Campaign root: `d8fba110-3124-5f4a-be55-630d2da6b301` (campaign id `cp_60fb4891`).
- Latest repo commit: `511194b`.

## Method discipline

- **Registered priors written before looking.** No candidate prior quotes a measured value from these tables. Two candidates (A4, A5) were *killed* because their answer-shape was already observed during allowed coverage scouting — recorded to demonstrate ordering discipline (the gate audits this).
- **Records over headlines.** No survivor restates "the world is warming"; known common-knowledge items (warming hole, Tambora, NH>SH, etc.) were screened out as NO-GO.
- **Feasibility from shape only.** No candidate statistic was computed during prospecting.
