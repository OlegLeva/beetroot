class Product:
    type_prod = ""
    name_prod = ""
    price = 0

    def __init__(self, type_prod, name_prod, price):
        if type(type_prod) != str:
            raise ValueError("Type should be a string")
        else:
            self.type_prod = type_prod
        if type(name_prod) != str:
            raise ValueError("Type should be a string")
        else:
            self.name_prod = name_prod
        if type(price) != int and type(price) != float:
            raise ValueError("Price should be a number")
        else:
            self.price = price

    def __str__(self):
        return f"{self.type_prod},  {self.name_prod} = {self.price}"

    def __repr__(self):
        return f"{self.type_prod}, {self.name_prod} = {self.price}"


class ProductStore:
    amount = 0
    profit = 0
    warehouse = []

    def add(self, product, amount):
        t = {}
        t["product"] = product
        t["amount"] = amount
        product.price *= 1.3
        self.warehouse.append(t)

    def set_discount(self, product_identifier, percent):
        if type(percent) != int and type(percent) != float:
            raise ValueError("Percent should be a number")
        for i in self.warehouse:
            my_product = i["product"]
            if my_product.type_prod == product_identifier or my_product.name_prod == product_identifier:
                my_product.price = my_product.price * (1 - (percent / 100))


    def sell_product(self, product, amount):
        for i in self.warehouse:
            my_product = i["product"]
            if my_product.name_prod == product.name_prod:
                try:
                    if amount >= i["amount"]:
                        raise Exception("We don't have such amount of product")
                    else:
                        i["amount"] -= amount
                        self.profit = amount * my_product.price
                except Exception as e:
                    print(e)

    def get_income(self):
        return print(f"{self.profit}")

    def get_all_product(self):
        return print(self.warehouse)

    def product_info(self, product):
        for i in self.warehouse:
            my_product = i["product"]
            if my_product.name_prod == product.name_prod:
                my_tuple = product.name_prod, i["amount"]
                return print(my_tuple)


try:
    p = Product("Sport", "Football T-Shirt", 100)
    p2 = Product("Food", "Ramen", 20)
    s = ProductStore()
    s.add(p2, 20)
    s.sell_product(p2, 5)
    s.sell_product(p2, 1)
    s.set_discount("Ramen", 20)
    s.get_all_product()
    s.get_income()
    s.product_info(p2)

except ValueError as e:
    print(e)

