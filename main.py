# MommyYuri main script alpha 2
# written by Yuristep in tandem with Emiliarra

# important things
import random
import glob
import os
import Cython
import asyncio
import discord
import aiohttp
from discord.ext.commands import Bot

#bot API token
TOKEN = 'NDYyMzU1MzU5MTczMTgxNDU5.Dhi_aw.X2bocPGBJJAzBGPM8mMA7je0Q3A'

#variables to separate bot commands from discord client commands
client = discord.Client()
botclient = Bot(command_prefix='!')

"""
    Basic Commands
"""

#Says hello
async def hello(message):
    msg = 'Hello there, {0.author.mention}'.format(message)
    await client.send_message(message.channel, msg)

#This function was just used to confirm I could run my own instance of MommyYuri
async def sdev(message):
    msg = "```Command execution from SomyDev's terminal was successful```"
    await client.send_message(message.channel, msg)

#This function was just used to confirm I could run my own instance of MommyYuri
async def dom(message):
    msg = "'I'll fukin get round to it, pls be patient' - SOMY \<3"
    await client.send_message(message.channel, msg)

#Picks a random line from insults.txt and messages it
async def sub(message):
    file = open("insults.txt", 'r')
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    msg = random.choice(lines)
    await client.send_message(message.channel, msg)   

#pics
async def pic(message):
    files = os.listdir('pic/')
    await client.send_file(message.channel, "pic/" + random.choice(files))

async def feet(message):
    files = os.listdir('feet/')
    await client.send_file(message.channel, "feet/" + random.choice(files))


#WIP Dictionary (temporarily omitted hello because of Emiliarra's instance)
chatdict = {
    #"!hello" : hello,
    "!sdev" : sdev,
    "!sub" : sub,
    "!dom" : dom,
    "!pic" : pic,
    "!feet" : feet
}

@client.event
# wait until message is sent on any of the bot's monitored channels
async def on_message(message):
    command = message.content + ' '
    command = command[:command.index(' ')]
    # prevent bot from replying to itself and check dictionary key is valid
    if message.author == client.user or command not in chatdict.keys():
        return
    await chatdict[command](message)
    


# prints information to console window when bot is connected and active
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot functionality now active!')
    print('------')

    await client.change_presence(game=discord.Game(name='YYLC', type=0))
    

#start bot command with API token
client.run(TOKEN)

