import requests
import json
from config import config as cfg

filename = "repos-private.json"

targetUrl = "https://github.com/SeanE15/aprivateone"

apiKey = cfg["github"]

apiurl = "https://api.html2pdf.app/v1/generate"

response = requests.get(targetUrl, auth=("token", apiKey))
repoJSON = response.json()

with open (filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)