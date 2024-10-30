import os
import requests
from git import Repo
import time


# Download the file from the URL
url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt'
response = requests.get(url)
with open('all.txt', 'wb') as f:
    f.write(response.content)

# Rename the file
os.rename('all.txt', 'proxy.txt')

# Initialize the Git repository in the current directory
repo = Repo('.')
repo.index.add(['proxy.txt'])

# Commit changes
repo.index.commit('Automatic commit')

# Push changes to the 'main' branch of the remote repository
origin = repo.remote(name='origin')
origin.push('main')

    
