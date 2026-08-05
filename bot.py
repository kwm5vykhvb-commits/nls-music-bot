import logging
from pyrogram import Client, filters, idle

API_ID = 38875417
API_HASH = "f079b800a9b2f0009e474bd3bb8300e9"
BOT_TOKEN = "8800268651:AAGKQ7YSHjUeuf_ox-D12fVYDR2GVgrO_GU"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client(
    "nls_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply_text("✅ Bot NLS Music en ligne !")

async def main():
    await app.start()
    logger.info("Bot started")
    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(main())
