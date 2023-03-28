from bot import dp, listen
from aiogram import types, executor
from handlers import *
import data.data as data
from utils import calc_coords
from data.global_vars import order
import time


def category_get():
    with open('data/category.txt', 'r', encoding='utf-8') as category:
        return str(category.read())


# Функция listen заменяет тонны хендлеров
# Вся логика раскидана по файлам
listen([
    [['/start', '/bar'], start.start],
    [['/menu', 'Меню 🍣', 'Назад в меню'], menu.menu],
    [data.categories, category.category],
    [
        [f'/{index + 1}' for index in range(1000)], 
        basket_add.basket_add
    ],
    [['Открыть корзину'], basket_show.basket_show],
    [['Очистить корзину'], basket_clear.basket_clear],
    [
        [f'/delete_{index + 1}' for index in range(1000)], 
        basket_clear.basket_remove
    ],
    [['Оформить заказ'], make_order.make_order],
    [['Отменить заказ'], make_order.make_order],
    [['-location'], read_geolocation.read_geolocation],
    [['Перейти к оплате'], pay.set_pay_method],
    [['Использовать промокод'], pay.set_promocode],
    [['Оплата картой', 'Оплатить картой'], pay.main],
])



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
