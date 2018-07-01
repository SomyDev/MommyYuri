# MommyYuri main script alpha 2
# written by Yuristep in tandem with Emiliarra

#Spaghetti Western Code Edition

# important things
import random
import math
import pickle
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

#WIP Dom lines
async def dom(message):
    msg = "'I'll fukin get round to it, pls be patient' - SOMY \<3"
    await client.send_message(message.channel, msg)

#Deletes EXP tracking data
async def clrdata(message):
    if "YY,LLC Exec" not in [y.name for y in message.author.roles]:
        msg = "ur hacking is shit lol"
        await client.send_message(message.channel, msg)
        return

    file = open("yylc.chr","wb")
    pickle.dump(dict(),file)
    file.close()
    msg = "```yylc.chr has been deleted```"
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

#Tracks level and EXP per message
async def lvl(message):
    #Open YYLC EXP tracker CSV file for all IO
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)
    
    if message.author.mention not in users.keys():
        users[message.author.mention] = [0,0]

    #Update EXP
    users[message.author.mention][0] += 10

    #Calculate level as per L = E^2 + 2
    lvl = round(abs(users[message.author.mention][0] / 2) ** 0.33)

    lvlupdate = False

    #If level has increased after EXP update, flag to inform user, update level
    if lvl > users[message.author.mention][1]:
        users[message.author.mention][1] = lvl
        lvlupdate = True
    
    file.close()
    file = open("yylc.chr", 'wb')
    #Update pickle
    pickle.dump(users,file)

    file.close()
    
    if lvlupdate:
        file = open("lvlup.txt", 'r')
        lines = []
        for line in file:
            lines.append(line)
        file.close()

        msg = random.choice(lines)
        await client.send_message(message.channel, message.author.mention + " " + msg.format(lvl))

#Shows user EXP stats
async def exp(message):
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)
    
    if message.author.mention not in users.keys():
        users[message.author.mention] = [0,0]

    file.close()
    msg = message.author.mention + ", you are Level " + str(users[message.author.mention][1]) + " and currently have " + str(users[message.author.mention][0]) + " EXP."
    await client.send_message(message.channel, msg)

#pics
async def pic(message):
    files = os.listdir('pic/')
    await client.send_file(message.channel, "pic/" + random.choice(files))

#feet
async def feet(message):
    files = os.listdir('feet/')
    await client.send_file(message.channel, "feet/" + random.choice(files))

#removes role for sub content
async def nice(message):
    role = discord.utils.get(message.server.roles, name="Degenerate")
    await client.remove_roles(message.author, role)

    await client.send_message(message.channel, message.author.mention + " aww I'm sorry if I was mean to you, I'll be nicer now.")    

#adds role for sub content
async def nasty(message):
    role = discord.utils.get(message.server.roles, name="Degenerate")
    await client.add_roles(message.author, role)

    await client.send_message(message.channel, message.author.mention + " is now my bitch.")    


#WIP Dictionary (temporarily omitted hello because of Emiliarra's instance)
chatdict = {
    #"!hello" : hello,
    "!sdev" : sdev,
    "!sub" : sub,
    "!dom" : dom,
    "!pic" : pic,
    "!feet" : feet,
    "!admin_clrdata" : clrdata,
    "!nasty" : nasty,
    "!nice" : nice,
    "!exp" : exp
}

@client.event
# wait until message is sent on any of the bot's monitored channels
async def on_message(message):
    command = message.content + ' '
    command = command[:command.index(' ')]
    # prevent bot from replying to itself and check dictionary key is valid
    if message.author == client.user:
        return
    await lvl(message)
    if command not in chatdict.keys():
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

