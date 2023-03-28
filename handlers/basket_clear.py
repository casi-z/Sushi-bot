from data.global_vars import order
from data.data import menu
async def basket_clear(message):
    order.clear_basket('all')
    await message.answer('Ваша корзина очищена')

async def basket_remove(message):
    with open('data/category.txt', 'r', encoding='utf-8') as category:

        selected_category = category.read()
        product_index = (int(message.text[8:]) - 1)
        delete_target = menu[selected_category][product_index]
        delete_target_name = delete_target['name']

        order.clear_basket(delete_target)
        await message.answer(f'<b><i>{delete_target_name}</i></b> удалён из корзины')
