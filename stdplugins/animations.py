"""Available Commands:
.hilao // 👉✊️💦
.sex // 🤵👼👰
.kiss // 🤵💋👰
.git
.🍎 to print a stack of 🍎
.police
.gaand
.loading
.square
.up
.round
.heart
.plane
.clock
.tclock
  © [cHAuHaN](http://t.me/amnd33p)"""
from telethon import events
import asyncio
import time
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 100)
    input_str = event.pattern_match.group(1)
    if input_str == "loading":
        animation_chars = [
            "▮",
            "▯",
            "▬",
            "▭"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "square":
        animation_chars = [
            "◧",
            "◨",
            "◧",
            "◨"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "up":
        animation_chars = [
            "╹",
            "╻",
            "╹",
            "╻"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "round":
        animation_chars = [
            "⚫",
            "⬤",
            "●",
            "∘"
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 4])
    if input_str == "heart":
        animation_chars = [
            "🖤",
            "💜",
            "💙",
            "💚",
            "💛",
            "🧡",
            "‎"
        ]
        for i in animation_ttl:
            await asyncio.sleep(0.4)
            await event.edit(animation_chars[i % 6])
    if input_str == "plane":
        animation_chars = [
            "✈-------------",
            "-✈------------",
            "--✈-----------",
            "---✈----------",
            "----✈---------",
            "-----✈--------",
            "------✈-------",
            "-------✈------",
            "--------✈-----", 
            "---------✈----",
            "----------✈---",
            "-----------✈--",
            "------------✈-",
            "-------------✈"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 14])
    if input_str == "clock":
        animation_chars = [
            "🕛",
            "🕐",
            "🕑",
            "🕒",
            "🕓",
            "🕔",
            "🕕",
            "🕖",
            "🕗",
            "🕘",
            "🕙"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
    if input_str == "tclock":
        deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
        for _ in range(48):
            await asyncio.sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    if input_str == "🍎":
        animation_chars = [
                        " ‏‏‎               🍎",
                        "            🍎 🍎",
                        "        🍎 🍎 🍎",
                        "    🍎 🍎 🍎 🍎",
                        "🍎 🍎 🍎 🍎 🍎"
                    ]
        msg = ""
        for s in animation_chars:
            msg += s+"\n"
            await event.edit(msg)
            await asyncio.sleep(0.5)
    if input_str == "hilao":
        animation_chars = [
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️ ‏‏‎  ‏‏‎ ",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️ ‏‏‎  ‏‏‎ ",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉 ‏‏‎  ‏‏‎ ✊️",
            "👉 ‏‏‎ ✊️ ‏‏‎ ",
            "👉✊️💦 ‏‏‎ "
        ]
        for i in range(1, 44):
            await asyncio.sleep(0.2)
            await event.edit(animation_chars[i % 11])
    animation_ttl = range(1, 40)
    if input_str == "sex":
        animation_chars = [
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👼👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ "
        ]
        for i in range(1, 40):
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])
    animation_ttl = range(1, 40)
    if input_str == "kiss":
        animation_chars = [
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎  ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵 ‏‏‎ 👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ ",
            "🤵💋👰 ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ "
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])
    if input_str == "gaand":
         animation_chars = [
                    "me",
                    "loge",
                    "kya?",
                    "gaand"
            ]
         for i in range(0,11):
             await asyncio.sleep(0.3)
             await event.edit(animation_chars[i % 4])
    if input_str == "hibuse":
        animation_chars = [
            "👁👁\n  👄  =====> Abey Ja Na Gandu",
            "👁👁\n  👅  =====> Abey Ja Na Madarchod",    
            "👁👁\n  💋  =====> Abey Ja Na Randi",
            "👁👁\n  👄  =====> Abey Ja Na Betichod",
            "👁👁\n  👅  =====> Abey Ja Na Behenchod",    
            "👁👁\n  💋  =====> Abey Ja Na Na Mard",
            "👁👁\n  👄  =====> Abey Ja Na Randi",
            "👁👁\n  👅  =====> Abey Ja Na Bhosdk",    
            "👁👁\n  💋  =====> Abey Ja Na Chutiye",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]
        for hi in animation_chars:
            await event.edit(hi)
            await asyncio.sleep(0.5)
    if input_str == "police":
        animation_chars = [
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
            "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
            "**Police is Here**"
            ]
        for i in range(0, 11):
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 11])
    if input_str == "git":
        animation_chars = [
            "h"
            "ht"
            "htt"
            "http"
            "https:"
            "https:/"
            "https://"
            "https://g"
            "https://gi"
            "https://git"
            "https://gith"
            "https://githu"
            "https://github"
            "https://github.c"
            "https://github.co"
            "https://github.com"
            "https://github.com/"
            "https://github.com/c"
            "https://github.com/cH"
            "https://github.com/cHA"
            "https://github.com/cHAu"
            "https://github.com/cHAuH"
            "https://github.com/cHAuHa"
            "https://github.com/cHAuHaN"
            "https://github.com/cHAuHaNz"
            "https://github.com/cHAuHaNz/"
            "https://github.com/cHAuHaNz/T"
            "https://github.com/cHAuHaNz/TG"
            "https://github.com/cHAuHaNz/TGU"
            "https://github.com/cHAuHaNz/TGUs"
            "https://github.com/cHAuHaNz/TGUse"
            "https://github.com/cHAuHaNz/TGUser"
            "https://github.com/cHAuHaNz/TGUserB"
            "https://github.com/cHAuHaNz/TGUserBo"
            "https://github.com/cHAuHaNz/TGUserBot"
            "https://github.com/cHAuHaNz/TGUserBot/"
        ]
        for i in range(0, 36):
            await asyncio.sleep(0.1)
            await event.edit(animation_chars[i % 36])