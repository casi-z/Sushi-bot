from aiogram.types import *
from utils import text
from bot import dp
from data.global_vars import order
set_pay_method_kb = ReplyKeyboardMarkup().add(
                            KeyboardButton('Использовать промокод'),
                            KeyboardButton('Оплатить картой')
                        )

rm = ReplyKeyboardRemove()
do_promocode_active = True
async def set_pay_method(message):
    await message.answer(
        text= text([
            'Стоимость вашего заказа составит',
            f'{order.calc_total_price()} P'
        ]),
        reply_markup=set_pay_method_kb
    )
    await message.answer('Хотите использовать промокод для получения скидки?')

read_promocode_kb = ReplyKeyboardMarkup().add(
    KeyboardButton('Оплатить картой')
)
async def set_promocode(message):
    await message.answer(text='Введите свой промокод', reply_markup=rm)

    @dp.message_handler()

    async def read_promocode(message):
        global do_promocode_active
        if do_promocode_active:
            do_promocode_active = False
            promocodes = ['promo']
            if message.text in promocodes:
                await message.answer(
                    text=text([
                        'Вы получили скидку в 10%',
                        'Стоимость вашего заказа составит',
                        f'{(order.calc_total_price() - (order.calc_total_price() * 30 / 100))} P'
                    ]),
                    reply_markup=read_promocode_kb
                )
            else: 
                await message.reply(text='Такого промокода не существует', reply_markup=read_promocode_kb)
async def main(message):
    await message.reply('Оплата картой', reply_markup=rm)