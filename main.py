from bot import dp, listen
from aiogram import types, executor
from handlers import *
import data.data as data
import time

def category_get():
    with open('data/category.txt', 'r', encoding='utf-8') as category:
        return str(category.read())

listen([
    [['/start', '/bar'], start.start],
    [['/menu', 'Меню 🍣', 'Назад в меню'], menu.menu],
    [data.categories, category.category],
    [
        [f'/{index + 1}' for index, item in enumerate(data.menu[category_get()])], 
        basket_add.basket_add
    ],
    [['Открыть корзину'], basket_show.basket_show],
])



if __name__ == '__main__':
    executor.start_polling(dp)
