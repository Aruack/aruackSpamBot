

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from ARUACK-SPAM-BOT.utils import load_plugins
import logging
from telethon import events
from . import Aru, Aru2, Aru3, Aru4, Aru5, Aru6, Aru7, Aru8, Aru9, Aru10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "ARUACK-SPAM-BOT/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("ᴀʀᴜᴀᴄᴋ ꜱᴘᴀᴍ ʙᴏᴛ Sᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇᴘʟᴏʏᴇD -!")
print("Eɴᴊᴏʏ! ᴅᴏ ᴠɪꜱɪT! @aruacksupport")

if __name__ == "__main__":
    Aru.run_until_disconnected()
    
if __name__ == "__main__":
    Aru2.run_until_disconnected()

if __name__ == "__main__":
    Aru3.run_until_disconnected()
    
if __name__ == "__main__":
    Aru4.run_until_disconnected()

if __name__ == "__main__":
    Aru5.run_until_disconnected()
    
if __name__ == "__main__":
    Aru6.run_until_disconnected()
    
if __name__ == "__main__":
    Aru7.run_until_disconnected()

if __name__ == "__main__":
    Aru8.run_until_disconnected()
    
if __name__ == "__main__":
    Aru9.run_until_disconnected()

if __name__ == "__main__":
    Aru10.run_until_disconnected()    
