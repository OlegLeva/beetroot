
def name_up(value):
    name = value
    def name_in():
        print(f"Hello {name} ")

    return name_in

#c = name_up("Kolya")
#print(c())
print(name_up("Olya")())