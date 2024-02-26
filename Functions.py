import aiosonic
from rgbprint import rgbprint, gradient_print

client = aiosonic.HTTPClient()

async def get_channels(guild: int, headers: dict):
    chanelIDS = []
    channels = await client.get(f"https://discord.com/api/v9/guilds/{guild}/channels", headers=headers)
    json = await channels.json()
    for channel in json:
        chanelIDS.append(channel["id"])
    return chanelIDS

async def get_members(guild: int, headers: dict):
    memberIDS = []
    members = await client.get(f"https://discord.com/api/v9/guilds/{guild}/members", headers=headers)
    json = await members.json()
    for member in json:
        memberIDS.append(member["user"]["id"])
    return memberIDS

async def sendmessage(webhook: str, message: str, amount: int):
    for _ in range(amount):
        await client.post(webhook, json={"content": message})

async def getroles(guild: int, headers: dict):
    roleIDS = []
    roles = await client.get(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers)
    json = await roles.json()
    for role in json:
        roleIDS.append(role["id"])
    return roleIDS