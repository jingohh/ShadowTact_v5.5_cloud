# log/log_tool.py

import os
import datetime

LOG_PATH = "log/logs.txt"

def write_log(tag, symbol, candle_data):
    """
    寫入判斷紀錄：貼圖類型、幣種、時間、K棒內容
    """
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message = f"[{now}] {symbol} - {tag}\n"
    message += f"Open: {candle_data['open']} | High: {candle_data['high']} | Low: {candle_data['low']} | Close: {candle_data['close']} | Vol: {candle_data['volume']}\n"
    message += "-" * 50 + "\n"

    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(message)
