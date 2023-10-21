import requests
import json 

filename = "repos-public.json"

url = "https://api.github.com/repos/SeanE15/Programming-for-Data-Analysis"

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()

with open (filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)