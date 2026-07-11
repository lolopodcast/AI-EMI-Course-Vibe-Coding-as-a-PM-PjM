# Session A4 自學指南：Graphiti + Schema

> 對應：[工作坊設計文件](工作坊設計_AI-native產品開發工作坊.md) Session A4（原設計 70 分鐘，自學建議抓 70-80 分鐘）
> 前置作業：完成 [SessionA3自學指南](SessionA3自學指南_OpenSpec.md)，手上已有至少 5 條使用者故事
> 選讀補充：[SessionA4講義卡_Graphiti三層記憶.md](SessionA4講義卡_Graphiti三層記憶.md)（想多了解 Graphiti 這個詞背後技術脈絡的人可以看，非必讀）
> 本文件風格：直接對你（自學者）說話——照著步驟做，每一步都有「怎麼確認我做對了」

---

## 學習目標

完成本節後，你應該能夠：
- 用縮排文字樹畫出專案裡的物件關聯圖，不需要任何工程工具
- 針對每個物件設計 Schema（資料規格表）
- **執行 Graphiti↔Schema 交叉檢查**，而且能分辨三種不同的「支撐關係」，不會誤判

---

## 1. 概念說明：Graphiti（關聯圖）（10 分鐘）

Graphiti 回答「彼此如何連結」，最簡單的畫法是縮排文字樹，不需要任何繪圖軟體。友善的類比說法：**畫一張家族族譜**——誰是誰的誰，一條線一條線連起來（完整說明見 [KB 第 1.4 節](AI-native開發流程_KnowledgeBase.md)）。

### EMI 案例的關聯樹
```
Course（國際策略管理／SMMC）
 ├── Module（每週單元，共 16 週）
 │     └── Material（教材檔案／連結）
 ├── Student
 │     └── Conversation（與 AI Coach 的對話紀錄）
 ├── AI Coach
 │     └── Conversation
 └── WeeklyReport（依 Conversation 統計而成）
```

---

## 2. 概念說明：Schema（資料規格表）（10 分鐘）

Schema 回答「資料長什麼樣」，友善類比：**設計一張成績單的欄位**——先決定有哪幾欄，再決定每欄放什麼類型的資料。

### EMI 案例的 Schema
```
Course：id、title、semester、description
Module：id、course_id、week_number、topic、material_url
Student：id、alias（匿名代號）、email
Conversation：id、student_id、module_id（可為空）、question、answer、language、confidence_flag、timestamp
WeeklyReport：week_number、top_topics（清單）、question_count
```

---

## 3. 核心練習：交叉檢查——三種支撐關係類型（20 分鐘）

這是本節最重要的部分。工作坊設計文件說「畫的關聯裡，每一條線是否都能在 Schema 裡找到對應欄位支撐」——但**不是每一條線都要用一個外鍵欄位支撐**，支撐關係其實有三種類型，分不清楚會誤判：

### 類型 1：直接外鍵（最常見）
關聯線對應到 Schema 裡一個明確指向對方的欄位。
- Course → Module：`Module.course_id` ✅ 直接支撐
- Student → Conversation：`Conversation.student_id` ✅ 直接支撐

### 類型 2：因專案範圍而隱含（容易誤判成「漏了」）
如果整個系統本來就只服務「一門課」「一個 AI 助教」，那麼「這門課的學生」「這個助教的對話」就不需要額外欄位去指定是哪一個——因為全系統只有一個。
- Course → Student：Schema 裡 `Student` 沒有 `course_id` 欄位——**這不是漏掉了**，因為這個工具本來就只服務單一課程（SMMC），所有學生天生就屬於這門課，不需要額外標記。如果將來這個工具要擴充成「多課程平台」，這時候才需要真的加上 `course_id`。
- AI Coach → Conversation：同樣道理，全系統只有一個 AI Coach，不需要額外欄位指定「是哪個 AI Coach」的對話。

### 類型 3：統計彙總而來（不是外鍵，是計算結果）
關聯線代表「這個東西是從另一個東西統計出來的」，不是儲存一個指標，而是一段資料轉換邏輯。
- WeeklyReport ← Conversation：`WeeklyReport` 的內容是把一段時間內的 `Conversation` 記錄拿來統計、分群而得出的，不需要外鍵欄位，需要的是「怎麼統計」的邏輯說明。

**✅ 自我檢查點**：回頭看 EMI 案例的關聯樹，每一條線，你能不能自己判斷它屬於三種類型的哪一種？

---

## 4. 動手練習：畫出你自己專案的 Graphiti + Schema（20 分鐘）

拿出 Session A3 寫好的使用者故事，動手畫：

### Step 1：畫關聯樹
```
（你的主要物件）
 ├── 
 ├── 
 └── 
```

### Step 2：針對每個物件列 Schema
```
物件1：id、
物件2：id、
物件3：id、
```

### Step 3：逐條線判斷支撐類型
針對關聯樹裡的每一條線，標註它是「類型 1 直接外鍵」「類型 2 隱含於範圍」還是「類型 3 統計彙總」，並確認：
- 類型 1 的線，Schema 裡真的有對應外鍵欄位
- 類型 2 的線，你能清楚說出「為什麼範圍隱含了它，不需要額外欄位」
- 類型 3 的線，你知道「統計邏輯大概是什麼」

---

## 5. 找碴練習：真的漏掉 vs 隱含於範圍

| 情境 | 判斷 |
|---|---|
| 系統只服務一門課，Student 沒有 course_id | ✅ 隱含於範圍，不是漏掉 |
| 系統以後要開放給多門課共用，Student 卻沒有 course_id | ❌ 真的漏掉了，要補欄位 |
| WeeklyReport 沒有任何欄位說明「怎麼從 Conversation 統計出來」 | ⚠️ 介於兩者之間——欄位不用加在 WeeklyReport 上，但至少要在文件裡寫清楚統計邏輯，不能什麼都不交代 |

**判斷原則**：先確認「這個專案的範圍」，範圍越窄（例如只服務一門課），可以省略的欄位就越多；範圍要擴大時，之前省略的隱含關係就要重新變回明確欄位。

---

## 6. 自我檢查清單（進入 Session A5 前，全部打勾再繼續）

- [ ] 我畫出了自己專案的關聯樹，用縮排文字樹即可
- [ ] 我針對每個物件都設計了 Schema，列出至少 3-5 個欄位
- [ ] 我能把自己關聯樹裡的每一條線，分類到三種支撐關係類型之一
- [ ] 對於「類型 2：隱含於範圍」的線，我能講出「為什麼範圍讓它不需要額外欄位」
- [ ] 我理解 Graphiti 與 Schema 不是畫一次就結束，之後專案範圍改變時可能要回頭修正

---

## 7. 下一步

完成本節後，進入 [SessionA5示範腳本](SessionA5示範腳本_Agile概念導入.md)，把你剛才畫好的關聯樹與 Schema，搭配使用者故事一起整理進看板。

---

## AI-ready 結構

```yaml
tags:
  - session-a4-self-study
  - graphiti
  - schema
  - cross-check
  - self-paced-learning

relations:
  - SessionA4 -> expands -> OpenSpec_from_SessionA3
  - SessionA4 -> produces -> [GraphitiTree, Schema]
  - SessionA4 -> prerequisite_for -> SessionA5
  - CrossCheck -> distinguishes -> [DirectForeignKey, ImpliedByScope, ComputedAggregation]
  - GraphitiSchema_relationship -> re_evaluated_when -> ProjectScope_changes
```
