# 講義卡：Graphiti 三分鐘搞懂（Session A4 現場發放）

> 用途：Session A4 尾聲發放的選讀小卡，給想多了解「Graphiti」這個詞為什麼特別的老師。完整技術說明見 [AI-native開發流程_KnowledgeBase.md](AI-native開發流程_KnowledgeBase.md) 第 1.3 節。
> **提醒**：A4 現場必教內容仍只是「用縮排文字樹畫關係地圖」，這張卡是選讀補充，不需要在 70 分鐘裡逐字講解，適合印出來讓有興趣的學員帶走。

---

## 正面｜一分鐘版本

**Graphiti 白話說法**：一張會「隨時間更新」的關係地圖

| 系統 | 知道什麼 | 例子 |
|---|---|---|
| 向量資料庫 | 哪些東西「像」 | EMI 課程 ≈ 數位課程 |
| 圖資料庫 | 哪些東西「有關」 | 老師 ─教─► 課程 |
| **Graphiti** | 像＋有關＋**還記得怎麼變化** | 「2026 年新增 AI 助教」「某個功能後來停用了」 |

👉 一句話：向量資料庫知道「像不像」；圖資料庫知道「有沒有關係」；Graphiti 兩者都知道，還多記住「什麼時候變的」。

---

## 背面｜進階：四個組成元素（選讀）

- 🔵 **節點（Nodes）**：一個東西——人、課程、文件、Agent
- ➡️ **連結線／邊（Edges）**：兩個東西的關係——教、包含、呼叫、依賴
- 〰️ **相似性（Similarity）**：長得像的東西——AI 助教 ≈ Tutor Agent
- 🕐 **時間軸（Temporal Evolution）**：什麼時候變的——新增、換版本、停用

> **Graphiti = 心智圖 + 長期記憶 + 關係推理**
> 也可以說：**Graphiti ≈ 一張「AI 看得懂、會自己更新」的心智圖（Evolving Mind Map for AI）**

📎 今天課堂上，我們只需要畫「關係地圖」（縮排文字樹）就好，不用碰這個工具本身——這張卡只是讓你知道，這個詞背後在講什麼，之後如果團隊裡有工程師接手，會用得上。

---

## AI-ready 結構

```yaml
tags:
  - session-a4-handout
  - graphiti-three-tier-memory
  - quick-reference-card

relations:
  - HandoutCard -> condensed_from -> KB第1.3節
  - HandoutCard -> distributed_at -> SessionA4尾聲
  - HandoutCard -> optional_supplement_to -> SessionA4必教內容
```
