from aiogram import types
from utils.keyboard import *
from bot import bot, dp
import data.data as data
from utils import text



async def category(message: types.Message):

    with open('data/category.txt', 'w+', encoding='utf-8') as category:
        category.write(message.text)

   
    for i in data.menu[message.text]:
        # try:
        #     img = open("./img/" + message.text + "/" + str((data.menu[message.text].index(i) + 1)) + ".jpg")
        #     await bot.send_photo(
        #         chat_id=message.chat.id,
        #         photo=img,
        #         caption=text([
        #             i['name'],
        #             '',
        #             i['description'],
        #             '',
        #             'Цена: <b>'+str(i['price'])+'₽</b>',
        #             '',
        #             'Добавить в корзину:  /'+ str(data.menu[message.text].index(i) + 1)
        #         ])
        #     )

        # finally: img.close()
        await message.answer(
            text=text([
                i['name'],
                '',
                i['description'],
                '',
                'Цена: <b>'+str(i['price'])+'₽</b>',
                '',
                'Добавить в корзину:  /'+ str(data.menu[message.text].index(i) + 1)
            ])
        )
            
