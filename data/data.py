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

    return restaurants_table

menu = database_get_menu()

categories = list(menu.keys())

restaurants = database_get_restaurants()
