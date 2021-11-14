import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from prodil.BotConfig import ProDil
from prodil.utils.helpers import command
from prodil_client.client import api


@ProDil.on_message(command("hakkinda") & filters.private)
async def bot_about(client: Client, message: Message):
    await client.send_message(
        chat_id=message.chat.id,
        text=(
            "This bot has been created for CodeTheChange 2021, without expecting anything in return."
            "It is mainly made to help society with Mental Health issues. "
            "If you have any recommendations, please contact our developers"
            "\n\n__You can contact us through the following__"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("@babybirkins", url="https://t.me/babybirkins"),
                ],
                [InlineKeyboardButton("TEJBarbarians", url="https://discord.gg/d5CYv92d")],
                [
                    InlineKeyboardButton(
                        "Source Codes",
                        url="https://github.com/emiravc/CodeTheChange",
                    )
                ],
            ]
        ),
    )


@ProDil.on_message(filters.me & filters.media & filters.private)
async def bot_file_update(_: Client, message: Message):
    update = api.update_resource(
        file_name=message.document.file_name,
        file_size=message.document.file_size,
        file_id=message.document.file_id,
    )

    text = "Documents has not been updated."
    if update.status_code == 200:
        text = "Documents has been updated successfully."

    reply_message = await message.reply_text(text=f"`{text}`")
    await asyncio.sleep(3)
    await reply_message.delete()