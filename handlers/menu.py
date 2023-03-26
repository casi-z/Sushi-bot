from aiogram import types
from utils.keyboard import *
from bot import bot

with open('data/category.txt', 'r', encoding='utf-8') as category:
    selected_category = category.read()

img = types.InputFile("./img/menu.jpg")

def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str
def text(array):
    return "\n".join(array)


def main(message):
    global selected_category
    selected_category = message.text
    return bot.send_photo(
        chat_id=message.chat.id,

        photo=img,

        caption="""Выберите один из наших разделов:\n""" +
        stringMap('\n<b>--', data.categories, '</b>\n'),
        reply_markup=category_kb
    )