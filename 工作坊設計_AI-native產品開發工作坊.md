# 工作坊設計：當老師變成 PM / PjM——用 AI-native 流程打造課程數位產品

> 母文件：[AI-native開發流程_KnowledgeBase.md](AI-native開發流程_KnowledgeBase.md)（概念層架構，含 Graphiti / Schema 友善替代說法見該文件第 1.4 節）
> 本文件：把架構轉譯成**基礎模組（6 小時）＋ 實施模組（6 小時）＝ 合計 12 小時**的工作坊，教對象是**AI / 程式初學者的大學教師**。全程 Vibe Coding 統一以 **Claude Code** 示範，不混用其他工具，降低學習負擔。
> 延伸文件：[工作坊講師簡報大綱.md](工作坊講師簡報大綱.md)（全套 A1-A6、B1-B6 濃縮成 57 張投影片大綱）、[工作坊評量與回饋機制.md](工作坊評量與回饋機制.md)（學習目標對照評量表、結業標準、課後回饋問卷）

---

## 1. 定位（Definitions）

### 1.1 這場工作坊在教什麼
不是教「寫程式」，而是教**專案定義能力**——把一個模糊的教學需求，逐層轉譯成 AI 能理解、能執行的規格，最後由 AI（而非學員自己）完成程式碼實作。

回答問題：
- 老師不會寫程式，要怎麼「主導」一個數位產品的開發？
  👉 老師負責前五層（Needs → Goals → Spec → Graphiti → Schema），Claude Code 負責第六層（Coding）。老師的專業價值在於「教學現場的判斷力」，不在於「打字寫程式」。

### 1.2 角色轉換對照
| 傳統角色 | 在這個工作坊中對應的角色 |
|---|---|
| 老師 | 兼任 Product Manager（定義要做什麼）與 Project Manager（安排誰、何時做） |
| TA / 協作教師 | Vibe Coder（實際與 Claude Code 對話、產出程式碼的人，可能是老師自己，也可能是團隊裡對 AI 工具較熟悉的人） |
| Claude Code | Implementer（依照交接文件把規格變成可運作的產品，必要時分派多個子代理人並行處理） |

### 1.3 兩模組的設計理由
- **基礎模組（6 小時）**：對應架構的「人類定義」區塊（Needs / Goals / Spec / Graphiti / Schema），並導入 Agile / PjM 必要概念。這一模組**完全不需要碰 Claude Code**，可以獨立開課，讓完全不用 AI 工具的老師也能先建立定義能力。
- **實施模組（6 小時）**：對應「AI 執行 + 團隊協作」區塊（Vibe Coding + 多重代理人 + 交接 + 回顧會）。**需要先修過基礎模組**，或帶著一份已經寫好的基礎規格包來上課。
- 兩模組可以排成連續兩個半天、間隔一週的兩次課、或各自獨立開課（基礎模組適合較大班制的入門場次，實施模組適合較小班制的實作場次）。

---

## 2. 學習目標（Learning Outcomes）

**基礎模組結束後，學員應能夠：**
- **LO1**：說出 AI-native 六層架構，並解釋「為什麼定義問題的順序很重要」
- **LO2**：針對自己的課程專案，寫出一份 Customer Needs → Product Goals → Open Spec 文件
- **LO3**：用「純文字關聯樹」畫出 Graphiti（不需要學習專業架構軟體）
- **LO4**：設計一份基本 Schema（資料表與欄位）
- **LO5**：說出 Backlog、看板、完成的定義（Definition of Done）、衝刺（Sprint）、每日／每週同步會、回顧會（Retrospective）這幾個 Agile 概念，並知道它們對應到六層架構的哪裡

**實施模組結束後，學員應能夠：**
- **LO6**：用 Claude Code 進行「Vibe Coding」，依據自己的規格包直接產出一個可運作的原型
- **LO7**：判斷什麼情況該把工作拆給多個子代理人（Subagent）同時處理，並用自然語言請 Claude Code 這麼做
- **LO8**：撰寫一份「交接文件」，讓 TA 或協作教師能在不追問的情況下接手開發
- **LO9**：主持一場簡短的回顧會（Retrospective），檢討流程而非檢討人

---

## 3. 兩模組流程總覽（Core Framework）

```
基礎模組（6 小時）— PM 角色 + Agile 概念，不需要 Claude Code
  Session A1  開場 + AI-native 六層架構總覽              40 分鐘
  Session A2  Customer Needs → Product Goals 工作坊       70 分鐘
  ── 休息 10 分鐘 ──
  Session A3  Open Spec 工作坊（使用者故事寫法）           70 分鐘
  ── 休息 / 午休 ──
  Session A4  Graphiti + Schema 工作坊                    70 分鐘
  Session A5  Agile / PjM 必要概念導入                     80 分鐘
  ── 休息 10 分鐘 ──
  Session A6  收尾：整理成「基礎規格包」                    30 分鐘

實施模組（6 小時）— PjM 角色 + Claude Code + 團隊協作
  Session B1  Claude Code 入門（不需要寫程式）              40 分鐘
  Session B2  Vibe Coding 實作                            90 分鐘
  ── 休息 10 分鐘 ──
  Session B3  多重代理人（Multi-Agent）協作做法             60 分鐘
  Session B4  交接文件撰寫工作坊                            40 分鐘
  ── 休息 / 午休 ──
  Session B5  分組演練：角色互換交接 + 看板追蹤              90 分鐘
  Session B6  成果展示 + 衝刺回顧會 + SOP 帶走               40 分鐘
```

👉 核心邏輯：基礎模組對應架構中「人類定義」的五層，實施模組對應「AI 執行 + 團隊協作」的部分。兩模組合計仍是完整走一次六層架構，只是拆成兩個各 6 小時、可分開排課的單元。

---

## 4. 基礎模組逐節設計（6 小時）

### Session A1（40 分鐘）｜開場 + 六層架構總覽
- **內容**：AI-native 六層架構總覽、建築比喻（開咖啡廳）、角色轉換對照表
- **活動**：每位學員用一句話寫下自己想做的課程數位產品（例如「我想幫我的 EMI 課程做一個 AI 助教」）
- **產出**：一句話的專案宣言（Project Statement）
- **自學版**：見 [SessionA1自學指南_六層架構總覽.md](SessionA1自學指南_六層架構總覽.md)

### Session A2（70 分鐘）｜Needs → Goals
- **內容**：Why → What outcome 的差異；如何把模糊的教學痛點轉成可衡量的 Product Goals
- **活動**：以自己的專案宣言為起點，寫出 3 條 Customer Needs，再轉譯成 2-3 個 Product Goals（需附可衡量指標，例如「80% 學生一週內至少使用 AI 助教一次」）
- **產出**：Needs & Goals 文件（交接文件範本第 2、3 節）
- **常見卡點提醒**：Goals 寫成「做一個網站」而非「達成的結果」——講師需示範修正
- **自學版**：見 [SessionA2自學指南_NeedsToGoals.md](SessionA2自學指南_NeedsToGoals.md)（含 EMI 案例示範、找碴練習）

### Session A3（70 分鐘）｜Open Spec
- **內容**：如何把 Goals 拆解成「系統必須做什麼」的條列敘述；導入 Agile 的**使用者故事（User Story）**句型：「身為〔角色〕，我想要〔行為〕，以便〔目的〕」，並學習搭配「完成的定義（Definition of Done）」
- **活動**：每組寫出至少 5 條使用者故事，每條附上完成的定義，並互相檢查是否「具體到 AI 看得懂、不需要再追問」
- **產出**：Open Spec 文件（交接文件範本第 4 節，含 Definition of Done 欄位）
- **自學版**：見 [SessionA3自學指南_OpenSpec.md](SessionA3自學指南_OpenSpec.md)

### Session A4（70 分鐘）｜Graphiti + Schema
- **內容**：關聯圖只需要「縮排文字樹」即可，不需要學工程工具；也可用「關係地圖」「資料規格表」等友善說法輔助理解（詳見知識庫 1.4 節）。Schema 只需列出「這個東西有哪幾個欄位」，可類比成設計一張成績單的欄位
- **活動**：
  1. 用縮排文字樹畫出專案裡的主要物件關聯（例如 Course/Module/Student/AI Coach）
  2. 針對每個物件，列出 3-5 個欄位（Schema）
  3. 對照檢查：畫的關聯裡，每一條線是否都能在 Schema 裡找到對應欄位支撐？（體現 Graphiti↔Schema 疊代）
- **產出**：Graphiti 縮排樹 + Schema 表格（交接文件範本第 5、6 節）
- **平替工具選用（不強制）**：見附錄 A
- **現場講義卡（選讀，尾聲發放）**：見 [SessionA4講義卡_Graphiti三層記憶.md](SessionA4講義卡_Graphiti三層記憶.md)——一分鐘版的向量資料庫／圖資料庫／Graphiti 三層記憶對照，給想多了解的學員帶走
- **自學版**：見 [SessionA4自學指南_GraphitiSchema.md](SessionA4自學指南_GraphitiSchema.md)（含 Graphiti↔Schema 交叉檢查的三種支撐關係類型：直接外鍵／隱含於範圍／統計彙總，避免自學者誤判「漏掉欄位」）

### Session A5（80 分鐘）｜Agile / PjM 必要概念導入
- **內容**：把 Backlog、看板（Kanban）、完成的定義、衝刺（Sprint）、每日／每週同步會（Standup）、回顧會（Retrospective）、最小可行產品（MVP）這些概念，對照到六層架構上（完整對照表見第 6 節）
- **活動**：把 Session A3 寫好的使用者故事，貼到一張三欄看板（待做 / 進行中 / 已完成）上，練習排優先順序
- **產出**：一張初版看板（可用紙本便利貼或線上工具如 Trello / Notion 皆可）
- **完整逐分鐘示範腳本**：見 [SessionA5示範腳本_Agile概念導入.md](SessionA5示範腳本_Agile概念導入.md)（沿用駱世民教授 EMI 案例已寫好的 5 條使用者故事，逐一操作 Backlog／看板／衝刺分配／完成的定義／同步會演練）

### Session A6（30 分鐘）｜收尾：整理成「基礎規格包」
- **內容**：把 A1-A5 的產出整理進交接文件範本的第 1-6 節，作為實施模組的輸入
- **產出**：「基礎規格包」v1（帶去實施模組使用，或交給協作的 TA）
- **自學版**：見 [SessionA6自學指南_基礎規格包收尾.md](SessionA6自學指南_基礎規格包收尾.md)（含四項最終交叉檢查）

---

## 5. 實施模組逐節設計（6 小時）

### Session B1（40 分鐘）｜Claude Code 入門
- **內容**：Claude Code 是什麼——一個能讀懂自然語言指令、直接讀寫檔案、執行程式並回報結果的 AI 協作工具；不需要先學程式語言，用中文描述你要什麼即可
- **活動**：現場示範最小案例：請 Claude Code 依照一小段 Open Spec，產出一個簡單的網頁原型，讓學員看到「規格 → 原型」的完整過程
- **產出**：無（示範觀摩為主）
- **自學版**：見 [SessionB1自學指南_ClaudeCode入門.md](SessionB1自學指南_ClaudeCode入門.md)（含安裝步驟、第一次啟動、最小示範練習、自我檢查清單與常見問題自助排除，供沒有講師在旁時獨立完成本節）

### Session B2（90 分鐘）｜Vibe Coding 實作
- **內容**：把 Session A6 的「基礎規格包」整段交給 Claude Code，請它依據 Needs、Goals、Open Spec、Graphiti、Schema 產出可運作的原型
- **活動**：每組把自己的規格包貼給 Claude Code，實際產出原型，並在畫面上檢視結果是否符合 Spec；同步開始記錄 Vibe Coding Log（交接文件範本第 7 節）
- **產出**：一個可運作的原型 + Vibe Coding Log 初版
- **講師提醒**：重點不是「原型多完美」，而是讓學員體驗「規格寫得清楚 vs 模糊」對 Claude Code 產出品質的直接影響
- **完整逐分鐘示範腳本**：見 [SessionB2示範腳本_EMI案例.md](SessionB2示範腳本_EMI案例.md)（以駱世民教授的 EMI 課程雙語 AI 助教為案例，含清楚規格與模糊規格的對照演示）

### Session B3（60 分鐘）｜多重代理人（Multi-Agent）協作做法
- **內容**：Claude Code 除了一般對話，還能把工作拆給多個「子代理人（Subagent）」同時處理，概念上像主管把任務分派給不同專員：
  - **探索型代理人**：先去讀懂整個專案現況、找資料在哪裡
  - **實作型代理人**：專門負責把某個功能做出來
  - **審查型代理人**：專門檢查另一個代理人寫出來的東西有沒有問題（類似請不同的人互相校對）
  - 也支援**背景執行**：代理人在背景跑一段較長的任務，完成後通知你，你可以同時做別的事
- **操作方式（給非技術學員）**：不需要學指令語法，直接在跟 Claude Code 對話時用自然語言描述，例如：「這個專案有三件事要做——課程頁面、AI 問答功能、學習報表，請你分別派人同時處理，做完後互相檢查一下」，Claude Code 會自行判斷如何拆分與执行
- **什麼時候該用**：
  - 專案裡有多個彼此獨立的功能，可以平行處理，加快速度
  - 想要「寫」與「審查」分開，避免同一個代理人自己寫、自己審查看不出問題
  - 想要背景執行較長的任務，自己同時繼續做別的事
- **什麼時候不需要**：專案小、功能單一，一個對話就能處理完，過度拆分反而增加追蹤成本
- **與 Agile 的對應**：多重代理人本質上就是把看板上的多張 Backlog 卡片同時分派出去執行——概念上等同於團隊裡「一人一張卡片，平行推進」
- **活動**：挑一組已經有 2-3 個獨立功能的專案，現場示範請 Claude Code 拆給多個代理人同時處理，並在 Vibe Coding Log 的「分工代理人」欄位記錄下來
- **產出**：更新後的 Vibe Coding Log（含分工紀錄）
- **完整逐分鐘示範腳本**：見 [SessionB3示範腳本_多重代理人.md](SessionB3示範腳本_多重代理人.md)（承接 Session B2 的 EMI 案例，示範如何用 Graphiti 關聯圖判斷任務相依關係，決定哪些工作平行、哪些要排隊）
- 給講師/助教的進階備忘見附錄 B

### Session B4（40 分鐘）｜交接文件撰寫工作坊
- **內容**：介紹完整的交接文件範本，說明每一節的目的，特別是「目前完成度」「已知限制」「下一步建議」
- **活動**：把 Session B2-B3 的產出整理進交接文件範本，補齊第 8、9、10 節
- **產出**：完整交接文件 v1
- **自學版**：見 [SessionB4自學指南_交接文件撰寫.md](SessionB4自學指南_交接文件撰寫.md)（含 EMI 案例逐節填寫範例、模糊版 vs 具體版找碴練習、自我檢查清單）

### Session B5（90 分鐘）｜分組演練：角色互換交接
- **內容**：模擬真實團隊情境——TA 或協作教師只能靠交接文件接手，不能問原作者；同時練習用看板追蹤交接後的進度
- **活動**：
  1. 兩組互換交接文件（A 組的文件交給 B 組，反之亦然）
  2. 每組只憑對方的交接文件，嘗試用 Claude Code 延伸對方的原型（例如加一個新功能），並把新工作項目加進對方的看板
  3. 交接後討論：文件裡哪裡看不懂？哪裡漏了？Claude Code 誤解了什麼？
- **產出**：一份「交接文件檢查清單」（學員親身踩過坑後，自己歸納出來的清單）
- **一人自學版**：見 [SessionB5自學指南_一人自學版交接測試.md](SessionB5自學指南_一人自學版交接測試.md)——沒有第二組人時，改用「全新、沒有記憶的 Claude Code 對話」當作沒參與過程的人，客觀測試交接文件是否自足

### Session B6（40 分鐘）｜成果展示 + 衝刺回顧會 + SOP 帶走
- **內容**：每組 5 分鐘展示原型 + 交接文件；接著主持一場簡短的**衝刺回顧會（Sprint Retrospective）**——每人分享「哪裡做得好（Keep）」「哪裡可以改善（Problem）」「下次要試試看什麼（Try）」，重點是檢討流程而非檢討人
- **產出**：學員帶走（1）自己專案的完整交接文件（2）空白範本（3）回顧會的 Keep-Problem-Try 紀錄，可套用到下一個專案
- **一人自學版**：見 [SessionB6自學指南_成果展示與回顧會.md](SessionB6自學指南_成果展示與回顧會.md)（自己錄一段 2 分鐘展示＋一人版 Keep/Problem/Try＋SOP 帶走清單）

---

## 6. Agile / PjM 必要概念對照表

| Agile 概念 | 白話說明 | 對應到六層架構的哪裡 |
|---|---|---|
| 待辦清單（Backlog） | 所有還沒做、但已經想到的功能／需求清單 | Open Spec 裡尚未實作的條目，先全部列進待辦清單，再依優先順序排隊處理 |
| 衝刺（Sprint） | 固定一段時間只專注做完一批工作，做完就檢視、調整，再進下一輪 | 每一輪「Vibe Coding + 交接 + 檢視」就是一個小型衝刺 |
| 看板（Kanban Board） | 用「待做 / 進行中 / 已完成」三欄追蹤進度 | 把 Open Spec 的每一條使用者故事當作一張卡片，貼在看板上移動 |
| 完成的定義（Definition of Done） | 一項工作要滿足什麼條件才能算「做完」，避免各自認定標準不一 | 每條使用者故事都先定義「怎樣才算做完」，Vibe Coding 產出才不會不符預期 |
| 每日／每週同步會（Standup） | 簡短同步「上次做了什麼、接下來要做什麼、卡在哪裡」 | 對應團隊協作節奏——建議每完成一層就同步一次，而非等到最後才檢查 |
| 回顧會（Retrospective） | 一輪工作結束後，檢討「哪裡做得好、哪裡可以改善」，不是檢討人，是檢討流程 | Session B6 的 Keep-Problem-Try 環節 |
| 使用者故事（User Story） | 「身為〔角色〕，我想要〔功能〕，以便〔目的〕」的敘述格式 | 就是 Open Spec 撰寫時建議採用的句型 |
| 最小可行產品（MVP） | 先做出「最小但能真的運作」的版本，而不是一次做到完美 | Vibe Coding 實作時的「先求有，再求好」原則 |

👉 補充：Scrum（固定衝刺週期）較適合有明確階段的專案（例如一學期分成三個衝刺）；看板（持續滾動、沒有固定週期）較適合平時零碎時間持續調整的課程網站維護工作。兩者可依專案性質選用，不必二選一硬套。

---

## 7. 團隊協作與溝通節奏建議（給實際帶團隊時參考）

| 情境 | 建議做法 |
|---|---|
| 老師（PM/PjM）與 TA（Vibe Coder）分工 | 老師負責 Needs/Goals/Spec/Graphiti/Schema，TA 負責實際跟 Claude Code 對話產出程式碼；交接靠交接文件，不靠口頭說明 |
| 多久同步一次 | 建議每次「一層」完成後同步一次（Standup 精神），而非等到最後才檢查 |
| 什麼情況要回頭修正規格 | 當 Vibe Coding 過程中 Claude Code 一直問同樣的問題，或產出結果一直不符預期，通常代表 Open Spec 或 Schema 不夠具體，應回頭修正而非一直重下指令 |
| 版本管理 | 交接文件建議用有版本號的共用文件（Google Docs / Notion 皆可），每次重大修正遞增版號，避免多人改到不同版本 |
| 定期檢討 | 每個衝刺結束後開一場簡短回顧會，用 Keep-Problem-Try 三欄記錄，避免同樣的卡點反覆發生 |

---

## 8. 常見誤解提醒（給講師）

1. **學員以為要先學會寫程式才能上這堂課** → 開場需明確澄清：這堂課完全不需要寫程式，重點是「定義能力」。
2. **學員把 Product Goals 寫成功能清單**（例如「做一個 AI 助教」）而非結果指標 → Session A2 需準備 1-2 個反例現場修正。
3. **學員覺得 Graphiti/Schema 太抽象、想跳過** → 強調這是 Vibe Coding 成功率的關鍵：規格模糊，Claude Code 產出就會不準確，Session B2 會直接讓他們體驗到落差。
4. **分組演練時想幫對方補充口頭說明** → 講師需嚴格禁止口頭補充，這正是練習「文件必須自足」的重點。
5. **學員一開始就想用多重代理人把所有事情都拆開** → Session B3 需提醒：多重代理人是進階選配，先確定單一對話能順利完成，再考慮拆分，避免為拆而拆。

---

## 附錄 A：Graphiti / Schema 的平替工具（選用，不強制）

工作坊建議**只用 Claude Code 一種工具**貫穿全程（從基礎模組請它幫忙草擬關聯樹，到實施模組正式動手實作）。若學員想要更視覺化的呈現，以下是難度由低到高的平替選項，皆為選用：

| 難度 | 工具 | 用法 |
|---|---|---|
| 最低（工作坊預設） | 直接請 Claude Code 用縮排文字樹描述關聯 | 例如：「幫我用縮排文字畫出 Course、Module、Student、AI Coach 之間的關係」，不需要安裝任何軟體 |
| 低 | Excalidraw / diagrams.net（draw.io） | 免費、拖拉即可、手繪風格，適合想要視覺化但不想學複雜工具的人 |
| 中 | Miro / FigJam 的 AI 生成圖表功能 | 打字描述關係，AI 自動畫出流程圖或關聯圖，適合團隊協作白板情境 |
| 中高（給對 Markdown 熟悉的學員） | Mermaid 語法 | 請 Claude Code 直接生成 Mermaid 語法，貼到 Notion / GitHub / 大部分筆記軟體會自動渲染成圖 |
| 進階（給團隊裡有工程師的情況，工作坊不涉及） | Graphiti（getzep/graphiti）等知識圖譜開發套件 | 當 AI 助教需要在正式環境中持續讀寫「活的」知識圖譜時才需要，屬於工程實作範疇 |

---

## 附錄 B：多重代理人操作備忘（給講師 / 助教參考）

- Claude Code 的「一般對話」與「子代理人」是同一套系統的兩種用法：主對話可以直接把子任務交給專門的子代理人執行，執行完會把結果彙整回主對話。
- 子代理人適合分工的情境：探索（找程式碼 / 資料在哪）、實作（把功能做出來）、審查（檢查別人做的東西），三種角色分開能降低「自己寫自己審查」看不出問題的風險。
- 需要長時間執行的任務可以請它在背景執行，不需要一直盯著看，完成後會有通知。
- 若多個代理人需要同時修改同一批檔案，建議請 Claude Code 幫忙把工作區分開（避免互相覆蓋），這部分細節可以直接交給 Claude Code 自行判斷，講師不需要向學員解釋底層機制。
- 教學拿捏：對完全非技術背景的學員，只需要示範「怎麼用一句話請它拆給多個代理人」，不需要深入解釋子代理人如何運作；重點放在「什麼時候該拆、什麼時候不用拆」的判斷力。

---

## AI-ready 結構

```yaml
tags:
  - faculty-development
  - workshop-design
  - pm-pjm-for-teachers
  - vibe-coding
  - claude-code
  - multi-agent
  - agile-for-education
  - ai-native-development
  - team-handoff
  - emi-course-development

relations:
  - Workshop -> composed_of -> [基礎模組_6hr, 實施模組_6hr]
  - 基礎模組_6hr -> covers -> [Needs, Goals, OpenSpec, Graphiti, Schema, Agile基礎概念]
  - 實施模組_6hr -> covers -> [ClaudeCode入門, VibeCoding, MultiAgent, HandoffDoc, Retrospective]
  - Teacher_Role -> maps_to -> [ProductManager, ProjectManager]
  - TA_Role -> maps_to -> VibeCoder
  - ClaudeCode -> maps_to -> Implementer
  - ClaudeCode -> supports -> MultiAgentDelegation
  - MultiAgent -> maps_to -> Agile_Backlog_平行分派
  - HandoffDocument -> enables -> Role_Handoff_without_verbal_explanation
  - Graphiti_Concept -> friendly_terms -> [關係地圖, 連連看圖]
  - Schema_Concept -> friendly_terms -> [資料規格表, 成績單欄位類比]
  - AgileConcepts -> [Backlog, Sprint, Kanban, DefinitionOfDone, Standup, Retrospective, UserStory, MVP]
```
