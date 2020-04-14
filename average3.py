#Continuously updates the average as new numbers are entered.

print ("Welcome to the Average Calculator, please insert a number")
currentaverage = 0
numofnums = 0
while True:
    newnumber = int(input("New number "))
    numofnums = numofnums + 1
    currentaverage = (round((((currentaverage * (numofnums - 1)) + newnumber) / numofnums), 3))
    print ("The current average is " + str((round(currentaverage, 3))))