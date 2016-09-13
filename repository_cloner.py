#! /usr/local/bin/python3

import urllib.request
import json
import subprocess
import argparse

parser = argparse.ArgumentParser(description="A script used for repository cloning from GitHub and GitLab code hosting sites.")
parser.add_argument("site", help="code hosting site")
parser.add_argument("organisation", help="organisation or group from which to retrieve all repositories")
parser.add_argument("-a", "--access-token", help="access token for accessing private repositories")
args = parser.parse_args()

current_page_message = "\033[92mOn page: {}\033[0m"
cloned_repositories_message = "\033[92mCloned {} repositories.\033[0m"
help_command_message = "\033[95mUse \033[1m./repository_cloner.py --help\033[0m \033[95m for more information.\033[0m"

wrong_git_site_error = "\033[1m\033[93mProvided code hosting site didn't match either GitHub or GitLab.\033[0m \n{}"
missing_access_token_error = "\033[1m\033[93mIn order to get GitLab repositories for organisation {} " \
                             "you have to provide the private access token by using the -a flag. \033[0m \n{}"

github_url = "https://api.github.com/orgs/{}/repos?per_page=100&page={}"
gitlab_url = "https://gitlab.com/api/v3/groups/{}/projects?per_page=100&page={}"
git_clone_cmd = "git clone {}"

page = 1
cloned_repository_count = 0


# Creates a URL that will be used to call the code hosting site API to get a JSON object with repositories.
def create_url():
    if args.site.lower() == "github":
        return get_github_url()
    elif args.site.lower() == "gitlab":
        return get_gitlab_url()
    else:
        raise AttributeError(wrong_git_site_error.format(help_command_message))


def get_gitlab_url():
    if args.access_token is not None:
        return gitlab_url.format(args.organisation, str(page)) + "&private_token=" + args.access_token
    else:
        raise AttributeError(missing_access_token_error.format(args.organisation, help_command_message))


def get_github_url():
    if args.access_token is not None:
        return github_url.format(args.organisation, str(page)) + "&access_token=" + args.access_token
    else:
        return github_url.format(args.organisation, str(page))


# Clones Git repository by executing git clone bash command.
def clone_repo(repository_to_clone):
    bash_cmd = git_clone_cmd.format(repository_to_clone)
    process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
    print(process.communicate()[0])

# Making the first request for repositories.
response = urllib.request.urlopen(create_url()).read()
repositories = json.loads(response.decode('utf-8'))

# While there are more repositories in the next page, continue cloning the repositories.
while len(repositories) != 0:
    print(current_page_message.format(str(page)))
    for repository in repositories:
        cloned_repository_count += 1
        if args.site.lower() == "github":
            clone_repo(repository['git_url'])
        elif args.site.lower() == "gitlab":
            clone_repo(repository['ssh_url_to_repo'])
    page += 1
    nextResponse = urllib.request.urlopen(create_url()).read()
    repositories = json.loads(nextResponse.decode('utf-8'))

print(cloned_repositories_message.format(str(cloned_repository_count)))
