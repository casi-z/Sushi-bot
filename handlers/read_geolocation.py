from utils import find_nearest_restaurant
from utils import text
from bot import bot


async def read_geolocation(message):
    lat = message.location.latitude
    lon = message.location.longitude
    nearest_restaurant = find_nearest_restaurant((lat, lon))

    nearest_restaurant_img_name = nearest_restaurant.replace(' ', '-')
    # print(nearest_restaurant_img_name)
    with open(f'img/restourants/{nearest_restaurant_img_name}.jpg' , 'rb') as img: 
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
        )
    await message.answer('jj')