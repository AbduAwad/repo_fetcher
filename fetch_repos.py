import os
import json
from constants import USERNAME, TOKEN

# Request to list all public repositories:  curl https://api.github.com/users/AbduAwad/repos
# Request to list all repos pub/priv: curl -u username:token https://api.github.com/user/repos
# For only private repos: curl -u username:token https://api.github.com/user/repos?visibility=private
# For only public repos: curl -u username:token https://api.github.com/user/repos?visibility=public
# For repos you are a collaborator on: curl -u username:token https://api.github.com/user/repos?affiliation=collaborator
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

os.system(f'curl -u {USERNAME}:{TOKEN} https://api.github.com/user/repos'f' > repos.json')