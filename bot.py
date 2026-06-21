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

# /start handler
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("✅ Bot is alive!\nSend me a file to rename.")

# rename handler
@app.on_message(filters.document)
async def rename(client, message):
    file = message.document

    file_path = await message.download()

    new_name = "RENAMED_" + file.file_name

    await message.reply_document(
        file_path,
        file_name=new_name
    )

async def main():
    await app.start()
    print("BOT RUNNING")
    await asyncio.Event().wait()

asyncio.run(main())
