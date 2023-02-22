import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=van gogh&isOnView=true&hasImages=true"
headers = {'Content-Type': 'application/json'}
res = requests.get(url, headers=headers)
res_json = res.json()
res_json = json.loads(res.text)
print(json.dumps(res_json, indent=2))
