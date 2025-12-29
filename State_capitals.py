import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.session()
session.verify = False

state_list_url = "https://gist.githubusercontent.com/jpriebe/d62a45e29f24e843c974/raw/us_state_capitals.json"
response = requests.get(state_list_url)
data = response.json()

state_capitals = {}

for key, value in data.items():
    print("======================")
    print(value)
    state_name = value["name"]
    capital_name = value["capital"]

    state_capitals[state_name] = {
        "capital": value["capital"],
        "lat": value["lat"],
        "long": value["long"]
    }

print(state_capitals)

with open("state_capitals.json", "w") as file:
    json.dump(state_capitals, file, indent=4, sort_keys=True)

