
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import utils.keyboard as keyboard
import data.data as data

TOKEN = "6041837935:AAEK1PEme5VxQRwBsEQg8hlAohzaHcJnvoQ"
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

photo = types.InputFile("./img/fon.jpg")
menuImg = types.InputFile("./img/menu.jpg")

def commands(dict):
    functions = list(dict.values())
    words = list(dict.keys())
    for i in range(len(functions)):
        @dp.message_handler(commands=[words[i]])
        async def process_new_command(message: types.Message):
            await functions[i](message)
    
def words(dict):
    functions = list(dict.values())
    words = list(dict.keys())
    for i in range(len(functions)):
        @dp.message_handler(text=[words[i]])
        async def process_new_command(message: types.Message):
            await functions[i](message)