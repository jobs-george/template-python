import json

def write_json(data, path_file = "data/data.json"):

    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
