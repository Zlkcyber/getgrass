# getgrass
## installation
install python3
for windows: https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe 

for linux distros: ```sudo apt-get install python3``` or ```sudo yum install python3``` or ```sudo dnf install python3```
## module install 
install fakeuseragent
```pip install fake_useragent```

install loguru
```pip install loguru```

install websockets_proxy
```pip install websockets_proxy```

## register: https://app.getgrass.io/register/?referralCode=PnmuSjrqxyxvZsk ( use this link instead! )

## how to use

#### getting your user id

login to https://app.getgrass.io

press f12 go to console, then type ```allow pasting```

![0001](https://github.com/im-hanzou/getgrass_bot/blob/main/pasting.JPG)

then insert this code
```localStorage.getItem('userId')```

![0001](https://github.com/im-hanzou/getgrass_bot/blob/main/userid.JPG)

#### usage command
for one account and many proxies use 1user_id.py and insert your proxies to proxy_list(for1).txt

then ```python 1user_id.py``` and insert your userid

![0001](https://github.com/im-hanzou/getgrass_bot/blob/main/insert.JPG)

for multiple accounts and for each of them one proxy use foreachuser_id_proxy.py, insert your accounts user ids to user_id.txt and insert your proxies to proxy_list(all).txt

then ```python foreachuser_id_proxy.py ```


