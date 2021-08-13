import asyncio
import logging

from pyrogram import Client
from pyrogram.types import Message

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y/%m/%d %H:%M:%S",
    format="%(levelname)s: %(message)s",
)
queues = {}


def send_media_group(
    client: Client,
    media_group_id: int,
    chats: list[int],
) -> None:
    loop = asyncio.get_event_loop()
    for chat_id in chats:
        loop.create_task(client.forward_messages(chat_id, *queues[media_group_id]))


async def channel_handler(
    client: Client,
    msg: Message,
    channels: list[str],
    chats: list[int],
) -> None:
    loop = asyncio.get_event_loop()
    if msg.chat.username not in channels or msg.edit_date:
        return
    logging.info(msg.chat)
    if hasattr(msg, "media_group_id") and msg.media_group_id:
        if msg.media_group_id not in queues:
            queues[msg.media_group_id] = (msg.chat.id, [])
            loop.call_later(10, send_media_group, client, msg.media_group_id, chats)
        queues[msg.media_group_id][1].append(msg.message_id)
        return
    for chat_id in chats:
        await msg.forward(chat_id)
