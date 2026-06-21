import os
import asyncio
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client(
    "renamebot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    workers=1
)

@app.on_message(filters.command("start"))
async def start(client, message):
    print("START RECEIVED")
    await message.reply("✅ Bot is alive")

@app.on_message(filters.all)
async def allmsg(client, message):
    print("MESSAGE:", message.text or message.caption or "FILE")
    await message.reply("✅ Received")

async def main():
    print("STARTING BOT...")
    await app.start()
    print("BOT CONNECTED TO TELEGRAM")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
