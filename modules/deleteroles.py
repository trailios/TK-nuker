import aiosonic, asyncio

async def deleteroles(guild: int, roleid: int, headers: dict):
    while True:
        async with aiosonic.HTTPClient() as session:
            r = await session.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{roleid}", headers=headers)
            if r.status_code == 429:
                print("     Ratelimited..")
            else:
                if r.status_code in [200, 201, 204]:
                    print(f"    deleted role {roleid}")
                    break
                else:
                    break