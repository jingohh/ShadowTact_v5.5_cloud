ShadowTact v5.6 機器人安裝說明（工程師專用）

======================================
說明：本程式為 Telegram 貼圖通知系統，會根據即時策略自動發送訊號圖與文字。請依以下步驟安裝執行。

--------------------------------------
一、資料夾內容（共 7 個檔案）
請確保以下檔案都在同一層資料夾內，不可移除、刪除或改名：

1. config.py
2. main.py
3. telegram_bot.py
4. tactics.py
5. image_trigger.py
6. loglog_tool.py
7. README_安裝說明.txt（本檔案，可留存）

--------------------------------------
二、安裝與啟動流程

1. 安裝 Python 環境
   - 系統需有 Python 3.8 或以上版本

2. 安裝 requests 套件
   - 打開終端機或命令列輸入：
     pip install requests

3. 修改參數
   - 打開 config.py
   - 填入：
     TELEGRAM_TOKEN = "你的 Telegram Bot Token"
     STICKERS = {...}  // 對應貼圖 ID
     DEFAULT_SYMBOL = "TRX/USDT" 或其他交易對

4. 執行程式
   - 在資料夾中執行 main.py：
     python main.py

--------------------------------------
三、注意事項（請務必遵守）

- 所有檔案不可刪除、改名或移出資料夾
- 貼圖 ID 請用 Telegram 的 GetIDs Bot 取得
- 若不出貼圖，請確認 STICKERS 中的 ID 正確
- 執行期間程式將每隔 3 分鐘檢查一次訊號
- loglog_tool.py 為記錄用，會自動產生 logs.txt

--------------------------------------
四、完成部署後
- 用戶會即時收到 Telegram 通知貼圖與訊息
- 無需人工干預，系統自動運作
- 若有更新版本，會再另行提供完整壓縮檔

======================================
製作：ShadowTact 行動系統 / v5.6 