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

    def add(self, price, name_prod):
        self.name_price[name_prod] = price * 1.3



avocado = ProductStore("fruit", 25.0, "Avocado")
avocado.add(25, "Avocado")


