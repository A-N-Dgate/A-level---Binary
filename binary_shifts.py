from hex_bin_den import *

def is_binary(number):
    number = str(number)
    if len(number) < 4:
        return False
    for digit in number:
        if digit != "1" and digit != "0":
            return False
    return True

def enter_number():
    number = input("enter a number: ")
    if is_binary(number):
        return number
    else:
        number = denary_to_binary(number)
        print("original number in binary: %s"%(number))
        return number

def list_to_string(number):
    string = ""
    for item in number:
        string = string + item
    return string
        

def right_shift(number, shift):
    number = list(number)
    for x in range(0,shift):
        number.pop(len(number) - 1)
        number.insert(0, "0")
    number = list_to_string(number)
    return number

def left_shift(number,shift):
    number = list(number)
    for x in range(0,shift):
        number.pop(0)
        number.append("0")
    number = list_to_string(number)
    return number
    
    
    
def main():
    count = True
    while count:
        answer = input("\n1.right shift \n2.left shift\n9.quit\n:")
        if answer == "1":
            number = enter_number()
            shift = int(input("enter shift value: "))
            print(right_shift(number,shift))
            print("hexadecimal:",denary_to_hex(binary_to_denary(right_shift(number,shift))))
            print("denary:",binary_to_denary(right_shift(number,shift)))
        if answer == "2":
            number = enter_number()
            shift = int(input("enter shift value: "))
            print(left_shift(number,shift))
            print("hexadecimal:",denary_to_hex(binary_to_denary(left_shift(number,shift))))
            print("denary:",binary_to_denary(left_shift(number,shift)))
        if answer == "9":
            count = False
            
if __name__ == "__main__":
    main()
        
 
    
