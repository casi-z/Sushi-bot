class UserOrder:
    price = 0
    basket_string = ""

    def __init__(self, delivery, address, phone, basket):
        self.delivery = delivery
        self.address = address
        self.phone = phone
        self.basket = basket

    def clear_basket(self, product):
        if product:
            del self.basket[self.basket.index(product)]

        else:
            self.basket = []

    def calc_total_price(self):
        if self.basket == []:
            return 0
        else:
            for product in self.basket:
                UserOrder.price += product["price"] * product["count"]

            return UserOrder.price

    def show_basket(self):
        
        if self.basket != []:
            for product in self.basket:
                UserOrder.basket_string += (
                    f"-- {product['name']}: {product['price']} x{product['count']}\n"
                )

            return f" {UserOrder.basket_string} \n\n Всего: {UserOrder.calc_total_price(self)}"
        else:
            return "Ваша корзина пуста"
        
    def add_product(self, product, count):
        product['count'] = count or 1
        self.basket.append(product)

order = UserOrder(False, "", "", [])

def text(array):
    return '\n'.join(array)

def calcPrice(list):
    price = 0
    for element in list:
        price += element['price']
    return str(price)

def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str