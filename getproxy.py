import os
import requests
from git import Repo
import time


# Download the file from the URL
print("Update Proxy...")
url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/all.txt'
response = requests.get(url)
with open('all.txt', 'wb') as f:
    f.write(response.content)

# Rename the file
os.rename('all.txt', 'proxy.txt')
print("Update Proxy Success save to proxy.txt")

    
