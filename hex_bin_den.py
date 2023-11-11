def denary_to_binary(number):
    number = int(number)
    binary_number = ""

    #check for 0
    if number == 0:
        binary_number = "0"
    
    while number != 0:
        remainder = number % 2
        number = number / 2
        number = int(number)
        binary_number = str(remainder) + binary_number

    #binary_number = check_length(binary_number)
    #^doesn't work with negative numbers and addition
        
    #print("binary number:",binary_number)

    return binary_number
    

def check_length(binary_number):
    zeros = ""
    value = 4
    while len(binary_number) > value:
        value = value * 2
        if len(binary_number) == value:
            return binary_number
        
    for x in range(len(binary_number), value):
        zeros += "0"
    
    binary_number = zeros + binary_number
    return binary_number

def binary_to_denary(number):
    #changed to 2's comp
    number = str(number)
    denary_number = 0
    bit_no = 1
    count = 1
    for x in reversed(number):
        x = int(x)
        if bit_no == len(number):
            count = -count
        denary_number += x * count
        count = count * 2
        bit_no += 1
    return denary_number

def denary_to_hex(number):
    number = int(number)
    hexedecimal_number = ""
    while number != 0:
        remainder = number % 16
        if remainder >= 10:
            remainder = number_to_letter(remainder)
        number = number // 16
        hexedecimal_number = str(remainder) + hexedecimal_number

    return hexedecimal_number

def number_to_letter(number):
    if number == 10:
        x = "A"
    elif number == 11:
        x = "B"
    elif number == 12:
        x = "C"
    elif number == 13:
        x = "D"
    elif number == 14:
        x = "E"
    elif number == 15:
        x = "F"
    else:
        x = ""
    return x

def hex_to_denary(number):
    number = str(number)
    denary_number = 0
    count = 1
    for x in reversed(number):
        try:
            x = int(x)
        except:
            x = letter_to_number(x)
        denary_number += x * count
        count = count * 16
    return denary_number

def letter_to_number(letter):
    letter = letter.upper()
    if letter == "A":
        x = 10
    elif letter == "B":
        x = 11
    elif letter == "C":
        x = 12
    elif letter == "D":
        x = 13
    elif letter == "E":
        x = 14
    elif letter == "F":
        x = 15
    else:
        x = 0
    return x

def base_to_number(number, base):
    base = int(base)
    number = str(number)
    denary_number = 0
    count = 1
    for x in reversed(number):
        x = int(x)
        denary_number += x * count
        count = count * base
    return denary_number
    

def menu():
    cont = True
    menu = "\n1.Denary number to binary \n2.Binary number to denary \n3.Denary number to hex \n4.Hexidecimal to denary number \n5.base to denary(doesn't work) \n9.quit \n:"
    while cont == True:
        answer = input(menu)
        if answer == "1":
            number = input("enter a number: ")
            answer2 = denary_to_binary(number)
        elif answer == "2":
            number = input("enter a number: ")
            answer2 = binary_to_denary(number)
        elif answer == "3":
            number = input("enter a number: ")
            answer2 = denary_to_hex(number) + "," + denary_to_binary(number)
        elif answer == "4":
            number = input("enter a number: ")
            answer2 = hex_to_denary(number) + "," + denary_to_binary(number)

        elif answer == "5":
            number = input("enter a number: ")
            base = input("enter the base: ")
            answer2 = base_to_number(number, base)
            
        elif answer == "9":
            cont = False
            exit()
        print(answer2)

if __name__ == "__main__":
    menu()
        

