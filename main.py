# MommyYuri main script alpha 2
# written by Yuristep in tandem with Emiliarra

#Spaghetti Western Code Edition

# important things
import asyncio
import discord
import aiohttp

from mmyCore import *


if __name__ == "__main__":
    #bot API token
    TOKEN = 'NDYyMzU1MzU5MTczMTgxNDU5.Dhi_aw.X2bocPGBJJAzBGPM8mMA7je0Q3A'

    #variables to separate bot commands from discord client commands
    botclient = Bot(command_prefix='!')
    botclient.remove_command('help')


    #start bot command with API token
    client.run(TOKEN)

