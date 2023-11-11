from hex_bin_den import *
from binary_operations import *
from floating_point_binary import *

from adders import *

def check_sign(number,answer):
    if number < 0:
        answer = "1" + answer
    else:
        answer = "0" + answer
    return answer

def check_number(number):
    if number < 0:
        number = -number
    return number

def sign_magnitude(number):
    #number = int(input(">"))
    positive_number = check_number(number)
    answer = denary_to_binary(positive_number)
    answer = check_sign(number,answer)
    return answer

def add_one(answer):
    #this function isn't used
    added = False
    index = len(answer) - 1
    while not added:
        if answer[index] == "0":
            answer[index] = "1"
            #make the previous digit 0?
            try:
                answer[index + 1] = "0"
            except: #the least significant bit is 1
                pass
            added = True
        else:
            index -= 1    
    return answer

def check_number_2(number,answer):
    #adding the number later - this doesn't work
    if number < 0:
        answer = list(answer)
        
        for digit_index in range(0, len(answer)):
            digit = answer[digit_index]
            #flip all bits
            if digit == "0":
                answer[digit_index] = "1"

            elif digit == "1":
                answer[digit_index] = "0"
       
        answer = add_one(answer)         
        answer = list_to_string(answer)
        answer = "1" + answer

    else:
        answer = "0" + answer
    return answer

def check_number2_2(number,answer):
    #doesn't work
    if number < 0:
        flip = False
        answer = reversed(list(answer))
        #^working from right to left to miss out the least significant 1
        for digit_index in range(0,len(answer)):
            if answer[digit_index - 1] == "1":
                flip = True # shouldn't set back to false
            if flip:
                #flip all bits
                if digit == "0":
                    answer[digit_index] = "1"

                elif digit == "1":
                    answer[digit_index] = "0"

        answer = list_to_string(reversed(answer))
        answer = "1" + answer
    else:
        answer = "0" + answer
    return answer

def check_number3_2(number,answer):
    #add one to the binary after flipping - doesn't work
    answer = "0" + answer
    if number < 0:
        answer = list(answer)
        for digit_index in range(len(answer)):
            digit = answer[digit_index]
            #flip all bits
            if digit == "0":
                answer[digit_index] = "1"

            elif digit == "1":
                answer[digit_index] = "0"

        #add one to the answer using binary addition
        answer = list_to_string(answer)
        
        #get binary number for 1 with correct number of 0s
        one = "1"
##        for number in range(0,len(answer)-1):
##            one = "0" + one
        #^done in check length
            
        answer = add_binary(answer,one)

        if answer[0] != "1":
            answer = "1" + answer 

    return answer

def check_number4_2(number,answer):
    #flipping all the bits, convert to denary, add one, then back to binary
    answer = "0" + answer
    if number < 0:
        print("positive binary: ", answer)
        answer = list(answer)
        for digit_index in range(len(answer)):
            #print(digit_index)
            digit = answer[digit_index]
            #flip all bits
            if digit == "0":
                answer[digit_index] = "1"

            elif digit == "1":
                answer[digit_index] = "0"

            elif digit == ".":
                pass
                #print("point found")
            #print(answer)
        #^this all works
        answer = list_to_string(answer)
        
##        if "." in list(str(number)):
##            answer = float(pointbinary_to_denary(answer)) + 1
##            answer = pointdenary_to_binary(answer)
##        else: 
##            answer = int(binary_to_denary(answer)) + 1
##            answer = denary_to_binary(answer)
        #converting to denary then adding one doesn't work

##        if "." in list(str(number)):
##            #adding one doesn't work
##            one = ["0",".","1"]
##            if len(one) != len(answer):
##                one.insert((one.index(".")+1),"0")
##            
##            answer = binary_operations.add_binary(answer,one)
##        else:
##            answer = binary_operations.add_binary(answer,"1")
##        
##        answer = "1" + answer

        point_index = -1
        if "." in list(str(number)):
            answer = list(answer)
            point_index = answer.index(".")
            answer.remove(".")
            answer = list_to_string(answer)
            
        one = "1"
        for number in range(0,len(answer)-1):
            one = "0" + one

        answer = full_adder(answer,one)
        if point_index > 0:
            answer = list(answer)
            answer.insert(point_index,".")
            answer = list_to_string(answer)

        answer = "1" + answer
        #^this works?       

    return answer

def list_to_string(char_list):
    string = ""
    for letter in char_list:
        string = string + letter
    return string

def twos_complement(number):
    positive_number = check_number(number)
    #print("positive number:",positive_number)
    if isinstance(positive_number, float):
        #print("floating point number")
        answer = pointdenary_to_binary(positive_number)
    else:
        answer = denary_to_binary(positive_number)
    answer = check_number4_2(number,answer)
    return answer

if __name__ == "__main__":
    while True:
        number = input(">")
##        if len(str(int(number))) + 2 == len(str(float(number))):
##            number = int(number)
##        else:
##            number = float(number)

        try:
            number = int(number)
        except:
            number = float(number)
        print(twos_complement(number))
    
    
