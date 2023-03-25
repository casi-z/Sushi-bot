from aiogram import types
from utils.keyboard import *
from .bot import bot

img = types.InputFile("./img/menu.jpg")

def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str
def text(array):
    return "\n".join(array)

def main(message):
    return bot.send_photo(
        chat_id=message.chat.id,

        photo=img,

        caption="""Выберите один из наших разделов:\n""" +
        stringMap('\n<b>--', data.categories, '</b>\n'),
        reply_markup=category_kb
    )