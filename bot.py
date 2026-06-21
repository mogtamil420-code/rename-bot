import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.all)
async def debug(client, message):
    print("MESSAGE RECEIVED:", message.text or message.caption or "FILE")
    await message.reply("✅ I received your message")

async def main():
    await app.start()
    print("BOT STARTED")
    await asyncio.Event().wait()

asyncio.run(main())
