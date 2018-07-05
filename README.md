```
          _ __                                _ __
   ____ _(_) /_   ________  ____  ____  _____(_) /_____  _______  __
  / __ `/ / __/  / ___/ _ \/ __ \/ __ \/ ___/ / __/ __ \/ ___/ / / /
 / /_/ / / /_   / /  /  __/ /_/ / /_/ (__  ) / /_/ /_/ / /  / /_/ /
 \__, /_/\__/  /_/   \___/ .___/\____/____/_/\__/\____/_/   \__, /    __
/____/                  /_/                                /____/____/ /___  ____  ___  _____
                                                               / ___/ / __ \/ __ \/ _ \/ ___/
                                                              / /__/ / /_/ / / / /  __/ /
                                                              \___/_/\____/_/ /_/\___/_/

```
A script used for repository cloning from GitHub, GitLab and BitBucket code hosting sites.

### How to run the script?
**GitHub)** `./repository_cloner.py github <group>`

Example of cloning all the Google repositories - `./repository_cloner.py github google`

**GitLab)** `./repository_cloner.py gitlab <organisation> -a <private_access_token>`

**BitBucket)** `./repository_cloner.py bitbucket <organisation>`

Help page: `./repository_cloner.py --help`

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).