import requests

from src.write_json import write_json

# see here for more info
# https://docs.python-requests.org/en/latest/user/quickstart/

payload = {"key1": "value1", "key2": ["value2", "value3"]}

try:
    r = requests.get("https://httpbin.org/get", params=payload)
    data = r.json()
    write_json(data=data, path_file="data/data.json")
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)