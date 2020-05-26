""" Додати товари з наявними параметрами
на склад і вказати їх кількість"""


class Product:
    type_prod = ""
    name_prod = ""
    price = 0.0

    def __init__(self, type_prod, name_prod, price):
        self.type_prod = type_prod
        self.name_prod = name_prod
        self.price = price

    def __str__(self):
        return f"{self.name_prod} = {self.price}"

    def __repr__(self):
        return f"{self.name_prod} = {self.price}"



class ProductStore:
    amount = 0
    profit = 0
    warehouse = []

    def add(self, produkt, amount):
        t = {}
        t["produkt"] = produkt
        t["amount"] = amount
        produkt.price += 1.3
        self.warehouse.append(t)



first_product = Product("fruit", "apple", 10)

store = ProductStore()
store.add(first_product, 300)