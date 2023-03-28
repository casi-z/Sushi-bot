class UserOrder:
    price = 0
    basket_string = ""
    delivery_price = 0
    def __init__(self, delivery, address, phone, basket):
        self.delivery = delivery
        self.address = address
        self.phone = phone
        self.basket = basket
        
    def clear_basket(self, product):
        if product != 'all':
            del self.basket[self.basket.index(product)]

        else:
            self.basket = []

    def calc_total_price(self):
        UserOrder.price = 0
        if self.basket == []:
            return 0
        else:
            for product in self.basket:
                UserOrder.price += (product["price"] * product["count"]) + self.delivery_price

            return UserOrder.price

    def show_basket(self):
        UserOrder.basket_string = ''
        if self.basket != []:
            for product in self.basket:
                UserOrder.basket_string += (
                    f"-- {product['name']}: {product['price']}₽ x{product['count']}\n"
                )

            return f" {UserOrder.basket_string} \n\n Всего: {UserOrder.calc_total_price(self)}₽"
        else:
            return "Ваша корзина пуста"
        
    def add_product(self, product, count):
        product['count'] = count or 1

        if product in self.basket:
            self.basket[self.basket.index(product)]['count'] += 1
        else:
            self.basket.append(product)
       
    def set_delivery(self, item):
        self.delivery = item

    def set_delivery_price(self, item):
        self.delivery_price = item
        
order = UserOrder(True, "", "", [])

def text(array):
    return '\n'.join(array)


def stringMap(first, array, last):

    str = ''
    for elem in array:
        str += (first + elem + last)

    return str