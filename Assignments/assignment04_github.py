from github import Github 
from config import config as cfg 
import requests
import json 

filename = "test.txt"
url = "https://api.github.com/repos/SeanE15/private"

# store api key in config program that is store locally rather than on Github
apikey = cfg["github"]

response = requests.get(url, auth = ("token", apikey))
#print (response.status_code)
repoJSON = response.json()

#store apikey in variable 'g'
g = Github(apikey)

repo = g.get_repo("SeanE15/private")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
print(fileInfo)
