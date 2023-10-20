import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://dash.html2pdf.app/"
apiKey = cfg["htmltopdfkey"]

apiurl = "https://api.html2pdf.app/v1/generate"

params = {"url": targetUrl, "apiKey": apikey}
parsedparams = urlib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams 

response = requests.get(requestUrl)
print (response.status_code)

result = response.content
with open ("document.pdf", "wb") as handler:
    handler.write(result)