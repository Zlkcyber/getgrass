import subprocess
import os
import requests
from git import Repo
import time

repo_path = '/root/grasspr/'  # Path to the Git repository

while True:
    # Download the file from the URL
    url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt'
    response = requests.get(url)
    with open('all.txt', 'wb') as f:
        f.write(response.content)

    # Rename the file
    os.rename('all.txt', 'proxy.txt')

    # Add all files to the Git repository
    repo = Repo(repo_path)
    repo.index.add('*')

    # Commit changes
    repo.index.commit('Automatic commit')

    # Push changes to the 'main' branch of the remote repository
    origin = repo.remote(name='origin')
    origin.push('main')

    # Wait for 5 minutes before running the loop again
    time.sleep(5 * 60)

