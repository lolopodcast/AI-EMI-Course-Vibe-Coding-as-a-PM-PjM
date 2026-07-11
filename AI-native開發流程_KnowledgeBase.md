# AI-native 開發團隊工作流程 知識架構（Knowledge Base）

> 主題：AI 時代的軟體 / 產品開發流程，從「客戶需求」到「Production」的六層架構，強調 Spec、關聯（Graphiti）、資料結構（Schema）與 AI Coding 的分工。

> 應用情境：本知識庫是概念層文件，實際教學應用請見同資料夾兩份延伸文件——
> - [工作坊設計：AI-native產品開發工作坊.md](工作坊設計_AI-native產品開發工作坊.md)（給非技術背景教師的兩天工作坊課程設計）
> - [交接文件範本.md](交接文件範本_AI-native專案.md)（教師與 TA/協作教師之間可直接複製使用的交接文件）

---

## 1. 定義（Definitions）

### 1.1 AI-native 開發（AI-native Development）
指以 AI Agent（如 Claude Code、Codex、Cursor）作為主要「實作者（Implementer）」的開發模式。人類團隊的工作重心從「寫程式」轉移到「定義問題、定義結構、定義關係」，AI 負責把定義好的規格轉譯成程式碼。

回答問題：
- 在 AI 時代，人類工程師 / PM 的核心價值從哪裡轉移到哪裡？
  👉 從「Implementation（怎麼寫）」轉移到「Specification（寫什麼、怎麼組、資料長怎樣）」。

### 1.2 六層架構的定義
| 層級 | 英文 | 核心問題 | 產出物 |
|---|---|---|---|
| 1 | Customer Needs | Why（為什麼要做？） | 需求陳述 |
| 2 | Product Goals | What outcome（要達成什麼結果？） | 目標清單 |
| 3 | Open Spec | What the system must do（系統必須做什麼？） | 功能規格 |
| 4 | Architecture / Graphiti | How things connect（彼此如何連結？） | 關聯圖 / 架構圖 |
| 5 | Schema | What data looks like（資料長什麼樣？） | 資料表 / 欄位定義 |
| 6 | AI Coding → Production | Implementation（誰把它寫出來？） | 可運行系統 |

### 1.3 Graphiti 的雙重意涵（Dual Meaning of Graphiti）
在這個架構中，「Graphiti」同時指涉兩件事，而且這兩件事是**故意疊合**的：

1. **通用概念（Generic Concept）**：架構關聯圖——描述系統中各物件 / 服務彼此如何連結（例如 Course ├─ Module ├─ Student）。任何開發流程都需要這一層，不論有沒有用特定工具。
2. **特定工具（Specific Tool）**：[Graphiti](https://github.com/getzep/graphiti)（由 Zep 團隊開源），是一個用來建構「具時間感知的知識圖譜（temporally-aware knowledge graph）」的開發套件，專為 AI Agent 在動態環境中使用而設計。要理解它在做什麼，最好的方式是對照三種不同的「記憶能力」：

#### 三種記憶能力的比較
| 系統 | 知道什麼 | 擅長回答 | 舉例 |
|---|---|---|---|
| 向量資料庫（Vector Database） | 哪些東西「像」（Similarity） | 「有哪些概念跟這個概念很相似？」 | EMI Course ≈ Digital Course；Student Learning ≈ Learner Analytics；Supply Chain ≈ Logistics Management |
| 圖資料庫（Graph Database） | 哪些東西「有關」（Relationships） | 「誰和誰有關？彼此是什麼關係？」 | Teacher ─teaches→ Course；Student ─enrolls→ Course；Frontend ─calls→ API；API ─writes→ Database |
| **Graphiti** | 哪些東西像、哪些東西有關，**並且記住它們如何隨時間演變** | 上面兩者都能回答，還能回答「這個關係是什麼時候成立的？現在還有效嗎？」 | 見下方核心元素 |

👉 一句話總結：向量資料庫知道哪些東西「像」；圖資料庫知道哪些東西「有關」；Graphiti 知道哪些東西像、哪些東西有關，以及它們如何隨時間和情境演變。

#### Graphiti 的核心元素
- **節點（Nodes / Entities）**：代表一個概念或實體，例如人、課程、文件、API、資料表、Agent
- **連結線／邊（Edges / Relationships）**：代表節點之間的關係，例如 teach、contain、call、depend_on、create、use、own
- **相似性（Similarity）**：例如 EMI Course ≈ Digital Course、AI Coach ≈ Tutor Agent、Supply Chain ≈ Logistics
- **脈絡與時間（Context & Temporal Evolution）**：例如「2026 年新增 AI Coach」「後來改成 Multi-Agent 架構」「某個 API 已被棄用（Deprecated）」「某個資料表已被合併」

其餘核心特性：
- 能從對話紀錄、結構化資料等「episode」中，漸進式地建立與更新知識圖譜，不需要每次重新計算整個圖
- 支援雙時態資料模型（bi-temporal）：同時記錄「事件發生時間」與「資料寫入時間」，讓 AI 能推理「當時是什麼狀態」
- 混合檢索（hybrid retrieval）：結合語意向量、關鍵字搜尋（BM25）與圖遍歷，供 LLM/AI Agent 在執行期查詢

#### 最後的定義
> Graphiti = 心智圖 + 長期記憶 + 關係推理
> 更簡潔地說：**Graphiti ≈ AI 的可演化心智圖（Evolving Mind Map for AI）**——一張可被機器理解（machine-readable）、可持續更新（dynamic）、可進行推理（reasoning）、具有長期記憶（long-term memory）的知識地圖。

👉 核心洞察：
- 在**傳統軟體開發**中，Architecture / Graphiti 這一層通常只是「給人看」的靜態圖（畫在白板或 Miro 上，工程師參考後就去寫 code）。
- 在 **AI-native 開發**中，當系統本身需要一個會持續學習、被 AI Agent 在執行期即時查詢的「關係層」（例如 AI Coach 需要記得「這個學生在哪個 Module 卡關過」「這個問題跟之前哪次對話有關」），這一層就可能**直接用 Graphiti 這類工具實作成活的知識圖譜**，而不只是設計期的靜態文件。
- 也就是說：**通用概念（設計期的關聯圖）與特定工具（執行期的知識圖譜）在 AI-native 系統中會合而為一**——這也是為什麼原文特別把它獨立成一層，而不是併入 Schema 或 Open Spec。

<!-- 註：Graphiti 工具的細節（API、版本特性）以官方文件為準，此處僅描述其設計理念與定位，供教學脈絡使用。 -->

👉 **教學上的取捨**：面對「AI / 程式小白」的大學教授學員，工作坊只教**第 1 點（通用概念）**——用純文字縮排樹或簡單白板圖表達關聯即可，不要求安裝或操作 Graphiti 這類工程工具。第 2 點（特定工具）保留在知識庫中作為「進階脈絡」，讓學員理解：如果團隊裡有工程師接手，這一層未來可能會被實作成真正的知識圖譜。可操作的平替工具清單見 [工作坊設計文件](工作坊設計_AI-native產品開發工作坊.md) 附錄 A。

### 1.4 給非技術背景學員的友善替代說法（選用，不強制）
Graphiti、Schema 這兩個詞對第一次接觸的大學教授來說偏抽象。以下說法可以在口語講解時交替使用，幫助理解，但**正式文件仍建議使用 Graphiti / Schema 原名**，以維持與後續工程團隊或工具（如 Claude Code）溝通時的一致性：

| 正式名稱 | 友善替代說法 | 好懂的類比 |
|---|---|---|
| Graphiti（關聯圖） | 關係地圖 / 連連看圖 / 「誰跟誰有關係」圖 | 像畫家族族譜——誰是誰的誰，一條線一條線連起來 |
| Schema（資料形狀） | 資料規格表 / 欄位清單 / 資料長相表 | 像設計一張成績單或 Excel 表頭——先決定有哪幾欄（姓名、學號、分數…），再決定每欄放什麼類型的資料 |

👉 使用建議：第一次講解時可以先用友善說法降低距離感（例如「我們先畫一張關係地圖」），待學員理解概念後，再回到正式名詞（「這張關係地圖就是 Graphiti」），讓學員之後查資料、跟工程背景的人溝通時不會斷層。

---

## 2. 核心架構（Core Framework）

### 2.1 主流程總覽
```
Customer Needs
      ↓
Product Goals
      ↓
Open Spec
      ↓
Architecture / Graphiti
      ↕
     Schema
      ↓
AI Coding
      ↓
Production
```

👉 核心邏輯：
- 前三層（Customer Needs → Product Goals → Open Spec）是「人類定義問題」的區塊，回答 Why / What outcome / What system does。
- 第四、五層（Graphiti、Schema）是「人類定義結構」的區塊，回答 How things connect / What data looks like。
- 最後一層（AI Coding）是「AI 執行」的區塊，依據前面五層的規格把系統寫出來。

### 2.2 Graphiti ↔ Schema 的雙向疊代關係（非線性特例）
Graphiti（架構關聯）與 Schema（資料形狀）**不是單純的上下層關係**，而是互相疊代、來回修正：
- 設計架構時（例如 Course 底下要有 Module、Student、AI Coach、Learning Analytics），會發現某個關聯需要特定欄位才能成立 → 回頭修改 Schema。
- 設計 Schema 時（例如 Student 需要 course_id 外鍵），會發現這暗示了一條原本沒畫出來的關聯 → 回頭修改 Graphiti。

👉 關鍵概念：
- Graphiti 決定「兩個物件之間有沒有關係、關係的方向」。
- Schema 決定「這個物件內部的資料欄位長什麼樣」。
- 兩者必須反覆對照，才能避免「畫了關聯卻沒有對應欄位」或「欄位存在卻沒有關聯支撐」的落差。

### 2.3 四句話濃縮原則（Compressed Principles）
1. **Spec 決定做什麼**（What）
2. **Graphiti 決定怎麼組裝**（How things connect）
3. **Schema 決定資料長什麼樣**（What data looks like）
4. **AI Agent 負責把它寫出來**（Implementation）

---

## 3. 案例對照（Worked Examples）

### 3.1 案例一：EMI 數位課程系統
| 層級 | 內容範例 |
|---|---|
| Customer Needs | 教師希望快速建立 EMI 數位課程；學生希望有 AI 助教；學校希望追蹤學習歷程 |
| Product Goals | Goal 1：建立 EMI 課程網站／Goal 2：提供 AI 問答功能／Goal 3：產出學習分析報表 |
| Open Spec | 教師可以建立課程；學生可以上傳作業；AI Coach 可以回答問題；每次對話都必須紀錄 |
| Graphiti | Course ├─ Module ├─ Student ├─ AI Coach └─ Learning Analytics；或 Frontend → API Gateway → AI Service → Database |
| Schema | Course（id, title, description）／Student（id, name, email） |
| AI Coding | 由 Claude Code / Codex / Cursor 依據上述 Open Spec、Graphiti、Schema 開始寫程式 |

### 3.2 案例二：建築比喻（開咖啡廳）
| 層級 | 咖啡廳對照 |
|---|---|
| Customer Needs | 我要開咖啡廳 |
| Product Goals | 50 個座位、可外帶 |
| Open Spec | 要有吧檯、廚房、洗手間 |
| Graphiti | 吧檯和廚房怎麼連接；排水管怎麼走；電線怎麼配置 |
| Schema | 每個房間尺寸；桌椅數量；插座位置 |
| AI Coding | 最後施工 |

👉 核心洞察：兩個案例的結構完全同構（isomorphic）——不論是蓋咖啡廳還是蓋軟體系統，「需求 → 目標 → 規格 → 關係 → 資料/尺寸 → 動工」的順序是通用的專案邏輯，AI-native 開發只是把「動工」的執行者換成了 AI Agent。

---

## 4. 角色與工具對應（Roles & Tools Mapping）

### 4.1 誰負責哪一層
| 層級 | 主要負責人 | AI 涉入程度 |
|---|---|---|
| Customer Needs | 客戶 / 使用者 / PM | 低（可用 AI 輔助訪談整理） |
| Product Goals | PM / 產品負責人 | 低～中 |
| Open Spec | PM + 工程師 | 中（AI 可協助撰寫規格草稿） |
| Architecture / Graphiti | 架構師 / 資深工程師 | 中～高（AI 可提出架構建議） |
| Schema | 工程師 / 資料設計者 | 中～高（AI 可生成 schema 草案） |
| AI Coding | AI Agent | 高（AI 為主要執行者，人類審查） |
| Production | 工程師 / DevOps | 中（人類把關部署與監控） |

### 4.2 工具對應
- **Claude Code / Codex / Cursor**：介入點在最後一層「AI Coding」，但輸入依據是前面五層（Open Spec + Graphiti + Schema）的產出。規格與結構定義得越清楚，AI 產出程式碼的準確度越高。
- **Graphiti（工具）**：介入點在 Architecture 層，且會延伸進入 Production——當系統上線後，AI Coach 仍持續透過 Graphiti 讀寫知識圖譜，讓「關係」這一層在正式環境中也持續更新（詳見 1.3 節）。

---

## 5. 常見誤解與釐清（Common Misconceptions）

1. **誤解**：以為六層是嚴格的線性流程，走完一層才能走下一層。
   👉 **釐清**：只有前三層（Needs → Goals → Spec）與最後兩層（Coding → Production）較線性；Graphiti 與 Schema 之間是疊代關係，需要來回修正。

2. **誤解**：以為 AI-native 開發代表人類不需要做架構設計。
   👉 **釐清**：AI-native 開發代表人類的重心「上移」到定義 Spec / Graphiti / Schema，而非消失。規格模糊時，AI 寫出來的程式碼品質會直接下降。

3. **誤解**：以為 Schema 只是資料庫表格設計，跟架構無關。
   👉 **釐清**：Schema 是 Graphiti（關聯）的具體化，兩者必須互相驗證，否則會出現「有關聯沒欄位」或「有欄位沒關聯」的落差。

---

## 6. 教學延伸（Teaching Extensions）— 供課程開發使用

### 6.1 可能的課程模組拆解
- Module 1：Why AI-native？從傳統 SDLC 到 AI-native workflow 的典範轉移
- Module 2：需求訪談與 Product Goals 撰寫實作
- Module 3：Open Spec 工作坊（以 EMI 課程系統為練習案例）
- Module 4：Architecture / Graphiti 繪圖實作（ER 圖、系統關聯圖）
- Module 5：Schema 設計與 Graphiti↔Schema 疊代練習
- Module 6：AI Coding 實作（用 Claude Code / Cursor 依規格產出程式碼）
- Module 7：從 Production 回頭檢視 Spec／Schema 是否有落差（案例回顧）

### 6.2 課堂討論問題
- 如果 Product Goals 寫得很模糊，會如何影響後面 Open Spec 與 AI Coding 的品質？
- 舉一個你熟悉的系統（如選課系統、社群 App），試著把它拆解成六層。
- 為什麼 Graphiti 與 Schema 需要「互相疊代」而不是「一次到位」？請舉一個實際會發生落差的例子。
- 在 AI-native 開發中，PM／架構師／工程師的職責邊界如何重新劃分？

### 6.3 練習設計（Workshop Exercise）
給定一個簡單情境（例如：「我要做一個學生打卡系統」），讓學生分組完成：
1. 寫出 3 條 Customer Needs
2. 轉譯成 2-3 個 Product Goals
3. 展開成 Open Spec（至少 4 條系統行為敘述）
4. 畫出 Graphiti（物件關聯圖）
5. 設計對應的 Schema（至少 2 張表、每張表 3-5 個欄位）
6. （進階）用 AI 編碼工具依據 1-5 的產出，實際生成一段程式碼，並檢視是否需要回頭修正 Graphiti 或 Schema

### 6.4 評量重點建議
- 是否能正確區分「Why / What outcome / What system does / How connect / What data looks like」五個問題層次
- 是否能識別 Graphiti 與 Schema 之間的落差並主動修正（體現「疊代」而非「一次到位」的理解）
- 最終 AI 生成程式碼的品質，是否直接反映規格撰寫的清晰程度（可作為「規格品質」的驗收指標）

---

## 7. AI-ready 結構（給機器讀）

```yaml
tags:
  - ai-native-development
  - product-management
  - software-architecture
  - open-spec
  - graphiti
  - schema-design
  - ai-coding
  - emi-course-development
  - workflow-framework

relations:
  - CustomerNeeds -> ProductGoals
  - ProductGoals -> OpenSpec
  - OpenSpec -> Architecture_Graphiti
  - Architecture_Graphiti <-> Schema
  - Schema -> AICoding
  - AICoding -> Production
  - Graphiti -> defines -> Relationships_between_entities
  - Schema -> defines -> Shape_of_data
  - OpenSpec -> defines -> What_system_must_do
  - AICoding_Tools -> [ClaudeCode, Codex, Cursor]
  - CoffeeShop_Analogy -> isomorphic_to -> Software_Development_Workflow
  - Graphiti_Concept -> generic_meaning -> Architecture_relationship_diagram
  - Graphiti_Tool -> specific_meaning -> getzep_graphiti_temporal_knowledge_graph
  - Graphiti_Tool -> extends_into -> Production
  - Graphiti_Tool -> enables -> AI_Agent_runtime_memory_query
  - VectorDatabase -> knows -> Similarity
  - GraphDatabase -> knows -> Relationships
  - Graphiti_Tool -> combines -> [VectorDatabase, GraphDatabase]
  - Graphiti_Tool -> adds -> Temporal_Evolution
  - Graphiti_Tool -> composed_of -> [Nodes, Edges, Similarity, Context_and_Time]
  - Graphiti_Tool -> summarized_as -> Evolving_Mind_Map_for_AI
```

---

## ✅ 升級報告

### 你原本筆記的問題
👉 有內容，也已經有清楚的六層流程與兩個範例（EMI 課程、咖啡廳比喻），但：
- 缺乏正式的「定義區塊」，六層各自的核心問題沒有被系統化整理成對照表
- Graphiti 與 Schema 之間「非線性疊代」的關係只有一句話帶過，沒有展開說明「為什麼」與「怎麼疊代」
- 缺少角色分工（誰做哪一層、AI 介入程度多少）
- 缺少可教學使用的延伸內容（課程模組、討論題、練習設計、評量重點）
- 缺少 AI-ready 的 tags/relations 區塊

### 補上的升級點

1️⃣ **結構（Structure）**：把原本的線性敘述整理成「定義表 → 核心架構 → 案例對照表 → 角色工具對應 → 教學延伸」五大區塊，並統一中英對照標題。

2️⃣ **系統（System）**：新增角色與工具對應表（第 4 節），釐清人類與 AI 在六層中各自的責任比重，也標記出原文中「Graphiti」一詞可能的歧義並留待確認。

3️⃣ **流程（Flow）**：保留並強化原本的箭頭流程圖，並把「Graphiti ↔ Schema 疊代」單獨拆出一節說明其雙向性與具體發生情境（第 2.2 節）。

4️⃣ **關係（Relations）**：在文末加入 AI-ready 的 `tags` 與 `relations` 區塊，將六層之間、以及 Graphiti/Schema 的雙向關係、工具對應關係都用機器可讀的格式列出。

### 下一步（Level 4 建議）
- [ ] 已確認：Graphiti 同時指通用概念（架構關聯圖）與特定工具（getzep/graphiti），已補上 1.3 節說明兩者如何在 AI-native 系統中疊合
- [ ] 挑一個你正在做的實際專案（例如 SMMC-EMI 或 AI-SD 課程網站），把六層架構實際套用一次，產出一份「Working Spec」文件
- [ ] 將第 6 節的教學延伸內容進一步展開成完整的課程大綱（含每週時數、教材、作業）
- [ ] 補充 1-2 個失敗案例（Spec 模糊導致 AI Coding 出錯的真實經驗），增加教材的說服力
