from scripts.bot import dp
from data.data import menu
from data.global_vars import *
from aiogram import types
from utils.keyboard import product_kb

def main():
    for i in menu[selected_category]:
        
        @dp.message_handler(commands=(str(menu[selected_category].index(i) + 1)))
        async def process_start_command(message: types.Message):
            order.add_product(i.copy())
            await message.answer(
                text='Товар добавлен в корзину',
                reply_markup=product_kb
            )