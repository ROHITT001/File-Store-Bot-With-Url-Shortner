import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "28421635"))
  API_HASH = os.environ.get("API_HASH", "a4856de5fec0b9b3601ff06425f3f58e
  ")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6947074831:AAHfx5XvS6p0BXjamh3mdIKtjaC6MMgM4x0")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "AnimePediaFile_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001970343871"))
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6657660775"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Filebot:Filebot@cluster0.1kdt8x3.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001991806323")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002093375923"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any File Or Video You Want. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🍁FɪʟᴇSᴛᴏʀᴇBᴏᴛ🍁]────⍟
│
├➥ My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├➥ Language: [Python 3](https://www.python.org)
│
├➥ Library: [Pyrogram](https://docs.pyrogram.org)
│
╰───────────────────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: (https://t.me/TeamAnimePedia)
 
 Working Hard To be Perfect 
 
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
