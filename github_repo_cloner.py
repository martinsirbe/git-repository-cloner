import urllib.request
import json
import subprocess
import sys

response = urllib.request.urlopen("https://api.github.com/orgs/" + sys.argv[1] + "/repos").read()
j_obj = json.loads(response.decode('utf-8'))
for element in j_obj:
	print(element['git_url'])
	bashCommand = "git clone " + element['git_url']
	process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]