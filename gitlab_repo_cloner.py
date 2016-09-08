import urllib.request
import json
import subprocess
import sys

gitlab_url = "https://gitlab.com/api/v3/groups/{}/projects?private_token={}&per_page=100&page={}"
git_clone_cmd = "git clone {}"

current_page_message = "\033[92mCurrent page: {}\033[0m"
cloned_repositories_message = "\033[92mCloned {} repositories.\033[0m"

group = sys.argv[1]
access_token = sys.argv[2]
page = 1
cloned_repository_count = 0


def create_url():
    return gitlab_url.format(group, access_token, str(page))


def clone_repo(ssh_url_to_repo):
    bash_cmd = git_clone_cmd.format(ssh_url_to_repo)
    process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
    print(process.communicate()[0])


response = urllib.request.urlopen(create_url()).read()
repositories = json.loads(response.decode('utf-8'))

while len(repositories) != 0:
    print(current_page_message.format(str(page)))
    for repository in repositories:
        cloned_repository_count += 1
        clone_repo(repository['ssh_url_to_repo'])
    page += 1
    nextResponse = urllib.request.urlopen(create_url()).read()
    repositories = json.loads(nextResponse.decode('utf-8'))

print(cloned_repositories_message.format(str(cloned_repository_count)))
