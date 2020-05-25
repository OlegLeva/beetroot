class Product:
    type_prod = ""
    name_prod = ""
    price = 0.0
    amount = 0
    name_price = {}


    def __init__(self, type_prod, name_prod, price):
        self.type_prod = type_prod
        self.name_prod = name_prod
        self.price = price
        self.name_price = {}


class ProductStore(Product):
    pass

    def add(self, name, price, name_prod=None):
        self.name_price[name_prod] = price*1.3
