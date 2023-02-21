import requests
import json

url = "https://api.moma.org/api/artists/2206?token=202d9d02-ede9-49a8-9ebb-4aa5bd3f0000"
headers = {'Content-Type': 'application/json'}
res = requests.get(url, headers=headers)
res_json = res.json()
formatted_res = json.dumps(res_json, indent=2)
print(formatted_res)