from hex_bin_den import *
from twos_comp import *
from floating_point_binary import *

def list_to_string(char_list):
    string = ""
    for letter in char_list:
        string = string + letter
    return string


def normalise_number(binary_number):
    binary_number = list(binary_number)
    for item in binary_number:
        if item == "0" and binary_number[binary_number.index(item)+1] == "0":
            binary_number.remove(item)
        if item == ".":
            point_start = binary_number.index(".") 
            binary_number.remove(".")
    try:
        exponent = denary_to_binary(point_start - 1)
    except: #there was no floating point in the number
        exponent = denary_to_binary(len(binary_number) - 1)
    exponent = check_length(exponent)

    if "." in binary_number:
        binary_number.remove(".")
        
    binary_number = list_to_string(binary_number)
    return binary_number,exponent

def expand_number(mantissa,exponent):
    mantissa = list(mantissa)
    exponent = int(binary_to_denary(exponent))
    if "." in mantissa:
        mantissa.remove(".")
    mantissa.insert(exponent+1,".")
    #print("point added at:",exponent+1)

    new_number = list_to_string(mantissa)
    return new_number

if __name__ == "__main__":
    #print(normalise_number("00000101.10"))
    print(expand_number("010110","0011"))
    print(pointbinary_to_denary(expand_number("010110","0011")))
        
