# tactics/tactics.py

def detect_entry_candle(candle):
    """
    判斷：上車機會（主升起點）
    打分條件：
        +1：紅K
        +1：爆量（大於前量 20%）
        +1：實體變長
        +1：上影線短（非假突破）
    回傳：需達3分以上才通過
    """
    score = 0
    if candle['close'] > candle['open']:
        score += 1
    if candle['volume'] > candle['prev_volume'] * 1.2:
        score += 1
    if candle['body'] > candle['prev_body']:
        score += 1
    if candle['upper_shadow'] < candle['body']:
        score += 1
    return score >= 3


def detect_exit_signal(candle):
    """
    判斷：下車訊號（主力撤退 or 假突破）
    打分條件：
        +1：黑K（轉弱）
        +1：實體變小
        +1：量縮
        +1：高檔吞噬（實體比前一根小很多）
    回傳：需達3分以上才通過
    """
    score = 0
    if candle['close'] < candle['open']:
        score += 1
    if candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    if candle['prev_body'] > 0 and (candle['body'] / candle['prev_body']) < 0.5:
        score += 1
    return score >= 3


def detect_prepare_switch(candle):
    """
    判斷：準備換車（高檔反轉可能）
    打分條件：
        +1：上影線過長
        +1：紅K但實體變弱
        +1：量縮或動能放緩
    回傳：需達2分以上才通過
    """
    score = 0
    if candle['upper_shadow'] > candle['body'] * 1.5:
        score += 1
    if candle['close'] > candle['open'] and candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    return score >= 2


def detect_prepare_exit(candle):
    """
    判斷：準備下車（紅K漲勢開始放緩）
    打分條件：
        +1：紅K但實體變弱
        +1：量縮
        +1：上影線變長
    回傳：需達2分以上才通過
    """
    score = 0
    if candle['close'] > candle['open'] and candle['body'] < candle['prev_body']:
        score += 1
    if candle['volume'] < candle['prev_volume']:
        score += 1
    if candle['upper_shadow'] > candle['body']:
        score += 1
    return score >= 2
