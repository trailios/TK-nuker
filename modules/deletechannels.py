import aiosonic, asyncio

async def deletechannels(guild: int, channelid: int, headers: dict):
    while True:
        async with aiosonic.HTTPClient() as session:
            s = await session.delete(f"https://discord.com/api/v9/channels/{channelid}", headers=headers)
            if s.status_code == 429:
                print("     Ratelimited..")
            else:
                if s.status_code in [200, 201, 204]:
                    print(f"    deleted channel {channelid}")
                    break
                else:
                    break