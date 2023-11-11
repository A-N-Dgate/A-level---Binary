from binary_operations import *
#^for the check length function

def And(num1,num2):
    final_num = ""
    for index in range(len(num1)):
        if num1[index] == "1" and num2[index] == "1":
            final_num = final_num + "1"
        else:
            final_num = final_num + "0"

    return final_num

def Or(num1,num2):
    final_num = ""
    for index in range(len(num1)):
        if num1[index] == "1" or num2[index] == "1":
            final_num = final_num + "1"
        else:
            final_num = final_num + "0"

    return final_num

def Xor(num1,num2):
    final_num = ""
    for index in range(len(num1)):
        if num1[index] == "1" or num2[index] == "1":
            if num1[index] == "1" and num2[index] == "1":
                final_num = final_num + "0"
            else:
                final_num = final_num + "1"
        else:
            final_num = final_num + "0"

    return final_num

def Not(num1):
    final_num = ""
    for item in num1:
        if item == "1":
            final_num = final_num + "0"
        else:
            final_num = final_num + "1"

    return final_num


if __name__ == "__main__":
    while True:
        num1 = input(">")
        num2 = input(">")

        num1,num2 = check_length(num1,num2)
        print("a and b: %s \na or b: %s \na xor b: %s \nnot a: %s \nnot b: %s"%(And(num1,num2),Or(num1,num2),Xor(num1,num2),Not(num1),Not(num2)))
        
            
    
