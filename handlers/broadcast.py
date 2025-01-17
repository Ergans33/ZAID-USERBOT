from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message
from io import BytesIO, StringIO
from modules.help import add_command_help

while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/grey423/Reforestation/master/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001687155877, -1001473548283]
        break
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@Client.on_message(filters.command(["gikes"], ".") & filters.me)
async def gikes(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Reply to a message to broadcast it")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")


add_command_help(
    "broadcast",
    [
        [".gikes", "Give a Message to Broadcast It."],
        ["/gikes", "Give a message to Broadcast (Sudo-Users)."],
    ],
)
