import os
import requests
import mmyCore as core
#from Pybooru import Danbooru

#pics
async def pic(message):
    await core.randomPic(message, 'pic/')

#feet
async def feet(message):
    await core.randomPic(message, 'feet/')

"""#booru
async def booru(message):
    query = message.content[message.content.index(' ') + 1:]
    
    bclient = Danbooru('danbooru')
    pic = bclient.post_list(tags=query, limit=1)
    try:
        fileurl = 'https://danbooru.donmai.us' + pic[0]['file_url']
    except:
        fileurl = 'https://danbooru.donmai.us' + pic[0]['source']

    file = open("tmp.jpg", 'wb')
    response = requests.get("Image path: {0}".format(post['file_url']), stream=True)

    if not response.ok:
        print response

    for block in response.iter_content(1024):
        if not block:
            break

        file.write(block)"""