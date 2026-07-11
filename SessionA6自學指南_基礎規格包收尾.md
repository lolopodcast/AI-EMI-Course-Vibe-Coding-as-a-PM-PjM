# Session A6 自學指南：收尾——整合成基礎規格包

> 對應：[工作坊設計文件](工作坊設計_AI-native產品開發工作坊.md) Session A6（原設計 30 分鐘，自學建議抓 30-40 分鐘）
> 前置作業：完成 A1-A5，手上應該已有：專案宣言、Customer Needs、Product Goals、Open Spec（5 條故事+DoD）、Graphiti 關聯樹、Schema、初版看板
> 本文件風格：直接對你（自學者）說話——這是基礎模組最後一節，目的是把前面散落的產出，整理成一份完整文件

---

## 學習目標

完成本節後，你應該能夠：
- 把 A1-A5 的所有產出，整合成一份「基礎規格包」
- 做最後一次交叉檢查，確認各項產出彼此一致、沒有矛盾
- 準備好進入實施模組（Session B1 起）

---

## 0. 為什麼要花時間做收尾

Session B2 會直接把你今天寫的東西，整段貼給 Claude Code。**如果現在整理得亂七八糟，Session B2 會直接卡關**。這 30 分鐘不是行政作業，是替下一階段鋪路。

---

## 1. 整合清單：把 A1-A5 的產出蒐集起來（10 分鐘）

逐項確認你手上有沒有這些東西（沒有的話回頭補）：

- [ ] 一句話專案宣言（Session A1）
- [ ] 至少 3 條 Customer Needs（Session A2）
- [ ] 2-3 個 Product Goals，附可衡量指標（Session A2）
- [ ] 至少 5 條使用者故事，附完成的定義（Session A3）
- [ ] Graphiti 關聯樹（Session A4）
- [ ] Schema 資料規格表（Session A4）
- [ ] 一張初版看板，含優先順序（Session A5）

---

## 2. 最終交叉檢查（15 分鐘）

這是本節真正的重點——不是把東西複製貼上就好，而是要檢查**它們彼此對不對得起來**：

### 檢查 1：Goals 是結果指標，不是功能清單
拿出 Product Goals，重新用 [SessionA2自學指南](SessionA2自學指南_NeedsToGoals.md) 第 2 節的判斷原則檢查一次。

### 檢查 2：每條 Open Spec 都有具體的 DoD
拿出使用者故事清單，重新用 [SessionA3自學指南](SessionA3自學指南_OpenSpec.md) 第 2 節的判斷原則檢查一次。

### 檢查 3：Graphiti 每條關聯線，Schema 都有欄位支撐
把 Graphiti 關聯樹跟 Schema 表格並排放，逐條確認：畫出來的每一條連結，是不是都能在 Schema 裡找到對應欄位？如果有一條線找不到欄位支撐，代表 Schema 還沒設計完整，回頭補。

### 檢查 4：看板上的卡片，都能對應到某一條 Open Spec
翻開你的看板，逐張卡片檢查：這張卡片是不是都能追溯回某一條使用者故事？如果有卡片對不到任何故事，代表要嘛是故事漏寫了，要嘛這張卡片其實不是這個階段該做的事。

**✅ 自我檢查點**：四項檢查都做完，且都能打勾，才算真正的「基礎規格包」完成。

---

## 3. 整理成一份文件

建議直接借用 [交接文件範本_AI-native專案.md](交接文件範本_AI-native專案.md) 的第 1-6 節作為容器：
- 第 1 節：填入專案基本資訊（用你的專案宣言）
- 第 2-6 節：依序貼入 Needs／Goals／Open Spec／Graphiti／Schema

看板本身不屬於交接文件的章節，建議另外用截圖或連結（例如 Trello／Notion 網址）附加在文件旁邊，作為「目前工作排序」的參考。

**這份文件就是你的「基礎規格包 v1」**，Session B2 會直接用到它。

---

## 4. 自我檢查清單（進入 Session B1 前，全部打勾再繼續）

- [ ] 第 1 節整合清單，7 項全部有內容
- [ ] 第 2 節四項交叉檢查，全部確認過且沒有矛盾
- [ ] 我已經把內容整理進交接文件範本的第 1-6 節（或至少整理成一份單一文件）
- [ ] 我知道 Session B1 開始，就要正式碰 Claude Code 了

---

## 5. 下一步

完成本節，代表整個基礎模組完成了。接下來進入 [SessionB1自學指南](SessionB1自學指南_ClaudeCode入門.md)，安裝並第一次啟動 Claude Code，準備在 Session B2 把這份基礎規格包變成真正的原型。

---

## AI-ready 結構

```yaml
tags:
  - session-a6-self-study
  - foundation-spec-pack
  - cross-check
  - self-paced-learning

relations:
  - SessionA6 -> consolidates -> [SessionA1, SessionA2, SessionA3, SessionA4, SessionA5]
  - SessionA6 -> produces -> 基礎規格包_v1
  - SessionA6 -> uses_container -> 交接文件範本_AI-native專案_第1到6節
  - SessionA6 -> prerequisite_for -> SessionB1
  - 基礎規格包_v1 -> consumed_by -> SessionB2
```
