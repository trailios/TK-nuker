import aiosonic, asyncio

async def createchannels(guild: int, name: str, headers: dict):
    chanelIDS = []
    while True:
        async with aiosonic.HTTPClient() as session:
            json = {"name": name, "type": 0}
            channels = await session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers, json=json)
            json = await channels.json()
            if channels.status_code == 429:
                print("     Ratelimited..")
            else:
                if channels.status_code in [200, 201, 204]:
                    print(f"    created channel {json['id']}")
                    break
                else:
                    break