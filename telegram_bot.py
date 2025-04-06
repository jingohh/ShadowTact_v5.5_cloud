# bot/telegram_bot.py

import requests
from config.config import TELEGRAM_TOKEN, STICKERS, SIGNATURE, ENABLE_IMAGE_MODE, ENABLE_TEXT_MODE

def send_sticker(chat_id, tag):
    if not ENABLE_IMAGE_MODE:
        return

    sticker_id = STICKERS.get(tag)
    if not sticker_id:
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendSticker"
    data = {
        "chat_id": chat_id,
        "sticker": sticker_id
    }
    requests.post(url, data=data)

def send_message(chat_id, text, tag="判斷"):
    if not ENABLE_TEXT_MODE:
        return

    full_text = f"{text} {SIGNATURE.get(tag, '')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": full_text
    }
    requests.post(url, data=data)

def notify(chat_id, action_tag, text=None):
    """
    發送貼圖與訊息綜合通知介面
    action_tag: '上車' / '下車' / '準備換車' / '準備下車'
    """
    send_sticker(chat_id, action_tag)
    if text:
        send_message(chat_id, text, tag="判斷")