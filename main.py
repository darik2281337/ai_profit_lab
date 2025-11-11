import time
from telegram import Bot
from pocketoption_api import PocketOption
import os

# --- Настройки ---
PO_EMAIL = os.getenv("PO_EMAIL")
PO_PASSWORD = os.getenv("PO_PASSWORD")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")

bot = Bot(token=BOT_TOKEN)
api = PocketOption(PO_EMAIL, PO_PASSWORD)

print("✅ Бот запущен и слушает Pocket Option...")

while True:
    try:
        signals = api.get_signals()
        for s in signals:
            msg = f"💹 Сигнал: {s['pair']} ➜ {s['direction']} ({s['timeframe']})"
            bot.send_message(chat_id=CHANNEL, text=msg)
        time.sleep(60)
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(10)
