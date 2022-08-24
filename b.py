import discord, os, time, json, asyncio
from discord.ext import commands
from discord.ext import tasks
from discord import Message
from discord import DMChannel

command = "leave"
leftmsg = "Group leaver - https://github.com/kWAYTV"

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
intro = f"""
═════════════════════════════════════════════════════════════════════════════════════
 ____ ____ ____ ____ ____ _________ ____ ____ ____ ____ ____ ____ 
||G |||r |||o |||u |||p |||       |||L |||e |||a |||v |||e |||r ||
||__|||__|||__|||__|||__|||_______|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|/__\|
═════════════════════════════════════════════════════════════════════════════════════

https://github.com/kWAYTV
"""

def slow_type(text, speed, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

sCount = 0
def rsCount():
    sCount = 0


def check_config():
    try:
        with open("config.json") as f:
            config = json.load(f)
    except FileNotFoundError:
        with open("config.json", "w") as f:
            config = {
                "userdata": {
                    "token": "null",
                    "prefix": "null",
                }
            }
            json.dump(config, f)
    return


check_config()
with open("config.json", "r") as config_file:
    config = json.load(config_file)

    token = config["userdata"]["token"]
    prefix = config["userdata"]["prefix"]

def config_filled():
    global token, prefix
    if token == "null":
        clear()
        slow_type("Please input your token: ", 0.001)
        token = input()
        update = {
                "userdata": {
                    "token": token,
                    "prefix": "null",
                }}

        token = token
        config.update(update)
        with open("config.json", "w") as jsfile:
            json.dump(config, jsfile)
            jsfile.close()
        clear()
        slow_type("Token updated!", 0.001)
    if prefix == "null":
        clear()
        slow_type("Please input your prefix: ", 0.001)
        prefix = input()
        update = {
                "userdata": {
                    "token": token,
                    "prefix": prefix,
                }}

        prefix = prefix
        config.update(update)
        with open("config.json", "w") as jsfile:
            json.dump(config, jsfile)
            jsfile.close()
        clear()
        slow_type("Prefix updated!", 0.001)

client = discord.Client()
@client.event
async def on_ready():
    clear()
    rsCount()
    slow_type(intro, 0.001)
    slow_type('Logged in as '+f'{client.user.name}#{client.user.discriminator}!'+" Type " + prefix + "" + "leave" + " in to any chat and the script will execute!", 0.001)

@client.event
async def on_message(message):
    global sCount
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count+1
                        await channel.send(leftmsg)
                        await channel.leave()
                        slow_type("Left a group: " + str(channel.id), 0.001)
                        os.system(f"title Group leaver - {count} groups left")
            await message.channel.send(f"**Finished!**\n{str(count)} groups left! Exiting...")
            time.sleep(3)
            exit()

config_filled()
client.run(token, bot=False)
slow_type("Press enter to close", 0.001)
input()
time.sleep(3)
exit()