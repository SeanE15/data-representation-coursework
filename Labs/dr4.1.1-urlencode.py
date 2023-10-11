import urllib.parse
query = "Hello World@Python"
parsed = urllib.parse.quote(query)
print(parsed)

params = {"q":"Python URL encoding", "as_sitesearch": "www.urlencoder.io"}
parsedparams = urllib.parse.urlencode(params)
print(parsedparams)

