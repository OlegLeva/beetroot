class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000VIP", "TV1000"]
    number = 0
    i = ""

    def first_chanel(self):
        self.number = 1
        self.i = self.CHANNELS[self.number - 1]
        return self.i

    def last_channel(self):
        self.number = len(self.CHANNELS)
        self.i = self.CHANNELS[self.number - 1]
        return self.i

    def turn_channel(self):
        self.number = int(n) - 1
        self.i = self.CHANNELS[self.number]
        return self.i

    def next_channel(self):
        if self.number == len(self.CHANNELS):
            self.number = 1
            self.i = self.CHANNELS[self.number - 1]
            return self.i
        else:
            self.number += 1
            self.i = self.CHANNELS[self.number - 1]
            return self.i

    def previous_channel(self):
        if self.number == 1:
            self.number = len(self.CHANNELS)
            self.i = self.CHANNELS[self.number - 1]
            return self.i
        else:
            self.number -= 1
            self.i = self.CHANNELS[self.number - 1]
            return self.i

    def current_channel(self):
        self.i = self.CHANNELS[self.number]
        return self.i


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

    if n == "x":
        break
