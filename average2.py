sum = 0.0

print("This program will take several numbers, then average them.")
count = int(input("How many numbers would you like to sum:  "))
current_count = 0

while current_count < count:
    print("Number", current_count)
    number = float(input("Enter a number:  "))
    sum = sum + number
    current_count += 1

print("The average was:", sum / count)