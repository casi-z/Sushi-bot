from aiogram import types
from utils.keyboard import *
from .bot import bot

photo = types.InputFile("./img/fon.jpg")


def text(array):
    return "\n".join(array)


def main(message):
    return bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=text(
            [
                "Приветствуем вас за столом нашего уютноо заведения!",
                "Будь как дома путник",
                "",
                "<b>Что бы увидеть меню пишите:</b>",
                "",
                "menu",
            ]
        ),
        reply_markup=start_kb,
    )
