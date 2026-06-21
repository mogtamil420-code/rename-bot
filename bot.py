from pyrogram import Client, filters

API_ID = 123456
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("renamebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document)
async def rename_file(client, message):
    file_name = message.document.file_name
    new_name = "Renamed_" + file_name

    file_path = await message.download()

    await message.reply_document(
        file_path,
        file_name=new_name
    )

app.run()
