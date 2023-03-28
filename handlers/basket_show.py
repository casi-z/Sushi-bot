from data.global_vars import *
from aiogram.types import *
from bot import bot, dp
from data.global_vars import order



order_button = KeyboardButton('Оформить заказ')
basket_back_button = KeyboardButton(text='Назад в меню')
basket_clear_button = KeyboardButton(text='Очистить корзину')

order_kb = ReplyKeyboardMarkup()
order_kb.add(order_button)
order_kb.add(basket_back_button)
order_kb.add(basket_clear_button)

basket_kb = ReplyKeyboardMarkup()
basket_kb.add(basket_back_button)
basket_kb.add(basket_clear_button)

async def basket_show(message):
    basket = order.show_basket()

    if basket == "Ваша корзина пуста":
        await message.answer(
            text=order.show_basket(),
            reply_markup = basket_kb
        )

    else:
        await message.answer(
            text=order.show_basket(),
            reply_markup = order_kb
        )
        