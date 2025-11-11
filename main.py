import requests
from telegram import Bot
import os
import time

# --- Telegram ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL")
bot = Bot(token=BOT_TOKEN)

# --- Pocket Option API ---
PO_API_URL = "wss://chat-po.site/cabinet-client/socket.io/?EIO=4&transport=websocket" 
PO_API_KEY = os.getenv("40527f1167b31e5240fc7c2b174589ce")

def get_signals():
    headers = {"Authorization": f"Bearer {PO_API_KEY}"}
    response = requests.get(PO_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()  
    else:
        print("Ошибка API:", response.status_code)
        return []

print("✅ Бот запущен и слушает API...")

while True:
    try:
        signals = get_signals()
        for s in signals:
            msg = f"💹 Сигнал: {s['pair']} ➜ {s['direction']} ({s['timeframe']})"
            bot.send_message(chat_id=CHANNEL, text=msg)
        time.sleep(60)  
    except Exception as e:
        print("Ошибка:", e)
        time.sleep(10)
