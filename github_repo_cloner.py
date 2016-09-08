import urllib.request
import json
import subprocess
import sys

cloned_repositories_message = "\033[92mCloned {} repositories.\033[0m"

github_url = "https://api.github.com/orgs/{}/repos"
git_clone_cmd = "git clone {}"

cloned_repository_count = 0

response = urllib.request.urlopen(github_url.format(sys.argv[1])).read()
repositories = json.loads(response.decode('utf-8'))

for repository in repositories:
    cloned_repository_count += 1
    bash_cmd = git_clone_cmd.format(repository['git_url'])
    process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

print(cloned_repositories_message.format(str(cloned_repository_count)))
