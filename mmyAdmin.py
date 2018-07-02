import mmyCore as core
import pickle
import os
import ast

#Deletes EXP tracking data
async def admin_clrdata(message):
    if not await core.checkRole(message, "YY,LLC Exec", "```Access Denied```"):
        return

    file = open("yylc.chr","wb")
    pickle.dump(dict(),file)
    file.close()
    msg = "```yylc.chr has been deleted```"
    await core.reply(message.channel, msg)

async def admin_kill(message):
    if not await core.checkRole(message, "YY,LLC Exec", "```Access Denied```"):
        return

    msg = "```Killing all instances of main.py...```"
    await core.reply(message.channel, msg)
    os._exit(1)       

async def admin_lvlmod(message):
    if not await core.checkRole(message, "YY,LLC Exec", "```Access Denied```"):
        return
    
    file = open("yylc.chr", 'rb')
    users = pickle.load(file)

    target = message.content.split(' ')[1]
    level = int(message.content.split(' ')[2]) 
    
    users[target] = [level**3 * 2,level // 10 * 10]

    file.close()
    file = open("yylc.chr", 'wb')
    #Update pickle
    pickle.dump(users,file)

    file.close()

    msg = "```" + target + " is now level " + str(level) + "```"
    await core.reply(message.channel, msg)

async def admin_python(message):
    if not await core.checkRole(message, "YY,LLC Exec", "```Access Denied```"):
        return

    try:
        msg = ast.literal_eval(message.content[message.content.index(' ') + 1:])
    except:
        msg = "Invalid syntax, only limited python syntax is accepted for security purposes"

    await core.reply(message.channel, "```" + str(msg) + "```")
   

    