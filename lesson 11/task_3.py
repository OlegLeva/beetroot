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



class ProductStore:
    pass

    def add(self, name_instance, amout):
        self.name_instance = name_instance
        self.amout = amout
        self.produkt_list = produkt_list #єксперимент
        dict_amout = {self.name_instance: self.amout}
        return produkt_list.append(dict_amout)

    def __str__(self):
        return (f'{self.produkt_list}')

    def __repr__(self):
        return (f'{self.produkt_list}')


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Apple', 20)
produkt_list = []

s = ProductStore()
s.add(p2, 300)
print(f'{produkt_list}')
print(str(produkt_list))