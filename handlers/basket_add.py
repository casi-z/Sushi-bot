from data.global_vars import order
from aiogram.types import *
from bot import dp, bot
from data.data import menu
from utils.keyboard import basket_add_kb
from utils import text

        
async def basket_add(message: Message):

    with open('data/category.txt', 'r', encoding='utf-8') as category:

        selected_category = category.read()
        selected_products = menu[selected_category]
        order.add_product(selected_products[int(message.text[1:]) - 1], 1)
        
        await message.answer(
            text=text([
                'Товар добавлен в корзину',
                f'Удалить: /delete_{message.text[1:]}'
            ]),
            reply_markup=basket_add_kb
        )