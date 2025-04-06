# config/config.py

# Telegram Bot Token（如果要更換，直接改這裡）
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Telegram 貼圖 ID（請使用你自己擷取的貼圖 file_id）
STICKERS = {
    "上車": "STICKER_ID_FOR_ENTRY",
    "下車": "STICKER_ID_FOR_EXIT",
    "準備換車": "STICKER_ID_FOR_PREP_SWITCH",
    "準備下車": "STICKER_ID_FOR_PREP_EXIT",
}

# 冷卻時間設定（秒）
COOLDOWN_SECONDS = 600  # 每張圖至少 10 分鐘內不會重複出現

# 幣種與週期設定（後續可支援多幣多週期）
DEFAULT_SYMBOL = "TRX/USDT"
DEFAULT_INTERVAL = "3m"

# 模式控制
ENABLE_IMAGE_MODE = True      # 是否啟用貼圖
ENABLE_TEXT_MODE = True       # 是否同時發送文字
DEBUG_MODE = False            # 除錯模式可看 log

# 通知簽章
SIGNATURE = {
    "判斷": "#影子判斷",
    "預測": "#影子預測"
}
