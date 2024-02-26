import aiohttp, asyncio

async def ban_members(guild: int, member_id: str, headers: dict):
    while True:
        with aiohttp.ClientSession() as session:
            resp = await session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member_id}", headers=headers)
            if resp.status == 429:
                print("     Ratelimited..")
            else:
                if resp.status in [200, 201, 204]:
                    print(f"    banned {member_id}")
                    break
                else:
                    break