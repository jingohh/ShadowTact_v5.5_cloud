# trigger/image_trigger.py

import time
from config import COOLDOWN_SECONDS

# 單圖冷卻紀錄（每個貼圖各自冷卻）
last_trigger_time = {
    "上車": 0,
    "下車": 0,
    "準備換車": 0,
    "準備下車": 0,
}

# 全域冷卻：控制整體貼圖頻率（避免短時間內連續出圖）
last_global_trigger = 0
GLOBAL_COOLDOWN = 90  # 秒數：例如 90 秒內最多出一張圖

def can_trigger(tag):
    global last_global_trigger

    now = time.time()
    last_tag_time = last_trigger_time.get(tag, 0)

    # 若全域冷卻未滿，禁止任何貼圖
    if now - last_global_trigger < GLOBAL_COOLDOWN:
        return False

    # 若該圖冷卻未滿，也不能發
    if now - last_tag_time < COOLDOWN_SECONDS:
        return False

    # 通過兩層條件，更新時間
    last_trigger_time[tag] = now
    last_global_trigger = now
    return True
