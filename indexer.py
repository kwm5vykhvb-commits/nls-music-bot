from pyrogram import Client
import json
import logging
import asyncio

# TES identifiants
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
    "nls_music_indexer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def index_channel():
    """Indexe tous les morceaux du channel @NLS_music"""
    tracks = []
    count = 0
    audio_count = 0
    
    logger.info(f"🔍 Début de l'indexation de {CHANNEL}...")
    
    try:
        async for message in app.get_chat_history(CHANNEL, limit=100000):
            count += 1
            
            if count % 1000 == 0:
                logger.info(f"📊 Progression : {count} messages traités")
            
            if message.audio:
                audio_count += 1
                track = {
                    "file_id": message.audio.file_id,
                    "titre": message.audio.title or "Inconnu",
                    "artiste": message.audio.performer or "Inconnu",
                    "date": str(message.date),
                    "taille": message.audio.file_size,
                    "duree": message.audio.duration,
                    "message_id": message.id
                }
                tracks.append(track)
            
            # Pause pour éviter le rate limit
            if count % 100 == 0:
                await asyncio.sleep(1)
    
    except Exception as e:
        logger.error(f"❌ Erreur pendant l'indexation : {e}")
    
    # Sauvegarder dans JSON
    with open("telegram_tracks.json", "w", encoding="utf-8") as f:
        json.dump(tracks, f, ensure_ascii=False, indent=2)
    
    logger.info(f"✅ Indexation terminée !")
    logger.info(f"📊 Total messages : {count}")
    logger.info(f"🎵 Total morceaux audio : {audio_count}")
    logger.info(f"💾 Fichier sauvegardé : telegram_tracks.json ({len(tracks)} pistes)")
    
    return tracks

if __name__ == "__main__":
    logger.info("🚀 Démarrage de l'indexation...")
    with app:
        app.loop.run_until_complete(index_channel())
