from bot import dp
from aiogram import types, executor
from handlers import *


def on_command(dict):
    functions = list(dict.values())
    words = list(dict.keys())
    for i in range(len(functions)):
        dp.register_message_handler(functions[i], commands=[words[i]])

def on_text(dict):
    functions = list(dict.values())
    words = list(dict.keys())
    for i in range(len(functions)):
        dp.register_message_handler(functions[i], text=[words[i]])

        
    
# def words(dict):
#     functions = list(dict.values())
#     words = list(dict.keys())
#     for i in range(len(functions)):
#         @dp.message_handler(text=[words[i]])
#         async def process_new_command(message: types.Message):
#             await functions[i](message)
            

on_command({
    'start': start.start
})

# commands({
#     'start': start,
#     'menu': menu,
    
# })

# words({
#     'Меню 🍣': menu,
#     'Открыть корзину': basket_open,
    
# })

# category()

# basket_add()

if __name__ == '__main__':
    executor.start_polling(dp)
