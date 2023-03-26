from data.global_vars import *
from aiogram.types import *
from data.global_vars import order
def main(message):
    return message.answer(text=order.show_basket())
