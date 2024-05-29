import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import asyncio
import aiohttp

target_ip = "127.0.0.1"
target_port = 4321
request_count = 100000000

async def send_requests():
    async with aiohttp.ClientSession() as session:
        for _ in range(request_count):
            try:
                url = f"http://{target_ip}:{target_port}"
                async with session.get(url) as response:
                    print(f"Status code: {response.status}")
            except Exception as e:
                print(f"Error: {e}")

asyncio.run(send_requests())
