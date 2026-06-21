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
    in_memory=True
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply("✅ Bot is working!\nSend me a file.")

@app.on_message(filters.document)
async def rename(_, message):
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

if __name__ == "__main__":
    asyncio.run(main())
