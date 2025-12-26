import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

states = []

state_list_url = "https://gist.githubusercontent.com/jpriebe/d62a45e29f24e843c974/raw/us_state_capitals.json"
response = requests.get(state_list_url)
data = response.json()

for key, value in data.items():
    states.append(key)

results = {}

for state in states:
    url = "https://carto.nationalmap.gov/arcgis/rest/services/structures/MapServer/41/query"

    params = {
        "where": f"STATE='{state}'",
        "outFields": "NAME,ADDRESS,CITY,STATE,ZIPCODE",
        "f": "json",
        "returnGeometry": "true",
        "outSR": "4326"
    }

    response = requests.get(url, params, verify=False)
    data = response.json()

    features = data["features"][0]

    print(features)

    attributes = features["attributes"]
    geometry = features["geometry"]

    results[state] = {
        "address": f"{attributes['ADDRESS']}, {attributes['CITY']}, {attributes['ZIPCODE']}",
        "lat": geometry["x"],
        "long": geometry["y"]
    }

print(results)

with open("state_capitals.json", "w") as file:
    json.dump(state_capitals, file, indent=4, sort_keys=True)
