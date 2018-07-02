import pickle
import mmyCore as core

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
        await core.randomLine(message, "nicelevel.txt", "nastylevel.txt", True, lvl)

#Shows user EXP stats
async def exp(message):
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)
    
    if message.author.mention not in users.keys():
        users[message.author.mention] = [0,0]

    file.close()
    msg = message.author.mention + ", you are Level " + str(users[message.author.mention][1]) + " and currently have " + str(users[message.author.mention][0]) + " EXP."
    await core.reply(message.channel, msg)