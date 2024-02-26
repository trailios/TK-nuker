import aiosonic, asyncio
from Functions import sendmessage

async def webhookspamm(channelid: int, amount: int, message: str, headers: dict):
    async with aiosonic.HTTPClient() as session:
        r = await session.post(f"https://discord.com/api/v9/channels/{channelid}/webhooks", headers=headers, json={"name": "Traili fucked you!!"})
        if r.status_code == 429:
            print("     Ratelimited..")
        else:
            if r.status_code in [200, 201, 204]:
                print("     Created webhook")
                json = await r.json()
                webhook = f"https://discord.com/api/webhooks/{json['id']}/{json['token']}"
                await asyncio.create_task(sendmessage(webhook, message, amount))
            else:
                print("     Error creating webhook")