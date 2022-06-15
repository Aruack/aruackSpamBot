import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Aru, Aru2, Aru3, Aru4, Aru5, Aru6, Aru7, Aru8, Aru9, Aru10, ALIVE_PIC, OWNER_ID
from ARUACK-SPAM-BOT.plugins.help import *


ARUACK_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/409e040b3f4a0c09dc701.jpg"

ARUACK_Button = [
        [
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/aruacksupport")
        ],
        [
        Button.inline("• ᴄᴍᴅs •", data="help_back")
        ]
        ]
               
ARUACK_Button = [
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/aruackofficial"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/aruacksupport")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/aruack/AruackSpamBot")
        ]
        ]
        
        
#USERS 


@Aru.on(events.NewMessage(pattern="/start"))
@Aru2.on(events.NewMessage(pattern="/start"))
@Aru3.on(events.NewMessage(pattern="/start"))
@Aru4.on(events.NewMessage(pattern="/start"))
@Aru5.on(events.NewMessage(pattern="/start"))
@Aru6.on(events.NewMessage(pattern="/start"))
@Aru7.on(events.NewMessage(pattern="/start"))
@Aru7.on(events.NewMessage(pattern="/start"))
@Aru8.on(events.NewMessage(pattern="/start"))
@Aru9.on(events.NewMessage(pattern="/start"))
@Aru10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       AruBot = await event.client.get_me()
       bot_id = AruBot.first_name
       bot_username = AruBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheARUACK = event.chat_id
       firstname = replied_user.user.first_name
       ownermsg = f"**Hi Master, Its me {bot_id}, Your Spam Bot !! \n\n Click Below Buttons For help**"
       usermsg = f"**Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull Spam Bot.** \n\n**If You Want Your Own Spam Bots You Can Deploy From Button Below.** \n\n**𝐏𝐎𝐖𝐄𝐑𝐄𝐃 𝐁𝐘 [𝐑𝐈𝐙𝐎𝐄𝐋 𝐗](https://t.me/ARUACKX)**"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(TheARUACK,
                  ARUACK_IMG,
                  caption=ownermsg, 
                  buttons=ARUACK_Button)
       else:
            await event.client.send_file(TheARUACK,
                  ARUACK_IMG,
                  caption=usermsg, 
                  buttons=ARUACK_Button)
                

