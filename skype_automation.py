from skpy import Skype
import os.path

sklogin = Skype('rhrahdi@gmail.com', '123456789')

# -- Uncomment to explore only one at a time --

# ---------for viewing all contacts
#contact = sklogin.contacts
#for i in contact:
#    print(i)

#---------- for sending message
#contact = sklogin.contacts['live:.cid.56656569565']
#contact.chat.sendMsg('hello')

# -------- create group ----
#group = sklogin.chats.create(['id, id, id, id'])

# --------- sending image------
#ch = sklogin.contacts["id"]
#with open('path/image.png', 'rb') as f:
#    ch.chat.sendFile(f, 'image.png', image=True)
