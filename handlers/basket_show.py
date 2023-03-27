from data.global_vars import *
from aiogram.types import *
from data.global_vars import order
from utils import order_kb
async def basket_show(message):
    await message.answer(
        text=order.show_basket(),
        inline_markup = order_kb
    )
