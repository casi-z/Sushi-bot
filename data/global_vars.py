selected_category = "Соусы"
order = {
    "delivery": None,
    "address": "",
    "phone": "",
    "basket": [],
}


class UserOrder:
    price = 0
    busket_string = ""

    def __init__(self, delivery, address, phone, basket):
        self.delivery = delivery
        self.address = address
        self.phone = phone
        self.basket = basket

    def clear_busket(self, product):
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

    def show_busket(self):
        if self.busket != []:
            for product in self.basket:
                UserOrder.busket_string += (
                    f"-- {product.name}: {product.price} x{product.count}\n"
                )

            return f"<b> {UserOrder.busket_string} \n\n Всего: <i>{UserOrder.calc_total_price()}</i>"
        else:
            return "Ваша корзина пуста"
    def add_product(self, product, count):
        product['count'] = count or 1
        self.busket.append(product)


order = UserOrder(False, "", "", [])
