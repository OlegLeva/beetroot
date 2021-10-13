class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000VIP", "TV1000"]
    number = 1
    # i = ""

    def get_current(self):
        return self.CHANNELS[self.number - 1]

    def first_chanel(self):
        self.number = 1
        return self.get_current()

    def last_channel(self):
        self.number = len(self.CHANNELS)
        return self.get_current()

    def turn_channel(self):
        self.number = int(n)
        return self.get_current()

    def next_channel(self):
        if self.number == len(self.CHANNELS):
            self.number = 1
            return self.get_current()
        else:
            self.number += 1
            return self.get_current()

    def previous_channel(self):
        if self.number == 1:
            self.number = len(self.CHANNELS)
            return self.get_current()
        else:
            self.number -= 1
            return self.get_current()

    def current_channel(self):
        return self.get_current()

    def is_exist(self, name):
        if name in ["BBC", "Discovery", "TV1000VIP", "TV1000"]:
            return "Yes"
        if name in "1234":
            return "Yes"
        else:
            return "No"


controller = TVController()

while True:

    n = input("Enter command or channel number: ")

    if n == "f":
        print(controller.first_chanel())
    if n == "l":
        print(controller.last_channel())
    if n in "1234":
        print(controller.turn_channel())
    if n == "nx":
        print(controller.next_channel())
    if n == "b":
        print(controller.previous_channel())
    if n == "c":
        print(controller.current_channel())
    if n == "name":
        name = input('Введите имя или номер канала: ')
        print(controller.is_exist(name))

    if n == "x":
        break
