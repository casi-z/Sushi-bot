from data.global_vars import order
from aiogram.types import *
from bot import dp
from data.data import menu
from utils.keyboard import basket_add_kb


def main():
    category_ = open('data/category.txt', 'r', encoding='utf-8')
    selected_category_ = category_.read()
    selected_products_ = menu[selected_category_]
    for i in selected_products_:
        
        # print(i)
        @dp.message_handler(commands=str(selected_products_.index(i) + 1))
        async def process_start_command(message: Message):

            category = open('data/category.txt', 'r', encoding='utf-8')
            selected_category = category.read()
            selected_products = menu[selected_category]

            order.add_product(selected_products[int(message.text[1:]) - 1].copy(), 1)
            
            await message.answer(
                text='Товар добавлен в корзину',
                reply_markup=basket_add_kb
            )
            print(order.show_basket())