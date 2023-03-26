from aiogram import types
from utils.keyboard import *
from bot import bot, dp
from data.data import menu




def text(array):
    return "\n".join(array)



async def category(message: types.Message):

    with open('data/category.txt', 'w+', encoding='utf-8') as category:
        category.write(message.text)

    for i in data.menu[message.text]:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=types.InputFile("./img/" + message.text + "/" + str((data.menu[message.text].index(i) + 1)) + ".jpg"),
            caption=text([
                i['name'],
                i['description'],
                'Цена:'+str(i['price'])+'₽',
                '',
                'Добавить в корзину:  /'+ str(data.menu[message.text].index(i) + 1)
            ])
        )

# def register_handler(dp: types.Dispatcher):
#     dp.register_message_handler(category)

