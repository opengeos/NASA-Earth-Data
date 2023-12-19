import json
import earthaccess
import pandas as pd

earthaccess.login()

datasets = earthaccess.search_datasets(keyword="*")


def get_info(dataset):
    info = {}
    info["ShortName"] = dataset["umm"]["ShortName"]
    info["EntryTitle"] = dataset["umm"]["EntryTitle"]
    try:
        info["DOI"] = dataset["umm"]["DOI"]["DOI"]
    except:
        info["DOI"] = ""
    info["concept-id"] = dataset["meta"]["concept-id"]
    info["provider-id"] = dataset["meta"]["provider-id"]

    try:
        info["s3-links"] = dataset["meta"]["s3-links"]
    except:
        info["s3-links"] = ""
    info["granule-count"] = dataset["meta"]["granule-count"]
    try:
        info["Creator"] = dataset["umm"]["CollectionCitations"][0]["Creator"]
    except:
        info["Creator"] = ""
    try:
        info["Publisher"] = dataset["umm"]["CollectionCitations"][0]["Publisher"]
    except:
        info["Publisher"] = ""
    try:
        info["ReleaseDate"] = dataset["umm"]["CollectionCitations"][0]["ReleaseDate"]
    except:
        info["ReleaseDate"] = ""
    try:
        info["ReleasePlace"] = dataset["umm"]["CollectionCitations"][0]["ReleasePlace"]
    except:
        info["ReleasePlace"] = ""

    try:
        info["Version"] = dataset["umm"]["CollectionCitations"][0]["Version"]
    except:
        info["Version"] = ""

    if info["DOI"] != "":
        info["Linkage"] = "https://doi.org/" + info["DOI"]
    else:
        info["Linkage"] = ""

    return info


data = [get_info(dataset) for dataset in datasets]
df = pd.DataFrame(data)
df.sort_values(by=["ShortName"], inplace=True)

df.to_csv("nasa_earth_data.tsv", index=False)

with open("nasa_earth_data.json", "w") as f:
    json.dump(df.to_dict("records"), f, indent=4)
