import requests
import json
import apiKey

def gpi(input):
    url = str("https://api-nba-v1.p.rapidapi.com/players/lastName/" + input)

    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': apiKey.key
    }

    response = requests.request("GET", url, headers=headers)
    parsed = json.loads(response.text)

    print(json.dumps(parsed, indent=2, sort_keys=True))