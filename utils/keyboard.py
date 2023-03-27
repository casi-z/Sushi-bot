from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import data.data as data

menu_button = KeyboardButton(text='Меню 🍣')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_kb.add(menu_button)

category_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

for i in data.categories:
    category_button = KeyboardButton(text=i)
    category_kb.add(category_button)

basket_add_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
basket_show_button = KeyboardButton(text='Открыть корзину')
basket_add_kb.add(basket_show_button)

basket_clear_button = KeyboardButton(text='Очистить корзину')
basket_add_kb.add(basket_clear_button)
basket_back_button = KeyboardButton(text='Назад в меню')
basket_add_kb.add(basket_back_button)

order_button = InlineKeyboardButton('Оформить заказ')

order_kb = InlineKeyboardMarkup()
order_kb.add(order_button)