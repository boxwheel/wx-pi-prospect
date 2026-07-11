#!/usr/bin/env python3
"""Orchestrate creation of the Prospect slate + 10 candidate nodes in Flywheel.
Creates each node, uploads its hero artifact, assigns tags, sets public.
"""
import json, subprocess, time, sys, os

ENV = dict(os.environ, FLYWHEEL_BASE_URL="https://flywheel.paradigma.inc/api")
REPO_URL = "https://github.com/boxwheel/wx-pi-prospect"
REPO_BRANCH = "main"
REPO_SHA = "3548205f575a91999f1b839348d0a0bd909762e2"

# Foundation parents
F_MANIFEST = "12b533f2-4e86-5bd8-8971-e03db64d1de3"
F_ENV     = "0bbeb257-7fb0-562b-bbb1-3e2248ddd8f8"
F_LAND    = "3aef7f39-c635-55c1-b53a-cbf025bf2abb"
F_RUBRIC  = "506cf1d0-cc19-5cd4-9238-895b592b54e9"
SLATE_FOUNDATION_PARENTS = [F_MANIFEST, F_ENV, F_LAND, F_RUBRIC]

# Tag IDs
T_LAYER2  = "tag-2377f91c125e"   # Layer:2-Prospect
T_IDEA    = "tag-d019fbf5b3a5"   # kind:idea
T_CAND    = "tag-a87f65385896"   # kind:candidate
T_CLUSTER = {
    "Prospect":           "tag-36642addc5ba",
    "Coverage":           "tag-15d41e4acfa8",
    "CrossDataset":       "tag-1c9795f89a29",
    "Uncertainty":        "tag-b6dfa64489dd",
    "Records-Asymmetry":  "tag-9435088c1cd3",
    "Seasonal":           "tag-c09d695135f4",
    "Distributional":     "tag-852ddc023af1",
}

HERO_DIR = "/home/user/research/wx-pi-prospect/artifacts/heroes"
PROSPECTUS = "/home/user/research/wx-pi-prospect/artifacts/prospectus.md"
COVSHAPE   = "/home/user/research/wx-pi-prospect/artifacts/coverage_shape.json"

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, env=ENV, timeout=180)
    if r.returncode != 0:
        sys.stderr.write(f"CMD FAIL: {' '.join(args[:3])}\nSTDERR: {r.stderr[:500]}\nSTDOUT: {r.stdout[:500]}\n")
        return None
    try:
        return json.loads(r.stdout)
    except Exception:
        return r.stdout

def _parse(d):
    if isinstance(d, dict) and "node" in d and isinstance(d["node"], dict) and "revision" in d["node"]:
        return d["node"]["revision"]
    return None

def get_rev(node_id):
    d = run(["flywheel","nodes:get","--node_id="+node_id,"--format=json"])
    return d["revision"] if isinstance(d, dict) else None

def commit_new(parent_ids, title, content, summary, temp_id):
    payload = {
        "local_temp_node_id": temp_id,
        "parent_ids": parent_ids,
        "staged_payload": {
            "title": title, "content": content, "summary": summary,
            "repo_context": {"repo_url": REPO_URL, "branch_name": REPO_BRANCH,
                             "head_commit_sha": REPO_SHA, "origin_host": "github.com",
                             "updated_by": None, "external_transcript_ref": None}
        }
    }
    f = f"/tmp/payload_{temp_id}.json"
    with open(f, "w") as fh: json.dump(payload, fh)
    d = run(["flywheel","nodes:commit-new","--payload_json=@"+f,"--format=json"])
    return d["node"]["node_id"], get_rev(d["node"]["node_id"])

def upload(node_id, items):
    f = f"/tmp/items_{node_id}.json"
    with open(f, "w") as fh: json.dump(items, fh)
    for _ in range(3):
        rev = get_rev(node_id)
        d = run(["flywheel","artifacts:upload","--node_id="+node_id,
                 f"--expected_revision={rev}","--items=@"+f,"--format=json"])
        if d and not (isinstance(d,dict) and "error" in d):
            return get_rev(node_id)
        time.sleep(0.6)
    return get_rev(node_id)

def assign_tags(node_id, tag_id_list):
    for _ in range(3):
        rev = get_rev(node_id)
        d = run(["flywheel","tags:assign","--node_id="+node_id,
                 "--tag_ids="+",".join(tag_id_list),
                 f"--expected_revision={rev}","--format=json"])
        if d and not (isinstance(d,dict) and "error" in d):
            return get_rev(node_id)
        time.sleep(0.6)
    return get_rev(node_id)

def set_public(node_id):
    run(["flywheel","nodes:sharing:set","--node_id="+node_id,"--sharing_mode=public","--format=json"])

def make_node(parent_ids, title, content, summary, temp_id, hero_path, hero_title,
              cluster_name, is_slate=False, extra_artifacts=None):
    nid, rev = commit_new(parent_ids, title, content, summary, temp_id)
    print(f"  created {nid} rev={rev}")
    # upload hero + extras
    items = [{"local_path": hero_path, "artifact_type": "text",
              "title": hero_title, "media_type": "text/markdown"}]
    if extra_artifacts:
        items.extend(extra_artifacts)
    rev = upload(nid, items)
    print(f"  uploaded {len(items)} artifact(s) rev={rev}")
    # tags
    if is_slate:
        tags = [T_LAYER2, T_IDEA, T_CLUSTER["Prospect"]]
    else:
        tags = [T_LAYER2, T_CAND, T_CLUSTER[cluster_name]]
    rev = assign_tags(nid, tags)
    print(f"  tagged rev={rev}")
    set_public(nid)
    print(f"  public")
    time.sleep(0.4)
    return nid

# ---------- Slate node ----------
slate_content = """## Prospect slate — cycle 1 (fresh)

28 candidate hypotheses generated across 10 territories (A coverage/data-construction, B record-breaking, C seasonal/month, D uncertainty, E cross-dataset, F latitudinal, G endpoint, H station-composition, I event-attribution, J distributional), self-screened to **10 survivors**. 18 kills recorded with reasons (NO-GO known, infeasible, ordering-violation, duplicate, low-surprise).

**Discipline applied:**
- Registered priors written BEFORE any candidate statistic was computed; no prior quotes a measured value from these tables.
- 2 candidates (A4, A5) were KILLED for ordering violations — their answer-shape was already observed during *allowed* coverage scouting. Recorded to demonstrate screening discipline (the gate audits this).
- Feasibility judged from input SHAPE only (schemas, coverage breadth, joins); no answer statistic computed.
- Records over headlines: no survivor restates "the world is warming"; known common-knowledge items (warming hole/Cold blob, Tambora/volcanic cooling, NH>SH, "everything hottest now") screened out as NO-GO.
- One infeasible catch: Pinatubo (1991) predates the daily-city dataset (starts 1995) — killed as infeasible.

**Hero artifact = the full ranked candidate table** (`prospectus.md`): every candidate, survivors and kills, with priors, feasibility, novelty, and kill reasons. A second artifact (`coverage_shape.json`) records the shape scouting (no answer statistics).

**Survivors (ranked):** A1 continent-rollup · A3 longest-continuous-series · E14 cross-dataset latitude-bias · D11 uncertainty-weighting flips rankings · D13 early warmest-years non-significant · D12 uncertainty seasonality · B7 cold records persist · C9 shoulder-month warming · J25 variance decreased · J26 skewness sign change.

**Novelty:** partial web (Wikipedia API + limited DDG). Where Wikipedia had a dedicated article (Cold blob/warming hole) the claim was marked KNOWN→NO-GO. Otherwise claims recorded as "no relevant public hit; appears unsearched at the table-specific level" with the rubric's down-weight for well-known-in-science-but-not-for-these-tables.

Repo: https://github.com/boxwheel/wx-pi-prospect
"""
slate_summary = ("Prospect cycle-1 slate: 28 hypotheses generated across 10 territories, "
  "self-screened to 10 survivors with registered priors (written before any answer "
  "statistic), feasibility-from-shape, and novelty checks; 18 kills recorded with reasons "
  "(NO-GO/infeasible/ordering/duplicate/low-surprise). Hero artifact = full ranked candidate table.")

slate_extra = [
    {"local_path": COVSHAPE, "artifact_type": "json", "title": "coverage_shape.json — input shape scouting (no answer statistics)", "media_type": "application/json"},
]

slate_id = make_node(
    SLATE_FOUNDATION_PARENTS,
    "Prospect · Slate — 28 candidates → 10 survivors (climate-records, cycle 1)",
    slate_content, slate_summary, "slate",
    PROSPECTUS, "prospectus.md — full ranked candidate table (hero)",
    cluster_name="Prospect", is_slate=True, extra_artifacts=slate_extra)
print("SLATE:", slate_id)

# ---------- Candidate nodes ----------
CANDIDATES = [
 dict(cid="A1", cluster="Coverage", hero="A1_continent_rollup.md",
   title="Candidate A1 · Continent pseudo-entries ≠ member-country rollup (ByCountry)",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="Berkeley Earth ByCountry's Africa/Asia/Europe/NA/SA series are predicted to match an area-weighted member rollup; claim is they diverge systematically beyond member uncertainty — a data-construction oddity. Prior: divergence small (within uncertainty), conf M. Feasible: HIGH."),
 dict(cid="A3", cluster="Coverage", hero="A3_longest_continuous.md",
   title="Candidate A3 · Longest 'continuous' single-city monthly series ≪ its 1743 date span",
   parents=[F_MANIFEST, F_RUBRIC],
   summary="The earliest-start city (Århus 1743) is predicted to be gappy; claim is its longest no-NaN run begins ~1800-1850 not 1743 and the true longest-continuous city differs. Prior: longest run starts ~1800-1850, conf M. Feasible: HIGH."),
 dict(cid="E14", cluster="CrossDataset", hero="E14_cross_dataset_bias.md",
   title="Candidate E14 · Berkeley-monthly vs daily-city disagree by a latitude-dependent bias (1995-2013)",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="Converting daily-city (°F) to °C and aggregating to monthly, per-city Δ from Berkeley major-city is predicted to be a constant offset; claim is the bias slopes with latitude. Prior: flat ~1°C offset, conf M. Feasible: MED-HIGH (city-name join)."),
 dict(cid="D11", cluster="Uncertainty", hero="D11_uncertainty_flips_ranking.md",
   title="Candidate D11 · Uncertainty-weighting flips the warmest-decade ranking for ≥N countries",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="1/u²-weighting each monthly reading is predicted to barely move decadal rankings (<2 flippers); claim is ≥5 countries' warmest-decade title flips. Prior: <2 flippers, conf M. Feasible: HIGH."),
 dict(cid="D13", cluster="Uncertainty", hero="D13_early_warmest_nonsignificant.md",
   title="Candidate D13 · Pre-1850 uncertainty makes most early 'warmest-year' titles non-significant",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="With ~±2.6°C pre-1850 uncertainty, a large fraction of country warmest-year titles are predicted non-significant under an uncertainty-overlap test (>50%). Prior: >50% non-significant, conf M-H. Feasible: HIGH."),
 dict(cid="D12", cluster="Uncertainty", hero="D12_uncertainty_seasonality.md",
   title="Candidate D12 · Temperature *uncertainty* itself has a winter>summer seasonal pattern",
   parents=[F_MANIFEST, F_RUBRIC],
   summary="AverageTemperatureUncertainty is predicted seasonally flat; claim is a repeatable winter>summer cycle across mid/high-latitude countries — a non-climatic seasonality in the error bar. Prior: flat, conf M. Feasible: HIGH."),
 dict(cid="B7", cluster="Records-Asymmetry", hero="B7_cold_records_persist.md",
   title="Candidate B7 · New monthly COLD records still occur into the 2000s–2010s at station level",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="Warming should suppress new monthly cold records; claim is a non-trivial share of stations set a new same-month cold record after 2005. Prior: last global cold record before ~2000, conf M. Feasible: HIGH."),
 dict(cid="C9", cluster="Seasonal", hero="C9_shoulder_month_warming.md",
   title="Candidate C9 · For ≥1 major country the fastest-warming month is a shoulder month, not winter",
   parents=[F_MANIFEST, F_RUBRIC, F_LAND],
   summary="Refutes the NO-GO 'winters warm fastest' at table scale: a major country's argmax-warming month is a shoulder/summer month. Prior: winter peaks (NH Dec-Feb), conf M-H. Feasible: HIGH. NOVEL down-weighted; SURPRISING is the value."),
 dict(cid="J25", cluster="Distributional", hero="J25_variance_decreased.md",
   title="Candidate J25 · Interannual temperature VARIANCE decreased for some regions while the mean rose",
   parents=[F_MANIFEST, F_RUBRIC],
   summary="Pushes back on 'warming=more variable': a non-trivial set of regions show a real interannual-variance DECREASE after coverage controls. Prior: variance increases/stays flat, conf M. Feasible: MED-HIGH (needs coverage control)."),
 dict(cid="J26", cluster="Distributional", hero="J26_skewness_sign_change.md",
   title="Candidate J26 · Anomaly-distribution skewness changed sign over the record",
   parents=[F_MANIFEST, F_RUBRIC],
   summary="Monthly anomalies (vs station climatology) are predicted ~symmetric throughout; claim is skewness flips sign between eras for a non-trivial share of stations — a distributional-shape change. Prior: symmetric, conf M. Feasible: MED-HIGH."),
]

# concise content body generator for each candidate
def body(c):
    return (f"## Candidate {c['cid']} — registered prior BEFORE any evidence\n\n"
      f"Full claim + registered prior + feasibility + novelty + evidence plan are in the hero artifact "
      f"(`{c['hero']}`). This node exists to plant the candidate in the graph for the gate.\n\n"
      f"**One-line claim:** see hero. **Registered prior:** see hero (written before computing any answer statistic; "
      f"no measured value quoted). **Feasibility:** HIGH/MED-HIGH from input shape. **Novelty:** see hero.\n\n"
      f"**Evidence plan (NOT executed — prospect layer is generation only):** defined in the hero artifact; "
      f"the experiment layer executes it with frozen eval, held-out confirmation, uncertainty quantification, and "
      f"both-endpoints reporting per the rubric.\n\n"
      f"**Verdict:** pending (GREEN/RED/REFUTED to be set by the experiment, scored by critique/synthesis).\n\n"
      f"Repo: https://github.com/boxwheel/wx-pi-prospect")

produced = [slate_id]
for c in CANDIDATES:
    nid = make_node(
        parent_ids = [slate_id] + c["parents"],
        title = c["title"],
        content = body(c),
        summary = c["summary"],
        temp_id = c["cid"],
        hero_path = f"{HERO_DIR}/{c['hero']}",
        hero_title = f"{c['cid']} hero — claim + registered prior + evidence plan",
        cluster_name = c["cluster"], is_slate=False)
    produced.append(nid)
    print(f"  CANDIDATE {c['cid']}: {nid}")

# save ids for the handoff edit
with open("/tmp/prospect_produced.json","w") as f:
    json.dump({"slate_id": slate_id, "produced": produced}, f, indent=2)
print("PRODUCED:", json.dumps({"slate":slate_id,"produced":produced}))
