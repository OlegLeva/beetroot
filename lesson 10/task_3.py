
CHANNELS = ["BBC", "Discovery", "TV1000VIP", "TV1000"]
i = 0

class TVController:
    BBC = ""
    Discovery = ""
    TV1000VIP = ""
    TV1000 = ""


    def __init__(self, BBC, Discovery, TV1000VIP, TV1000):
        self.BBC = BBC
        self.Discovery = Discovery
        self.TV1000VIP = TV1000VIP
        self.TV1000 = TV1000


    n = input("Enter command or channel number: ")
    def first_chanel(self):
        return CHANNELS[i]

    def last_channel(self):
        return CHANNELS[-1]

    def turn_channel(self):
        return CHANNELS[int(n)-1]

  #  def next_channel(self):
   #     if CHANNELS[]


controller = TVController(CHANNELS)

print(controller.turn_channel())
