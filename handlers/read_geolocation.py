from utils import find_nearest_restaurant, way_to_restaurant, get_delivery_time
from utils import text
from bot import bot
from data.global_vars import order
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup().add(
    KeyboardButton('Перейти к оплате')
    

)



def calc_delivery_price(way):
    if way <= 15:
        return 0
    elif way > 15:
        return (way - 15) * 20
    elif way > 30:
        return None
    
def get_message_text(way):
    result = calc_delivery_price(way)
    if result == None:
        return 'Наш ресторан не доставляет в ваши края 😢'
    else:
        order.set_delivery_price(result)
        return text(
                    [
                        f"Заказ будет доставлен к вашей двери через {get_delivery_time(way)} минут",
                        "",
                        f'Cтоимость доставки составит: {result} рублей',
                    ]
                )
        

async def read_geolocation(message):
    lat = message.location.latitude
    lon = message.location.longitude
    nearest_restaurant = find_nearest_restaurant((lat, lon))

    nearest_restaurant_img_name = nearest_restaurant.replace(" ", "-")

    if order.delivery == True:
        with open('img/courier.jpg', 'rb') as img: 
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption=get_message_text(way_to_restaurant((lat, lon))),
                reply_markup=kb
            )

    else:
        with open(f"img/restourants/{nearest_restaurant_img_name}.jpg", "rb") as img:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=img,
                caption=text(
                    [
                        "Заказ будет готов нашем ближайшем ресторане:",
                        "",
                        nearest_restaurant,
                    ]
                ),
                reply_markup=kb
            )
    
