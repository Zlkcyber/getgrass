import asyncio
import random
import ssl
import json
import time
import uuid
import requests
from loguru import logger
from websockets_proxy import Proxy, proxy_connect
from fake_useragent import UserAgent

async def connect_to_wss(socks5_proxy, user_id):
    user_agent = UserAgent(os=['windows', 'macos', 'linux'], browsers='chrome')
    random_user_agent = user_agent.random
    device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, socks5_proxy))
    logger.info(device_id)
    while True:
        try:
            await asyncio.sleep(random.randint(1, 10) / 10)
            custom_headers = {
                "User-Agent": random_user_agent,
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            urilist = ["wss://proxy.wynd.network:4444/","wss://proxy.wynd.network:4650/"]
            uri = random.choice(urilist)
            server_hostname = "proxy.wynd.network"
            proxy = Proxy.from_url(socks5_proxy)
            async with proxy_connect(uri, proxy=proxy, ssl=ssl_context, server_hostname=server_hostname,
                                     extra_headers=custom_headers) as websocket:
                async def send_ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        logger.debug(send_message)
                        await websocket.send(send_message)
                        await asyncio.sleep(5)

                await asyncio.sleep(1)
                asyncio.create_task(send_ping())

                while True:
                    response = await websocket.recv()
                    message = json.loads(response)
                    logger.info(message)
                    if message.get("action") == "AUTH":
                        auth_response = {
                            "id": message["id"],
                            "origin_action": "AUTH",
                            "result": {
                                "browser_id": device_id,
                                "user_id": user_id,
                                "user_agent": custom_headers['User-Agent'],
                                "timestamp": int(time.time()),
                                "device_type": "desktop",
                                "version": "4.28.2",
                            }
                        }
                        logger.debug(auth_response)
                        await websocket.send(json.dumps(auth_response))

                    elif message.get("action") == "PONG":
                        pong_response = {"id": message["id"], "origin_action": "PONG"}
                        logger.debug(pong_response)
                        await websocket.send(json.dumps(pong_response))
        except Exception as e:
            pass
            

async def main():
    # Load user IDs from userid.txt
    with open('userid.txt', 'r') as f:
        user_ids = [line.strip() for line in f if line.strip()]

    while True:
        r = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/all.txt")
        if r.status_code == 200:
            with open('socks5.txt', 'wb') as f:
                for chunk in r:
                    f.write(chunk)
            with open('socks5.txt', 'r') as file:
                auto_proxy_list = file.read().splitlines()

            # Start connections for each proxy-user ID pair
            tasks = [asyncio.ensure_future(connect_to_wss(proxy, user_id))
                     for proxy in auto_proxy_list
                     for user_id in user_ids]
            await asyncio.gather(*tasks)

        # Wait an hour before fetching the new proxy list
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
