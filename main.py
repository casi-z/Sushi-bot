from scripts.bot import *
from scripts.start import main as start
from scripts.menu import main as menu
from scripts.category import main as category
from scripts.basket_add import main as basket_add
from scripts.bot import commands, words
from data.global_vars import UserOrder
from data.data import menu

def text(array):
    return '\n'.join(array)


def calcPrice(list):
    price = 0
    for element in list:
        price += element['price']
    return str(price)



commands({
    'start': start,
    'menu': menu,
    
})

words({
    'Меню 🍣': menu,

})

category()

def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str



# for i in data.menu[selectedCategory]:
    
#     @dp.message_handler(commands=(str(data.menu[selectedCategory].index(i) + 1)))
#     async def process_start_command(message: types.Message):
#         global userOrder
#         userOrder['basket'].append(i)
#         await message.answer(
#             text='Товар добавлен в корзину',
#             reply_markup=keyboard.product_kb
#         )


# def showBasket():
#     global userOrder
#     string = ''
#     for i in userOrder['basket']:
#         string += '\n' + i['name'] + ':' + str(i['price']) + 'x1'

#     return string

# @dp.message_handler(text='Открыть корзину')
# async def process_start_command(message: types.Message):

#     if userOrder['basket'] != []:    
#         await message.answer(
#             text=text([
#                 'Ваша корзина:',
#                 "\n" + showBasket() + '\n',
#                 'Всего: ' + calcPrice(userOrder['basket']) + '₽'

#             ])
            
#         )
#     else:
#         await message.answer(
#             text='Ваша корзина пуста'
            
#         )


# @dp.message_handler(text='Очистить корзину')
# async def process_start_command(message: types.Message):
#     userOrder['basket'] = []
#     await message.answer(
        
#         text='Ваша корзина очищена',
        
#     )

if __name__ == '__main__':
    executor.start_polling(dp)
