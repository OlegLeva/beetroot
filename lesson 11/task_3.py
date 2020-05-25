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

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)


"""
class ProductStore(Product):
    pass

    def add(self, name_prod, price):
        self.name_price[name_prod] = price * 1.3
"""



"""
s = ProductStore()

s.add(p, 10)

s.add(p2, 300)"""





