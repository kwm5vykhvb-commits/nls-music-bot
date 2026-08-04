from pyrogram import Client
import logging

# TES identifiants (à remplacer par des variables d'environnement sur Render)
API_ID = 38875417
API_HASH = "f079b800a9b2f0009e474bd3bb8300e9"
BOT_TOKEN = "8800268651:AAGKQ7YSHjUeuf_ox-D12fVYDR2GVgrO_GU"
CHANNEL = "@NLS_music"

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialisation du client
app = Client(
    "nls_music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Commande /start
@app.on_message()
async def handle_message(client, message):
    if message.text and message.text.startswith("/start"):
        await message.reply(
            "✅ **Bot NLS Music en ligne !**\n\n"
            "Bot hébergé sur Render 24h/24.\n"
            "Channel : @NLS_music\n"
            "Contact : @ton_username"
        )

# Lancement du bot
if __name__ == "__main__":
    logger.info("🚀 Démarrage du bot...")
    try:
        app.run()
    except Exception as e:
        logger.error(f"❌ Erreur : {e}")
