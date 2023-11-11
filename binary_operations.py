from twos_comp import * #list to string in twos_comp
from hex_bin_den import *
from floating_point_binary import *

def add_binary(num1, num2, subtract=False):
    index = 0
    carry = 0
    final_number = ""
    
    if "." in list(num1) or "." in list(num2):
        num1,num2 = allign_floating_points(list(num1),list(num2))
        num1,num2 = check_length_point(num1,num2)
    else:
        num1,num2 = check_length(num1,num2,subtract)
    print("%s add %s"%(num1,num2))
    while index != len(num1):
        num_index = len(num1) - index - 1
        carry,bit = adding_bits(num1,num2,num_index,carry)
        if bit != None:
            final_number = str(bit) + final_number
        index += 1

    if carry != 0 and not subtract:
        final_number = str(carry) + final_number
    return final_number

def check_length(num1,num2,subtract):
    if len(num1) == len(num2):
        return num1,num2
    else:
        if len(num1) < len(num2):
            while len(num1) != len(num2):
                num1 = "0" + num1
        elif len(num2) < len(num1):
            if subtract:
                while len(num2) != len(num1):
                    num2 = "1" + num2
            else:
                while len(num2) != len(num1):
                    num2 = "0" + num2
        
    return num1,num2
                
    
        

def adding_bits(num1,num2,index,carry):
    try:
        bit1 = int(num1[index])
        bit2 = int(num2[index])
    except: #floating point
        return carry,"." 
    
    number = denary_to_binary(bit1 + bit2 + int(carry))

    if len(number) == 2:
        carry,bit = number
    else:
        bit = number
        carry = "0"

    return carry,bit

def subtract_binary(num1,num2):
    num2 = int(binary_to_denary(int(num2)))
    num2 = str(twos_complement(-num2))
    num1 = str(twos_complement(binary_to_denary(int(num1))))
    return add_binary(num1,num2,True)

if __name__ == "__main__":
    #print(subtract_binary("011101101","010011100"))
    
    #print(add_binary("1111","0101"))
    print("\n")
    print(subtract_binary("01011011","01011110"))

    #print(add_binary("1010","1"))

    
