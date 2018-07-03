import mmyCore as core
import discord
import emoji
import pickle
import random

async def rdmReact(message):
    e = emoji.random_emoji()[0]
    await core.react(message,e)

async def lvlReact(message):
    file = open("yylc.chr",'rb')
    users = pickle.load(file)
    p = users[message.author.mention][1] / 100
    file.close()

    if random.random() < p:
        await rdmReact(message)