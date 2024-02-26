import aiosonic, asyncio

async def createroles(guild: int, rolename: str, headers: dict):
    while True:
        async with aiosonic.HTTPClient() as session:
            r = await session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json={"name": rolename})
            if r.status_code == 429:
                print("     Ratelimited..")
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"    created role {rolename}")
                    break
                else:
                    break