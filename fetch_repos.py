import os
import subprocess
import json
from constants import USERNAME, TOKEN, REPO_PATH

def main():

    # Fetching repos from github
    response = subprocess.run(f'curl -u {USERNAME}:{TOKEN} https://api.github.com/user/repos'f'', shell=True, capture_output=True, text=True)
    repos = json.loads(response.stdout) # Parse the JSON output

    if ('message' in repos):
        print('Error:', repos['message'])
        if repos['message'] == 'Bad credentials':
            print('Please check your github username and token in constants.py')
        if repos['message'] == 'Not Found':
            print('Please check your github username in constants.py')
        exit()
    else:
        print('Success:', len(repos), 'repos fetched')

    repo_list = [repo['html_url'] for repo in repos]
    for repo in repos:
        print(repo['html_url'])

    os.chdir(REPO_PATH)
    print('Current Directory:', os.getcwd())
    for repo in repo_list:
        if os.path.exists(f'{REPO_PATH}/{repo.split("/")[-1]}'): # If the directory already exists don't clone it again
            print(f'{repo.split("/")[-1]} already exists')
            continue
        os.system(f'git clone {repo}.git')
        print(f'{repo.split("/")[-1]} cloned successfully')

    print('All repos cloned successfully')

if __name__ == '__main__':
    main()