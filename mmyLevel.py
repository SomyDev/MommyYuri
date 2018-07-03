import pickle
import mmyCore as core

#Tracks level and EXP per message
async def lvl(message):
    #Open YYLC EXP tracker CSV file for all IO
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)

    if message.author.mention not in users.keys():
        users[message.author.mention] = [0,0] #EXP, Level

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

async def stats(message):
    file = open("yylc2.chr", 'rb')
    stats = pickle.load(file)

    if message.author.mention not in stats.keys():
        stats[message.author.mention] = [0,0,0,0] #Subs, Doms, Nice Msgs, Nasty Msgs

    if await core.checkRole(message,"Degenerate"):
        stats[message.author.mention][3] += 1
    else:
        stats[message.author.mention][2] += 1
    
    if message.content.split(' ')[0] == "!dom":
        stats[message.author.mention][1] += 1        

    if message.content.split(' ')[0] == "!sub":
        stats[message.author.mention][0] += 1   

    file.close()
    file = open("yylc2.chr", 'wb')
    #Update pickle
    pickle.dump(stats,file)

    file.close()


#Shows user EXP stats
async def exp(message):
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)
    file2 = open("yylc2.chr", 'rb')
    stats = pickle.load(file2)

    subr = -1
    domr = -1
    nicer = -1
    nastyr = -1
    
    if message.author.mention not in users.keys():
        users[message.author.mention] = [0,0]
    if message.author.mention not in stats.keys():
        stats[message.author.mention] = [0,0,0,0]
    else:
        subv = stats[message.author.mention][0]
        domv = stats[message.author.mention][1]
        nicev = stats[message.author.mention][2]
        nastyv = stats[message.author.mention][3]

        nicer = round(nicev / (nicev + nastyv) * 100)
        nastyr = round(nastyv / (nicev + nastyv) * 100)

        if subv + domv != 0:
            subr = round(subv / (subv + domv) * 100)
            domr = round(domv / (subv + domv) * 100)

    file.close()
    msg = message.author.mention + ", you are Level " + str(users[message.author.mention][1]) + " and currently have " + str(users[message.author.mention][0]) + " EXP."

    if max(subr,domr) > 0:
        if subr == domr:
            msg += "\nYou are equally submissive as you are dominant."
        elif subr > domr:
            msg += "\nYou are " + str(subr) + "% submissive."
        else:
            msg += "\nYou are " + str(domr) + "% dominant."

    if max(nicer,nastyr) > 0:
        if nicer == nastyr:
            msg += "\nYou don't have a preference about how nice I am."
        elif nicer > nastyr:
            msg += "\nYou are " + str(nicer) + "% into gentler kinks."
        else:
            msg += "\nYou are " + str(nastyr) + "% into extreme kinks."

    await core.reply(message.channel, msg)