import urllib.request
import json
import subprocess
import sys

GREEN_COLOR = '\033[92m'
END_COLOR = '\033[0m'

group = sys.argv[1]
access_token = sys.argv[2]
page = 1
totalClonedRepos = 0

def createUrl():
	return "https://gitlab.com/api/v3/groups/" + group + "/projects?private_token=" + access_token + "&per_page=100&page=" + str(page)

def cloneRepo(ssh_url_to_repo):
	bashCommand = "git clone " + ssh_url_to_repo
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]

response = urllib.request.urlopen(createUrl()).read()
repos = json.loads(response.decode('utf-8'))

while(len(repos) != 0):
	print(GREEN_COLOR + "Current page: " + str(page) + END_COLOR)
	for repo in repos:
		totalClonedRepos = totalClonedRepos + 1
		cloneRepo(repo['ssh_url_to_repo'])
	page = page + 1
	nextResponse = urllib.request.urlopen(createUrl()).read()
	repos = json.loads(nextResponse.decode('utf-8'))

print(GREEN_COLOR + "Cloned: " + str(totalClonedRepos) + " repos" + END_COLOR)