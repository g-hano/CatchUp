def Report(analysis: str):
    try:
        with open("analysis.txt", "w") as f:
            f.write(analysis)
            print("Succesfully saved")
    except Exception:
        print("Exception Occurred: ", Exception)

import requests
import json
def InternetSearch(query: str):
    url = "https://google.serper.dev/search"

    payload = json.dumps({
        "q": query,
        "num": 3
    })
    headers = {
        'X-API-KEY': 'e2cbe13e681460766f8f897683646601ab0c2b08',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

import wikipedia
def wikipedia_search(user_input: str):
    return wikipedia.search(user_input)
