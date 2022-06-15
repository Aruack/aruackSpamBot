from ARUACK-SPAM-BOT import Aru, Aru2, Aru3, Aru4, Aru5, Aru6, Aru7, Aru8, Aru9, Aru10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from ARUACK-SPAM-BOT import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/409e040b3f4a0c09dc701.jpg"

ARUACK_Help = "__Click On Below Buttons for help__"


@Aru.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Aru10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=ARUACK_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/aruackofficial")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> : Owner Cmd

**Echo**: To Active Echo On Any User
command:
i) {hl}addecho <reply to user>
ii) {hl}rmechk <reply to user>

**Leave**: To Leave Group/channel
command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @aruackofficial**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**raid:** Activates raid on any individual user for given range.
command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates raid on any individual user for given range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**replyraid:** Activates Reply Raid on the user!!
command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**dreplyraid:** Deactivates reply raid on the user!!
command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @aruackofficial**
"""

spam_msg = f"""
**Help Spam Cmds**

**spam**: Spams a message for given counter(<= 100).
command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**bigspam**: Spams a message for given counter.
command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**delayspam**: Delay spam a text for given counter after given time.
command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**pornspam**: Pornography Spam.
command:
i) {hl}pornspam <count>

**hang**: Spams hanging message for given counter.
command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @aruackofficial**
"""                     
           
           
@Aru.on(events.CallbackQuery(pattern=r"help_back"))
@Aru2.on(events.CallbackQuery(pattern=r"help_back"))
@Aru3.on(events.CallbackQuery(pattern=r"help_back"))
@Aru4.on(events.CallbackQuery(pattern=r"help_back"))
@Aru5.on(events.CallbackQuery(pattern=r"help_back"))
@Aru6.on(events.CallbackQuery(pattern=r"help_back"))
@Aru7.on(events.CallbackQuery(pattern=r"help_back"))
@Aru8.on(events.CallbackQuery(pattern=r"help_back"))
@Aru9.on(events.CallbackQuery(pattern=r"help_back"))
@Aru10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            ARUACK_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra cmds", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/aruackofficial")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own ᴀʀᴜᴀᴄᴋ ꜱᴘᴀᴍ ʙᴏᴛ !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Aru.on(events.CallbackQuery(pattern=r"spam"))
@Aru2.on(events.CallbackQuery(pattern=r"spam"))
@Aru3.on(events.CallbackQuery(pattern=r"spam"))
@Aru4.on(events.CallbackQuery(pattern=r"spam"))
@Aru5.on(events.CallbackQuery(pattern=r"spam"))
@Aru6.on(events.CallbackQuery(pattern=r"spam"))
@Aru7.on(events.CallbackQuery(pattern=r"spam"))
@Aru8.on(events.CallbackQuery(pattern=r"spam"))
@Aru9.on(events.CallbackQuery(pattern=r"spam"))
@Aru10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own ᴀʀᴜᴀᴄᴋ ꜱᴘᴀᴍ ʙᴏᴛ !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Aru.on(events.CallbackQuery(pattern=r"raid"))
@Aru2.on(events.CallbackQuery(pattern=r"raid"))
@Aru3.on(events.CallbackQuery(pattern=r"raid"))
@Aru4.on(events.CallbackQuery(pattern=r"raid"))
@Aru5.on(events.CallbackQuery(pattern=r"raid"))
@Aru6.on(events.CallbackQuery(pattern=r"raid"))
@Aru7.on(events.CallbackQuery(pattern=r"raid"))
@Aru8.on(events.CallbackQuery(pattern=r"raid"))
@Aru9.on(events.CallbackQuery(pattern=r"raid"))
@Aru10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own ᴀʀᴜᴀᴄᴋ ꜱᴘᴀᴍ ʙᴏᴛ !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Aru.on(events.CallbackQuery(pattern=r"extra"))
@Aru2.on(events.CallbackQuery(pattern=r"extra"))
@Aru3.on(events.CallbackQuery(pattern=r"extra"))
@Aru4.on(events.CallbackQuery(pattern=r"extra"))
@Aru5.on(events.CallbackQuery(pattern=r"extra"))
@Aru6.on(events.CallbackQuery(pattern=r"extra"))
@Aru7.on(events.CallbackQuery(pattern=r"extra"))
@Aru8.on(events.CallbackQuery(pattern=r"extra"))
@Aru9.on(events.CallbackQuery(pattern=r"extra"))
@Aru10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own ᴀʀᴜᴀᴄᴋ ꜱᴘᴀᴍ ʙᴏᴛ !!"
            )
        await event.answer(Alert, cache_time=0, alert=True)

