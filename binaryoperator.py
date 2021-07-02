a = 0
b = 0

def dectobin(dec):
    if dec >= 128:
        bin = "1"
        dec -= 128
    else:
        bin = "0"
    if dec >= 64:
        bin += "1"
        dec -= 64
    else:
        bin += "0"
    if dec >= 32:
        bin += "1"
        dec -= 32
    else:
        bin += "0"
    if dec >= 16:
        bin += "1"
        dec -= 16
    else:
        bin += "0"
    if dec >= 8:
        bin += "1"
        dec -= 8
    else:
        bin += "0"
    if dec >= 4:
        bin += "1"
        dec -= 4
    else:
        bin += "0"
    if dec >= 2:
        bin += "1"
        dec -= 2
    else:
        bin += "0"
    if dec >= 1:
        bin += "1"
        dec -= 1
    else:
        bin += "0"
    return bin

def invoer():
    try:
        number = int(input("Please enter a number from 0 to 255: "))
        if number < 0:
            number = int(input("Please enter a number from 0 to 255: "))
        if number > 255:
            number = int(input("Please enter a number from 0 to 255: "))
    except ValueError:
        print("Numbers only!")
    return number

print("Welcome to my decimal to binary calculator with bitwise operators!\n")
print("Please enter your first number")
a = invoer()
yorn = input("Would you like to see your number in binary? (y or n) ")
while yorn not in ["y", "n"]:
    yorn = input("\nWould you like to see your number in binary? (y or n) ")
if yorn == "y":
    dec = a
    x = dectobin(dec)
    print()
    print(x)

print("\nPlease enter your second number")
b = invoer()
yorn = input("\nWould you like to see your number in binary? (y or n) ")
while yorn not in ["y", "n"]:
    yorn = input("Would you like to see your number in binary? (y or n) ")
if yorn == "y":
    dec = b
    y = dectobin(dec)
    print()
    print(y)

print("\nWhich bit operator do you want me to perform?")
op = input("Enter 1 for AND, enter 2 for OR, enter 3 for XOR: ")
while op not in ["1", "2", "3"]:
    op = input("Enter 1 for AND, enter 2 for OR, enter 3 for XOR: ")
if op == "1":
    result = a & b
elif op == "2":
    result = a | b
elif op == "3":
    result = a ^ b

dec = result
z = dectobin(dec)
print("The result is: "+z)
yorn = input("\nWould you like to see the result in decimal? (y or n) ")
while yorn not in ["y", "n"]:
    yorn = input("Would you like to see the result in decimal? (y or n) ")
if yorn == "y":
    print()
    print(result,"\n")
