# main.py

from tactics import *
from image_trigger import can_trigger
from bot.telegram_bot import notify
from log.log_tool import write_log
from config import DEFAULT_SYMBOL
import time

# 模擬三根K棒資料（實戰中請改為API取得）
def get_latest_candles():
    return [
        {
            'open': 0.066, 'high': 0.069, 'low': 0.065, 'close': 0.068,
            'volume': 100000, 'body': 0.002, 'prev_body': 0.0015, 'prev_volume': 95000, 'upper_shadow': 0.001,
        },
        {
            'open': 0.068, 'high': 0.072, 'low': 0.067, 'close': 0.071,
            'volume': 125000, 'body': 0.003, 'prev_body': 0.002, 'prev_volume': 100000, 'upper_shadow': 0.0012,
        },
        {
            'open': 0.071, 'high': 0.073, 'low': 0.070, 'close': 0.072,
            'volume': 132000, 'body': 0.0015, 'prev_body': 0.003, 'prev_volume': 125000, 'upper_shadow': 0.0018,
        },
    ]

# 請替換為實際的 Telegram chat_id
CHAT_ID = 'YOUR_CHAT_ID'

def main():
    candles = get_latest_candles()
    symbol = DEFAULT_SYMBOL

    # 只分析最後一根（搭配前兩根判斷）
    latest_candle = candles[-1]

    if detect_entry_candle(latest_candle) and can_trigger("上車"):
        notify(CHAT_ID, "上車", f"{symbol} 上車機會")
        write_log("上車", symbol, latest_candle)

    elif detect_exit_signal(latest_candle) and can_trigger("下車"):
        notify(CHAT_ID, "下車", f"{symbol} 下車警示")
        write_log("下車", symbol, latest_candle)

    elif detect_prepare_switch(latest_candle) and can_trigger("準備換車"):
        notify(CHAT_ID, "準備換車", f"{symbol} 多空轉折警示")
        write_log("準備換車", symbol, latest_candle)

    elif detect_prepare_exit(latest_candle) and can_trigger("準備下車"):
        notify(CHAT_ID, "準備下車", f"{symbol} 趨勢轉弱提醒")
        write_log("準備下車", symbol, latest_candle)

if __name__ == "__main__":
    main()
