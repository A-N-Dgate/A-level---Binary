from hex_bin_den import *
from binary_operations import *
from normalisation import *

def testing_addition():
    #space between the mantissa and exponent
    num1 = "0.101101 0011"
    num2 = "0.111011 0101"

    one = num1.split(" ")
    two = num2.split(" ")

    adding_num1 = expand_number(one[0],one[1])
    adding_num2 = expand_number(two[0],two[1])

    answer = add_binary(adding_num1, adding_num2)

    print(normalise_number(answer))

def testing_subtraction():
    num1 = "0.111011 0101"
    num2 = "0.101101 0010"

    one = num1.split(" ")
    two = num2.split(" ")

    adding_num1 = expand_number(one[0],one[1])
    adding_num2 = expand_number(two[0],two[1])

    answer = floating_point_subtraction(adding_num1, adding_num2)
    print("unnormalised answer: %s"%(answer))
    print("normlaised answer:",normalise_number(answer))

#testing_addition()
testing_subtraction()
    
