from github import Github 
from config import config as cfg 
import requests

apikey = cfg["github"]

g = Github(apikey)

repo = g.get_repo("SeanE15/private")
print(repo.clone_url)


fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
newContents = contentOfFile + " more stuff 2 \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by programme",newContents,fileInfo.sha)
print (gitHubResponse)