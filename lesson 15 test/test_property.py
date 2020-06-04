class PhoneBook:

    def __init__(self, name, citi, phone):
        self.__name = name
        self.__citi = citi
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self,  name_value):
        if not isinstance(name_value, str):
            raise ValueError("Если вы не сын Илона Маска, то введите нормальное имя!!!")
        self.__name = name_value

    def get_citi(self):
        return self.__citi

    def set_citi(self,  citi_value):
        if not isinstance(citi_value, str):
            raise ValueError("Введите правильный город")
        self.__citi = citi_value

    def get_phone(self):
        return self.__phone

    def set_phone(self,  phone_value):
        if not isinstance(phone_value, int):
            raise ValueError("Не верный формат")
        self.__phone = phone_value

    name = property(get_name, set_name)
    citi = property(get_citi, set_citi)
    phone = property(get_phone, set_phone)


k = PhoneBook("Katya", "Kiyv", 380509000000)

k.name = "Olya"
k.citi = "New York"
k.phone = 12160000000

print(k.get_name())
print(k.get_citi())
print(k.get_phone())