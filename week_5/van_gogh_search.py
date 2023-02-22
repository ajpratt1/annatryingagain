import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/object"
headers = {'Content-Type': 'application/json'}
res = requests.get(https://collectionapi.metmuseum.org/public/collection/v1/search/artistOrCulture/gogh, headers=headers)
res_json = res.json()
res_json = json.loads(res.text)
print(json.dumps(res_json, indent=2))
