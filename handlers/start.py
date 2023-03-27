from aiogram import types
from utils.keyboard import *
from bot import bot
from utils import text


async def start(message: types.Message):
    with open('img/fon.jpg', 'rb') as photo:

        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=text(
                [
                    f"Приветствуем вас за столом нашего уютного заведения!",
                    "Будь как дома путник",
                    "",
                    "<b>Что бы увидеть меню пишите:",
                    "",
                    "/menu</b>",
                ]
            ),
            reply_markup=start_kb,
        )
