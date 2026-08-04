import asyncio
import json
import logging
from pyrogram import Client

API_ID = 38875417
API_HASH = "f079b800a9b2f0009e474bd3bb8300e9"
BOT_TOKEN = "8800268651:AAGKQ7YSHjUeuf_ox-D12fVYDR2GVgrO_GU"
CHANNEL = "@NLS_music"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Client(
    "nls_music_indexer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def index_channel():
    tracks = []
    count = 0
    audio_count = 0

    logger.info(f"Start indexing {CHANNEL}")

    async for message in app.get_chat_history(CHANNEL):
        count += 1

        if count % 1000 == 0:
            logger.info(f"Processed {count} messages")

        if message.audio:
            audio_count += 1
            tracks.append({
                "file_id": message.audio.file_id,
                "titre": message.audio.title or "Inconnu",
                "artiste": message.audio.performer or "Inconnu",
                "date": str(message.date),
                "taille": message.audio.file_size,
                "duree": message.audio.duration,
                "message_id": message.id
            })

        if count % 200 == 0:
            await asyncio.sleep(0.5)

    with open("telegram_tracks.json", "w", encoding="utf-8") as f:
        json.dump(tracks, f, ensure_ascii=False, indent=2)

    logger.info(f"Done. Messages: {count}, Audio: {audio_count}, Tracks: {len(tracks)}")

async def main():
    async with app:
        await index_channel()

if __name__ == "__main__":
    asyncio.run(main())
