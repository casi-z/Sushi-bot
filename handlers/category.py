from aiogram import types
from utils.keyboard import *
from bot import bot, dp
import data.data as data
from utils import text



async def category(message: types.Message):

    with open('data/category.txt', 'w+', encoding='utf-8') as category:
        category.write(message.text)

   
    for i in data.menu[message.text]:
        
        await message.answer(
            text=text([
                i['name'],
                i['description'],
                'Цена:'+str(i['price'])+'₽',
                '',
                'Добавить в корзину:  /'+ str(data.menu[message.text].index(i) + 1)
            ])
        )
            
