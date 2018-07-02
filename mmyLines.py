import mmyCore as core
import random

#Says hello
async def hello(message):
    msg = 'Hello there, {0.author.mention}'.format(message)
    await core.reply(message.channel, msg)

#Dom lines
async def dom(message):
    await core.randomLine(message, "nicedom.txt", "nastydom.txt")

#Picks a random line from insults.txt and messages it
async def sub(message):
    await core.randomLine(message, "nicesub.txt", "nastysub.txt")

async def compliment(message):
    await core.randomLine(message, "compl.txt", "compl.txt")

async def magic8ball(message):
    await core.randomLine(message, "magic8ball.txt", "magic8ball.txt")

async def pick(message):
    if message.content.find('"') == -1:
        options = message.content.split(' ')[1:]
    else:
        options = message.content.split('"')[1:]
        temp = []
        for i in range(len(options) // 2):
            temp.append(options[i] + options[i + 1])
            temp[-1] = temp[-1].replace('"','')
        options = temp
        
    msg = "I pick " + random.choice(options)
    await core.reply(message.channel, msg)