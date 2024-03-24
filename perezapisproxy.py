#opening
with open('proxy_list.txt', 'r') as file:
    proxies = file.readlines()

#add "socks5://" before the IP address
socks5_proxies = ['socks5://' + proxy.strip() for proxy in proxies]

# open
with open('proxy_list.txt', 'w') as file:
    #rewrite
    file.write('\n'.join(socks5_proxies))
