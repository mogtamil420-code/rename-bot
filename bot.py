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
    bot_token=BOT_TOKEN
)

@app.on_message(filters.document)
async def rename_file(client, message):
    file_name = message.document.file_name
    new_name = "Renamed_" + file_name

    file_path = await message.download()

    await message.reply_document(
        file_path,
        file_name=new_name
    )

# 🔥 FIX for Railway async issue
async def main():
    await app.start()
    print("Bot is running...")
    await asyncio.Event().wait()

asyncio.run(main())
