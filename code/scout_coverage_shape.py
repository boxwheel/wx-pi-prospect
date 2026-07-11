"""Scout the SHAPE of the climate inputs (schemas, coverage breadth, joins).
Records NO candidate answer statistics (no trends, no record-counts-by-value,
no warming magnitudes). Used by the Prospect layer to ground feasibility.
Run from repo root with data/ populated by kaggle CLI.
"""
import pandas as pd, json, os

def main():
    os.makedirs("artifacts", exist_ok=True)
    out = {}
    # GlobalTemperatures
    gt = pd.read_csv("data/GlobalTemperatures.csv")
    gt["dt"] = pd.to_datetime(gt["dt"])
    out["global"] = {"cols": list(gt.columns), "rows": len(gt),
                     "range": [gt["dt"].min().date().isoformat(), gt["dt"].max().date().isoformat()],
                     "nulls": gt.isnull().sum().to_dict()}
    # ByCountry
    c = pd.read_csv("data/GlobalLandTemperaturesByCountry.csv")
    c["dt"] = pd.to_datetime(c["dt"]); c["Year"] = c["dt"].dt.year; c["Decade"] = (c["Year"]//10*10)
    pseudo = ["Africa","Asia","Europe","North America","South America","Antarctica"]
    out["country"] = {"cols": list(c.columns), "rows": len(c),
                      "n_countries": int(c["Country"].nunique()),
                      "continent_entries_present": [x for x in pseudo if x in c["Country"].unique()],
                      "range": [c["dt"].min().date().isoformat(), c["dt"].max().date().isoformat()],
                      "nulls": c.isnull().sum().to_dict(),
                      "countries_per_decade": c.dropna(subset=["AverageTemperature"]).groupby("Decade")["Country"].nunique().to_dict()}
    # ByState
    s = pd.read_csv("data/GlobalLandTemperaturesByState.csv")
    out["state"] = {"cols": list(s.columns), "rows": len(s),
                    "n_states": int(s["State"].nunique()),
                    "countries_with_states": s["Country"].unique().tolist()}
    # ByMajorCity
    mc = pd.read_csv("data/GlobalLandTemperaturesByMajorCity.csv")
    mc["dt"] = pd.to_datetime(mc["dt"]); mc["Year"]=mc["dt"].dt.year; mc["Decade"]=(mc["Year"]//10*10)
    out["majorcity"] = {"cols": list(mc.columns), "rows": len(mc),
                        "n_cities": int(mc["City"].nunique()),
                        "range": [mc["dt"].min().date().isoformat(), mc["dt"].max().date().isoformat()],
                        "has_latlong": "Latitude" in mc.columns and "Longitude" in mc.columns,
                        "cities_per_decade": mc.dropna(subset=["AverageTemperature"]).groupby("Decade")["City"].nunique().to_dict()}
    # ByCity (header only — 532MB)
    bc = pd.read_csv("data/GlobalLandTemperaturesByCity.csv", nrows=5)
    out["city"] = {"cols": list(bc.columns), "has_latlong": "Latitude" in bc.columns}
    # Daily
    ct = pd.read_csv("data/city_temperature.csv", low_memory=False)
    out["daily"] = {"cols": list(ct.columns), "rows": len(ct),
                    "n_cities": int(ct["City"].nunique()), "n_countries": int(ct["Country"].nunique()),
                    "year_min": int(ct["Year"].min()), "year_max": int(ct["Year"].max()),
                    "regions": ct["Region"].unique().tolist() if "Region" in ct.columns else [],
                    "sentinel_99": int((ct["AvgTemperature"]==-99.0).sum()),
                    "year_200_rows": int((ct["Year"]==200).sum()), "day_0_rows": int((ct["Day"]==0).sum())}
    with open("artifacts/coverage_shape.json","w") as f:
        json.dump(out, f, indent=2, default=str)
    print("wrote artifacts/coverage_shape.json")

if __name__=="__main__":
    main()
