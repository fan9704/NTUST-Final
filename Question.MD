# 2026 台科大資管：Python 程式設計實作任務

> 專案名稱：遺留代碼重生計劃 (Legacy Code Rebirth)

## 1. 任務背景

你接手了一個由前輩開發的「簡易記帳系統」`messy_tracker.py` 。雖然該程式目前可以執行，但內部邏輯混亂、變數命名不明確，且缺乏現代軟體開發的架構。

你的任務是：利用 GitHub Copilot 作為協作對象，將這段「充滿味道」的程式碼進行分析、文件化，並重構成一個專業級的 Python 專案。

## 2. 素材

- 答案卷：`Answer.MD`，作答方式請依照答案卷為主。
- 刪除 Git 資料夾的批次檔：`delete_git.ps1`，請在 Clone 後執行此批次檔來刪除現有的 Git 資料夾。
- 測試資料： `input_test.txt` 裡面有可以複製的輸入資料，請用來多多測試程式執行正確，提供您在執行 `messy_tracker.py` 時使用的
- 原始程式碼： `messy_tracker.py`
- 題目卷：`Question.MD`
- 提示文件：`README.MD`。

## 3. 實作任務與步驟

### 第零階段：環境準備（Preparation）

1. 安裝 Git 並設定 GitHub 帳號。
2. 安裝 VSCode 並安裝 GitHub Copilot Extension。
3. Clone 此專案到本地，並執行 `delete_git.ps1` 來刪除現有的 Git 資料夾。
4. 在 VSCode 中打開專案資料夾，並熟悉專案結構與內容。
5. 建立一個檔案 `refined_tracker.py` 用來放置修改後的程式碼
6. 執行看看 `messy_tracker.py` 的執行結果，測試是否執行正常

### 第一階段：代碼審核 (Code Audit)

1. 請在 VSCode 中開啟 `messy_tracker.py`。
2. 使用 GitHub Copilot Chat 功能分析程式碼。
3. 在 `Answer.md` 中完成「變數與邏輯對照表」，找出神祕變數 a, b, cate_dict 的真實商業意義。
4. 診斷出 5 個以上的「代碼壞味道」，並說明為何這些設計會造成維護困難。

### 第二階段：Vibe-Coding 重構 (Refactor)

1. 目標： 撰寫 refined_tracker.py。
2. 要求： 透過 Prompt 引導 Copilot 完成以下改動：
    - 模組化： 將功能拆解為類別 (Class) 或函式 (Function)。
    - 格式升級： 捨棄 txt 混亂格式，改用 json 格式儲存。
    - 強健性： 增加對使用者輸入與檔案讀取的錯誤處理 (Try-Except)。
    - 優化： 修正原程式每次新增資料都要存檔的低效率行為。
3. 紀錄： 在 `Answer.md` 紀錄你使用的 3 個關鍵 Prompt 以及 AI 出錯後的修正對話。

### 第三階段：測試與驗證 (Testing & Validation)

1. 執行 `refined_tracker.py`，確保功能正確。
2. 輸入 `show` 指令，確認資料清單能正確顯示。
3. 確認 `records.json` 的格式正確，並貼上前幾行內容到 `Answer.md`。

### 第四階段：版本控制 (Git & GitHub)

1. 在本地初始化 Git 倉庫
2. 開發過程中需有 Commit，紀錄你的開發進度。
3. 將專案推送到 GitHub (Public) 若提交 Private 連結不給分。

---

## 助教溫馨提示

Vibe-Coding 的核心在於 **「精準的溝通」**。如果你發現 AI 給的 code 還是很亂，請試著告訴它：「請參考 Clean Code 原則重新命名變數」或是「請將這個邏輯獨立成一個XX模組」。祝各位學弟妹重構順利！
