from aiogram import types
from utils.keyboard import *
from bot import bot
from utils import stringMap


with open('data/category.txt', 'r', encoding='utf-8') as category:
    selected_category = category.read()



async def menu(message):
    
    global selected_category
    selected_category = message.text
    with open("img/menu.jpg", 'rb') as img:
        await bot.send_photo(
            chat_id=message.chat.id,

            photo=img,

            caption="""Выберите один из наших разделов:\n""" +
            stringMap('\n<b>--', data.categories, '</b>\n'),
            reply_markup=category_kb
        )