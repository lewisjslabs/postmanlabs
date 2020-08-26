import requests
import json

host = "investigate.api.umbrella.com"
api_key = "a0b1c2d3-e4f5-g6h7-i8j9-kalbmcndoepf"
domain = "internetbadguys.com"

print(f"\n==> Checking domain against Umbrella Investigate to retreive categorization")

url = f"https://{host}/domains/categorization/{domain}?showlabels"
headers = {'Authorization':'Bearer ' + api_key}

try:
	response = requests.get(url, headers=headers)
except:
	response.raise_for_status()

print (domain)
print (response.json())