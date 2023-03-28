from aiogram.types import *
from bot import dp
rest_button = KeyboardButton('Заказать в ресторан')
home_button = KeyboardButton('Заказать на дом')
deny_order_button = KeyboardButton('Отменить заказ')

make_order_kb = ReplyKeyboardMarkup()
make_order_kb.add(rest_button)
make_order_kb.add(home_button)
make_order_kb.add(deny_order_button)

get_geolocation_kb = ReplyKeyboardMarkup()
send_geolocation_button = KeyboardButton('Отправить местоположение', request_location=True)
get_geolocation_kb.add(send_geolocation_button)
get_geolocation_kb.add(deny_order_button)


async def make_order(message):
    await message.answer(
        text='Вы хотите покушать в ресторане или у себя дома?',
        reply_markup = make_order_kb,
    )
    @dp.message_handler(text=['Заказать в ресторан', 'Заказать на дом'])
    async def get_geolocation(message):
        
        await message.answer(
            text='Отправьте своё местоположение для заказа!',
            reply_markup = get_geolocation_kb,
        )
    
    