import sqlite3 as sql

db = sql.connect('data/database.db')
cursor = db.cursor()

def database_get_categories():

    categories_table = cursor.execute("""SELECT * FROM categories""").fetchall()
    categories_list = []
    
    for item in categories_table:
        categories_list.append(item[1])

    return categories_list

def database_get_menu():
    
    menu = {}

    
    for item in database_get_categories():
        menu_table = cursor.execute(f"""SELECT * FROM {item}""").fetchall()
        menu_items = []
        for string in menu_table:
            menu_items.append({'name': string[0], 'price': string[1], 'description': string[2]})
        menu[item.replace('_', ' ')] = menu_items

    return menu

def database_get_restaurants():

    restaurants_table = cursor.execute("""SELECT * FROM restaurants""").fetchall()
    restaurants = []
    
    for item in restaurants_table:
        restaurant = {
            'address': item[0], 
            'geolocation': item[1]
        },
        restaurants.append(restaurant[0])

    return restaurants

menu = database_get_menu()

categories = list(menu.keys())

restaurants = database_get_restaurants()
print(restaurants)




# menu = {
#     "Соусы": [
#         {"name": "Имбирь", "price": 55, "description": "30г"},
#         {"name": "Соевый соус", "price": 55, "description": "40г"},
#         {"name": "Кетчуп", "price": 35, "description": "30г"},
#         {"name": "Ореховый соус", "price": 55, "description": "30г"},
#     ],
#     "Классические": [
#         {
#             "name": "Суши с копчёным лососем",
#             "price": 85,
#             "description": "35г  Рис, копченый лосось  130 ккал, жиры - 4 г, белки - 10 г., углеводы - 14 г.",
#         },
#         {
#             "name": "Суши с тунцом",
#             "price": 85,
#             "description": "35г  Рис, тунец  110 ккал, жиры - 1 г, белки - 11 г., углеводы - 14 г.",
#         },
#         {
#             "name": "Суши с угрём",
#             "price": 85,
#             "description": "37г  Рис, угорь  220 ккал, жиры - 13 г, белки - 10 г., углеводы - 15 г.",
#         },
#     ],
#     "Мини роллы": [
#         {
#             "name": "Мини с лососем",
#             "price": 235,
#             "description": "100г  Лосось  120 ккал, жиры - 2 г, белки - 8 г., углеводы - 18 г.",
#         },
#         {
#             "name": "Мини с огурцом",
#             "price": 125,
#             "description": "93г  Огурец, кунжут  110 ккал, жиры - 2 г, белки - 3 г., углеводы - 20 г.",
#         },
#         {
#             "name": "Мини с тунцом",
#             "price": 225,
#             "description": "95г  Тунец  110 ккал, жиры - 0,5 г, белки - 7,5 г, углеводы - 19 г.",
#         },
#         {
#             "name": "Мини с угрём",
#             "price": 255,
#             "description": "98г  Угорь, соус Унаги, кунжут  170 ккал, жиры - 7 г, белки - 6 г., углеводы - 20 г.",
#         },
#     ],
#     "Острые": [
#         {
#             "name": "Суши с креветкой",
#             "price": 95,
#             "description": '37г  Креветки, соус "Спайси"  180 ккал, жиры - 10 г, белки - 8 г., углеводы - 14 г.',
#         },
#         {
#             "name": "Суши с лососем",
#             "price": 95,
#             "description": '37г  Лосось, соус "Спайси"  190 ккал, жиры - 11 г, белки - 8,5 г., углеводы - 14 г.',
#         },
#         {
#             "name": "Суши с мидиями",
#             "price": 95,
#             "description": '37г  Мидии, соус "Спайси"  170 ккал, жиры - 10 г, белки - 5 г., углеводы - 14 г.',
#         },
#         {
#             "name": "Суши с тунцом",
#             "price": 95,
#             "description": '37г  Тунец, соус "Спайси"  180 ккал, жиры - 9,5 г, белки - 9,5 г., углеводы - 14 г.',
#         },
#         {
#             "name": "Суши с угрём",
#             "price": 95,
#             "description": '37г  Угорь, соус "Спайси"  250 ккал, жиры - 18 г, белки - 8 г., углеводы - 14 г.',
#         },
#     ],
#     "Роллы": [
#         {
#             "name": "Эби панко",
#             "price": 335,
#             "description": "190г  Сыр, креветки, огурец, ореховый соус, унаги соус, сухари, кунжут.",
#         },
#         {
#             "name": "Филадельфия",
#             "price": 335,
#             "description": "200г  Лосось, сливочный сыр, огурец.  130 ккал, жиры - 5 г, белки - 6 г., углеводы - 15 г.",
#         },
#         {
#             "name": "Калифорния",
#             "price": 285,
#             "description": "175 г  Краб, икра масаго, сливочный сыр, огурец, кунжут  160 ккал, жиры - 4 г, белки - 8 г., углеводы - 18 г.",
#         },
#         {
#             "name": "Снек ролл",
#             "price": 255,
#             "description": "218г  Курица жареная, огурец, соус сырный, крошка чипсов  170 ккал, жиры - 7 г, белки - 6 г., углеводы - 19 г.",
#         },
#         {
#             "name": "Токио",
#             "price": 355,
#             "description": "210г  Тигровая креветка, сыр сливочный, огурец, угорь.",
#         },
#     ],
#     "Запечённые роллы": [
#         {
#             "name": "Эби темпура",
#             "price": 375,
#             "description": "200г  Креветка, лосось, сливочный сыр, соус унаги.",
#         },
#         {
#             "name": "Калифорния темпура",
#             "price": 295,
#             "description": "220г  Краб, огурец, сливочный сыр, массаго, кляр.",
#         },
#         {
#             "name": "Кидо",
#             "price": 345,
#             "description": "220г  Рис, спайс соус, гребешок, креветка, кляр.",
#         },
#         {
#             "name": "Сяке фурай",
#             "price": 345,
#             "description": "230г  Лосось жареный, кляр, сливочный сыр, икра масаго, соус спайси.",
#         },
#         {
#             "name": "Темпура креветка",
#             "price": 345,
#             "description": "200г  Креветка, лосось, огурец, сливочный сыр, темпура  230,04 ккал, жиры - 6,92 г, белки - 7,54 г., углеводы - 34,39 г.",
#         },
#         {
#             "name": "Темпура лосось",
#             "price": 345,
#             "description": "200г  Лосось, огурец, сливочный сыр, икра масаго, темпура  232,1 ккал, жиры - 7,1 г, белки - 7,37 г., углеводы - 34,74 г.",
#         },
#         {
#             "name": "Темпура угорь",
#             "price": 345,
#             "description": "200г  Угорь, огурец, сливочный сыр, темпура  242,7 ккал, жиры - 8,15 г, белки - 6,51 г., углеводы - 35,83 г.",
#         },
#         {
#             "name": "Яки-кани",
#             "price": 285,
#             "description": "195г  Краб, розовый соус, капуста китайская.",
#         },
#     ],
# }