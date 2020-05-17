
CHANNELS = ["BBC", "Discovery", "TV1000VIP", "TV1000"]
i = 0

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


n = input("Enter command or channel number: ")

 #       def turn_channel(self):
 #           i = int(n) - 1
 #           return CHANNELS[i]

  #  def next_channel(self):

controller = TVController(*CHANNELS)

if n == "first":
    print(controller.first_chanel())
if n == "last":
    print(controller.last_channel())
#if n.isdigit():
