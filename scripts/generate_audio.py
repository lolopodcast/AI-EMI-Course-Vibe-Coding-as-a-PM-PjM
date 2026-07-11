# -*- coding: utf-8 -*-
"""Generate pre-recorded narration audio (mp3) for 工作坊行銷簡報.html using edge-tts.
Voices: zh-TW-HsiaoYuNeural (the "Yating" voice) / en-GB-RyanNeural (British male).
Run: python scripts/generate_audio.py
"""
import asyncio
import os

ZH_VOICE = "zh-TW-HsiaoYuNeural"
EN_VOICE = "en-GB-RyanNeural"

NARR = [
    {
        "zh": "你有沒有想過，其實不用會寫程式，你也可以自己主導開發一個課程數位產品？接下來我想跟你分享一套我們設計出來的工作坊——它讓大學教師，不需要任何程式背景，就能扮演產品經理與專案經理的角色，用 AI 把你的教學想法，變成真正能用的數位工具。",
        "en": "Have you ever imagined leading the development of a digital product for your course, without writing a single line of code? I want to share a workshop we designed. It lets university faculty, with zero programming background, take on the role of product manager and project manager, and use AI to turn their teaching ideas into something real.",
    },
    {
        "zh": "第一部：為什麼需要新的做法。",
        "en": "Part One: why we need a new approach.",
    },
    {
        "zh": "我們都遇過類似的狀況：EMI 全英語授課，學生課後常常看不懂教材，卻不敢舉手發問；老師想幫忙，卻沒有時間一一回覆重複性的問題；系所也希望能追蹤學生在哪些單元卡關，但手上沒有合適的工具。過去，這些問題的解法通常是——去找工程師、去找廠商，然後開始漫長的溝通與等待。",
        "en": "We've all seen this: in English-medium instruction, students often can't keep up after class but hesitate to ask questions. Instructors don't have time to answer the same questions repeatedly. And departments want to track where students get stuck, but lack the right tool. In the past, the only fix was hiring engineers or vendors, then waiting through long rounds of back and forth.",
    },
    {
        "zh": "但現在情況不一樣了。AI 時代真正改變的，不是要不要用 AI，而是開發一個數位產品的整個流程。我們把它整理成六層架構：先問為什麼要做，這是 Needs；再問要達成什麼結果，這是 Goals；然後決定系統必須做什麼，這是 Spec；接著畫出彼此怎麼連結，這是 Graphiti；再定義資料長什麼樣，這是 Schema；最後，才是動手實作。用一句話說：Spec 決定做什麼，Graphiti 決定怎麼組裝，Schema 決定資料長怎樣，而 AI Agent 負責把它寫出來。",
        "en": "But things have changed. What AI really transforms isn't whether to use it, it's the entire process of building a digital product. We organized it into six layers: first ask why, that's Needs; then what outcome, that's Goals; then what the system must do, that's Spec; then how things connect, that's Graphiti; then what the data looks like, that's Schema; and only then, implementation. In one sentence: Spec decides what to build, Graphiti decides how it connects, Schema decides what the data looks like, and the AI agent writes it.",
    },
    {
        "zh": "這代表什麼？代表老師的角色，從不會寫程式所以做不了，變成負責定義要做什麼、怎麼組裝、資料長怎樣的產品經理與專案經理。真正動手把程式碼寫出來的，是 AI，具體來說，是 Claude Code。你不需要學程式語言，你只需要學會怎麼把你的教學需求說清楚。",
        "en": "This means the instructor's role shifts, from 'I can't code, so I can't build this' to 'I define what to build, how it connects, and what the data looks like,' acting as both product manager and project manager. The one actually writing the code is AI, specifically Claude Code. You don't need to learn a programming language. You just need to learn how to state your teaching needs clearly.",
    },
    {
        "zh": "第二部：實際上怎麼做。",
        "en": "Part Two: how it actually works.",
    },
    {
        "zh": "所以我們設計了一套工作坊，分成兩個模組，各六小時。基礎模組，完全不需要碰任何 AI 工具，專注在把你的教學想法，一層一層轉譯成清楚的規格，同時導入 Agile 專案管理的必要概念，像是看板、衝刺、完成的定義。實施模組，才正式開始動手，用 Claude Code 把規格變成真正能運作的原型，還會學到怎麼把工作拆給多個 AI 代理人同時處理，加快速度。如果時間有限，我們也準備了快速精華版：基礎模組三小時，實施模組三小時，一樣可以完整走過六層架構。",
        "en": "So we designed a workshop in two six-hour modules. The Foundations module needs no AI tools at all, it focuses on translating your teaching ideas, layer by layer, into a clear specification, while introducing essential Agile concepts like Kanban boards, sprints, and definition of done. The Implementation module is where the hands-on work begins, using Claude Code to turn the spec into a working prototype, and learning to delegate tasks to multiple AI agents running in parallel. If time is limited, we also offer a condensed track: three hours of foundations and three hours of implementation, still covering the full six-layer framework.",
    },
    {
        "zh": "這不是紙上談兵。我們實際用一個真實案例走過一次——駱世民教授的 EMI 課程，國際策略管理。學生英語授課常跟不上，老師沒時間逐一解惑。我們把需求一層一層寫成規格，交給 Claude Code，很快就做出一個雙語 AI 助教的原型。更關鍵的是，我們還故意示範了一次，如果規格寫得模糊，AI 做出來的東西會少了什麼。這個對比，讓在場的老師親眼看到：規格的清晰度，直接決定了 AI 產出的品質。",
        "en": "This isn't just theory. We walked through a real case, Professor Shihmin Lo's EMI course, Strategic Management of Multinational Corporations. Students struggled to keep up in English, and the instructor had no time to answer every question. We wrote the requirements layer by layer, handed them to Claude Code, and quickly had a working bilingual AI teaching assistant prototype. Just as important, we deliberately ran it again with a vague spec, so everyone could see exactly what a clear specification changes.",
    },
    {
        "zh": "更進階一點，當專案有好幾件事要同時做，比如課程頁面、AI 助教、還有學習報表，我們也會教老師怎麼用一句話，請 Claude Code 同時派出好幾個 AI 代理人平行處理，甚至互相審查彼此的成果。老師不需要懂任何技術細節，只需要學會判斷：哪些工作可以同時做，哪些工作有先後順序。",
        "en": "One step further: when a project has several things to build at once, a course page, an AI assistant, a learning report, we also teach instructors how to ask Claude Code, in one sentence, to dispatch multiple AI agents in parallel, and even have them review each other's work. No technical detail required, just the judgment to know what can run in parallel, and what has to wait its turn.",
    },
    {
        "zh": "第三部：你會帶走什麼、為什麼是現在。",
        "en": "Part Three: what you'll take away, and why now.",
    },
    {
        "zh": "完成這套工作坊，你會帶走的不只是一場工作坊的回憶，而是四樣實際的東西：一份完整的專案規格包、一個真正可以運作的原型、一份可以直接交給 TA 或協作教師的交接文件、還有一套帶團隊做 AI 專案的協作方法。",
        "en": "By the end of this workshop, you won't just walk away with a memory of the session, you'll walk away with four concrete things: a complete project specification, a working prototype, a handoff document your TA or co-instructor can pick up directly, and a method for leading a team through an AI-native project.",
    },
    {
        "zh": "這跟坊間很多 AI 工具教學不一樣。我們不是教你怎麼跟 AI 聊天，而是教你一套完整的專案定義紀律，這套紀律，不管 AI 工具怎麼換，都會一直有用。",
        "en": "This is different from most AI tool tutorials out there. We're not teaching you how to chat with AI, we're teaching you a complete discipline for defining problems. And that discipline keeps working no matter which AI tool comes next.",
    },
    {
        "zh": "如果你也想讓自己的課程，變成一個真正能用的數位產品，而且完全不需要先學程式，歡迎加入這場工作坊。基礎模組六小時，實施模組六小時；如果時間有限，也有三小時加三小時的快速精華版，一起把你的教學想法，變成看得到、用得到的東西。",
        "en": "If you want to turn your course into a real, working digital product, without learning to code first, join this workshop. Six hours of foundations, six hours of implementation, or a condensed three-plus-three track if time is tight. Let's turn your teaching ideas into something you can see, and something your students can use.",
    },
]

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "audio")


async def gen_one(text, voice, out_path):
    import edge_tts
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_path)


async def main():
    zh_dir = os.path.join(BASE_DIR, "zh")
    en_dir = os.path.join(BASE_DIR, "en")
    os.makedirs(zh_dir, exist_ok=True)
    os.makedirs(en_dir, exist_ok=True)

    for i, item in enumerate(NARR, start=1):
        zh_path = os.path.join(zh_dir, "{:02d}.mp3".format(i))
        en_path = os.path.join(en_dir, "{:02d}.mp3".format(i))
        print("Generating", zh_path)
        await gen_one(item["zh"], ZH_VOICE, zh_path)
        print("Generating", en_path)
        await gen_one(item["en"], EN_VOICE, en_path)

    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
