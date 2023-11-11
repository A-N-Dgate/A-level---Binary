from hex_bin_den import *
#from twos_comp import *
#^twos comp wasn't being imported correctly
import twos_comp
import binary_operations

from adders import *


def pointbinary_to_denary(binary_number):
    number = binary_number.split(".")
    #print(number)
    integer_binary = number[0]
    fraction_binary = number[1]

    integer = binary_to_denary(integer_binary)
    
    #convert the factional portion in this function
    fraction_binary = str(fraction_binary)
    fraction = 0
    count =  0.5
    for x in fraction_binary:
        x = int(x)
        fraction += x * count
        count = count / 2
        
    denary_number = int(integer) + fraction
    #print("deanry number",denary_number)

    #this function works
    return denary_number


def pointdenary_to_binary(denary_number):
    #same method as point binary to denary?
    num = str(denary_number).split(".")
    integer_number = int(num[0])
    fractional_number = float("0." + num[1])

    integer_binary = denary_to_binary(integer_number)
    
    fractional_binary = ""
    weighting = 0.5
    limit = False
    while fractional_number != 0 and not limit:
        #use subtraction method
        if (fractional_number - weighting) >= 0:
            fractional_number = fractional_number - weighting
            weighting = weighting / 2
            fractional_binary += "1"
        else:
            weighting = weighting / 2
            fractional_binary += "0"

        #since fractional numbers can't be fully represented in binary:
        if len(fractional_binary) > 6:
            limit = True

    binary_number = "0" + integer_binary + "." + fractional_binary
    return binary_number
    

def allign_floating_points(num1,num2):
    #enter num1 and num2 as lists
    index1 = num1.index(".")
    index2 = num2.index(".")

    #allign num1 against num2
    if index1 > index2:
        while num1.index(".") > num2.index("."):
            num2.insert(0,"0")

    else:
        while num1.index(".") < num2.index("."):
            num1.insert(0, "0")

    num1 = twos_comp.list_to_string(num1)
    num2 = twos_comp.list_to_string(num2)

    num1,num2 = check_length_point(num1,num2)
    #print("\n",num1,num2)
    return num1,num2

def check_length_point(num1,num2):
    check_num1 = num1.split(".")
    check_num2 = num2.split(".")

    if len(check_num2[1]) < len(check_num2[1]):
        while len(check_num1[1]) != len(check_num2[1]):
            num2 = num2 + "0"
            check_num2 = num2.split(".")
    else:
        while len(check_num2[1]) != len(check_num1[1]):
            num1 = num1 + "0"
            check_num1 = num1.split(".")
        
    return num1,num2

def floating_point_subtraction(num1,num2):
    num2 = float(pointbinary_to_denary(num2))
    num2 = str(twos_comp.twos_complement(-num2))
    num1 = str(twos_comp.twos_complement(pointbinary_to_denary(num1)))
    return binary_operations.add_binary(num1,num2,True)

    
    
    

if __name__ == "__main__":
    #print(pointbinary_to_denary("01010.101"))
    #print(pointdenary_to_binary(5.625))

    original_binary = "01010.11"
    print(original_binary)
    denary = pointbinary_to_denary(original_binary)
    print("denary number:",denary)
    print("convert back to binary:",pointdenary_to_binary(denary))

    original_number = 5.625
    print("\n%.3f"%(original_number))
    binary = pointdenary_to_binary(original_number)
    print("binary number:",binary)
    print("convert back to denary:",pointbinary_to_denary(binary))
    


    
