
CHANNELS = ["BBC", "Discovery", "TV1000VIP", "TV1000"]


class TVController:
    pass


    def __init__(self, BBC, Discovery, TV1000VIP, TV1000):
        self.BBC = BBC
        self.Discovery = Discovery
        self.TV1000VIP = TV1000VIP
        self.TV1000 = TV1000


    def first_chanel(self):
        return CHANNELS[i]

    def last_channel(self):
        i = -1
        return CHANNELS[i]

    def turn_channel(self):
        i = int(n) - 1
        return CHANNELS[i]

    def next_channel(self):
        global i
        if CHANNELS[i] == CHANNELS[-1]:
            i = 0
            return CHANNELS[i]
        else:
            return CHANNELS[i+1]

    def previous_channel(self):
        global i
        if CHANNELS[i] == CHANNELS[0]:
            i = -1
            return CHANNELS[i]
        else:
            return CHANNELS[i-1]

    def current_channel(self):
        return CHANNELS[i]

i = 0
controller = TVController(*CHANNELS)

while True:

    n = input("Enter command or channel number: ")

    if n == "first":
        print(controller.first_chanel())
    if n == "last":
        print(controller.last_channel())
    if n in "1234":
        print(controller.turn_channel())
    if n == "next":
        print(controller.next_channel())
    if n == "back":
        print(controller.previous_channel())


    if n == "x":
        break
