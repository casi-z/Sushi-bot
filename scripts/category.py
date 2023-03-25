from aiogram import types
from utils.keyboard import *
from .bot import bot
from data.data import menu
from data.global_vars import selected_category
from scripts.bot import dp


def text(array):
    return "\n".join(array)

def main():
    @dp.message_handler(text=data.categories)
    async def process_start_command(message: types.Message):
        global selected_category
        selected_category = message.text
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