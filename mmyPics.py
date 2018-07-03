import os
import requests
import mmyCore as core
from pybooru import Danbooru, Moebooru

#booru
async def lewd(message, attempts = 0):
    if attempts == 5:
        return

    try:
        query = message.content[message.content.index(' ') + 1:]
        
        bclient = Danbooru('danbooru')
        pic = bclient.post_list(tags=query, random=True)
        try:
            fileurl = pic[0]['file_url']
        except:
            fileurl = pic[0]['source']  
    except:
        await lewd(message, attempts + 1)
    
    await core.reply(message.channel, fileurl)

async def pic(message, attempts = 0):
    if attempts == 5:
        return

    try:
        query = message.content[message.content.index(' ') + 1:]
        
        bclient = Danbooru('danbooru')
        pic = bclient.post_list(tags=query, random=True, rating = "safe", is_rating_locked = 1)
        try:
            fileurl = pic[0]['file_url']
        except:
            fileurl = pic[0]['source']  
    except:
        await lewd(message, attempts + 1)
    
    await core.reply(message.channel, fileurl)

async def interact(message, action, tags):
    target = message.content.split(' ')[1]
    await core.reply(message.channel, target + " has been " + action + " by " + message.author.mention + "!")
    message.content = tags
    await lewd(message)

async def hug(message):
    await interact(message, "hugged", "!dummy couple hug")

async def step(message):
    await interact(message, "stepped on", "!dummy stepped_on")

async def headpat(message):
    await interact(message, "headpat", "!dummy petting")

