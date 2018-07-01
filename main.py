# MommyYuri main script alpha 2
# written by Yuristep in tandem with Emiliarra

# important things
import random
import asyncio
import discord
import aiohttp
from discord.ext.commands import Bot

#bot API token
TOKEN = 'NDYyMzU1MzU5MTczMTgxNDU5.Dhi_aw.X2bocPGBJJAzBGPM8mMA7je0Q3A'

#variables to separate bot commands from discord client commands
client = discord.Client()
botclient = Bot(command_prefix='!')

# dictionary of chat commands
# bot is currently BROKEN with these active as the commands have not been implemented yet
#chatdict = {
#    "!hello": hello(),
#    "!insult": insult(),
#    "!love": love(),
#    "!hug": hug(),
#    "!smut": smut(),
#    "!fap": fap(),
#    "!music": music()
#}



# change status to current game (not working for fuckall reasons)
@client.event
# wait until server is up then execute
async def wait_until_ready():
    await client.change_presence('',game=discord.Game(name='YYLC'))

# !Hello command - says hello
@client.event
# wait until message is sent on any of the bot's monitored channels
async def on_message(message):
    # prevent bot from replying to itself
    if message.author == client.user:
        return
    # says hello to requested user with a mention
    if message.content.startswith('!hello'):
        msg = 'Hello there, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


# prints information to console window when bot is connected and active
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot functionality now active!')
    print('------')
    

#start bot command with API token
client.run(TOKEN)

