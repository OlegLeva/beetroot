class Car(object):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_alarm_on = False

    def alarm_on(self):
        self.is_alarm_on = True

    def alarm_off(self):
        self.is_alarm_on = False



mazda = Car("Mazda", "3", 2016)
rav4 = Car("Toyota", "Rav4", 2015)

print(mazda.year, rav4.year)

mazda.alarm_on()

print(mazda.is_alarm_on, rav4.is_alarm_on)

rav4.alarm_on()
mazda.alarm_off()

print(mazda.is_alarm_on, rav4.is_alarm_on)