import os
import discord
import random
import asyncio
import aiohttp
from discord.ext.commands import Bot

from mmyLevel import * 
from mmyLines import *
from mmyAdmin import *
from mmyPics import *
from mmyAi import *

client = discord.Client()

"""
    Basic Commands
"""

async def reply(msgIn, msgOut):
    await client.send_message(msgIn, msgOut)

async def react(msgIn, react):
    await client.add_reaction(msgIn,react)

async def randomLine(msgIn, niceFile, nastyFile, mentionUser = False, formatVar = False):    
    if await checkRole(msgIn, "Degenerate"):
        file = open(nastyFile, 'r')
    else:
        file = open(niceFile , 'r')
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    msg = random.choice(lines)

    msg = msg.replace("<br>",'\n')

    if formatVar:
        msg = msg.format(formatVar)

    if mentionUser:
        msg = msgIn.author.mention + " " + msg

    await reply(msgIn.channel, msg)

async def randomPic(message, path):
    files = os.listdir(path)
    await client.send_file(message.channel, path + random.choice(files))

async def checkRole(msgIn, roleName, failMessage = False):
    if roleName not in [y.name for y in msgIn.author.roles]:
        if failMessage:
            await reply(msgIn.channel, failMessage)
        return False
    return True

#removes role for sub content
async def nice(message):
    role = discord.utils.get(message.server.roles, name="Degenerate")
    await client.remove_roles(message.author, role)
    await reply(message.channel, message.author.mention + " aww I'm sorry if I was mean to you, I'll be nicer now.")

#adds role for sub content
async def nasty(message):
    role = discord.utils.get(message.server.roles, name="Degenerate")
    await client.add_roles(message.author, role)
    await client.send_message(message.channel, message.author.mention + " is now my bitch.")     
    

# prints information to console window when bot is connected and active
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot functionality now active!')
    print('------')

    await client.change_presence(game=discord.Game(name='YYLC', type=0))

@client.event
# wait until message is sent on any of the bot's monitored channels
async def on_message(message):
    await stats(message)
    command = message.content + ' '
    command = command[:command.index(' ')]
    # prevent bot from replying to itself and check dictionary key is valid
    if message.author == client.user:
        return
    if command not in chatdict.keys():
        await lvlReact(message)
        await lvl(message)
        return
    await chatdict[command](message)

async def help2(message):
    msg = """Here's a list of commands you can use to interact with me:\n```
            !help: display this help message\n
            !hello: have me ping you\n
            !sub: submit to me, get insulted gently or harshly if you have the Degenerate role\n
            !dom: dominate me, harshly if you have the Degenerate role\n
            !nasty: gain the Degenerate role, be treated harshly by me\n
            !nice: remove the Degenerate role, be treated nicely by me\n
            !exp: check your stats such as your EXP and level on the server\n
            !compliment: recieve a nice compliment from me whether or not you're a Degenerate\n
            !magic8ball: recieve an answer from the beyond\n
            !pick: have me pick between things, either seperated by spaces or using quotation marks\n
            !pic: search for an (often) SFW picture on Danbooru with up to 2 space separated tags\n
            !lewd: search for a NSFW picture on Danbooru with up to 2 space separated tags\n
            !react: I will react your message with a random emoji regardless of your level\n
            !hug: hug a pinged user\n
            !headpat: headpat a pinged user\n
            !step_on: step on a pinged user```"""
    
    await reply(message.channel, msg)
    

#Function Dictionary
chatdict = {
    "!help" : help2,
    "!hello" : hello,
    "!sub" : sub,
    "!dom" : dom,
    "!admin_clrdata" : admin_clrdata,
    "!admin_kill" : admin_kill,
    "!admin_lvlmod" : admin_lvlmod,
    "!admin_python" : admin_python,
    "!nasty" : nasty,
    "!nice" : nice,
    "!exp" : exp,
    "!compliment" : compliment,
    "!magic8ball" : magic8ball,
    "!pick" : pick,
    "!milk" : milk,
    "!react" : rdmReact,
    "!lewd" : lewd,
    "!pic" : pic,
    "!hug" : hug,
    "!step_on" : step,
    "!headpat" : headpat,
    "!dice" : dice
} 