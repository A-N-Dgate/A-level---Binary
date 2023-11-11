class gate():
    def __init__(self, name):
        self.name = name.upper()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def answer(self, num1, num2):
        #calculates the answer from the name of the gate
        #seperate into subclasses
        if num1 > 1 or num2 > 1:
            return "Error: numbers have to be one or zero"
        
        if self.get_name() == "OR":
            answer = num1 or num2
            
        if self.get_name() == "AND":
            answer = num1 and num2
            
        if self.get_name() == "NOT":
            if num1 == 1:
                answer = 0
            else:
                answer = 1

        if self.get_name() == "XOR":
            if num1 == 1 and num2 == 1:
                answer = 0
            elif num1 == 1 or num2 == 1:
                answer = 1
            else:
                answer = 0

        if self.get_name() == "NAND":
            if num1 == 1 and num2 == 1:
                answer = 0
            else:
                answer = 1

        if self.get_name() == "NOR":
            if num1 == 1 or num2 == 1:
                answer = 0
            else:
                answer = 1

        return answer

#names don't matter in the subclasses since they overwrite the answer method
    #the parent class probably isn't needed either.
class and_gate(gate):
    def __init__(self):
        gate.__init__(self,"AND")

    def answer(self,num1,num2):
        answer = num1 and num2
        return answer

class or_gate(gate):
    def __init__(self):
        gate.__init__(self,"OR")

    def answer(self,num1,num2):
        answer = num1 or num2
        return answer

class not_gate(gate):
    def __init__(self):
        gate.__init__(self,"NOT")

    def answer(self,num1):
        if num1 == 1:
            answer = 0
        else:
            answer = 1
        return answer

class xor_gate(gate):
    def __init__(self):
        gate.__init__(self,"XOR")

    def answer(self,num1,num2):
        if num1 == 1 and num2 == 1:
            answer = 0
        elif num1 == 1 or num2 == 1:
            answer = 1
        else:
            answer = 0
        return answer

class nand_gate(gate):
    def __init__(self):
        gate.__init__(self,"NAND")

    def answer(self,num1,num2):
        if num1 == 1 and num2 == 1:
            answer = 0
        else:
            answer = 1
        return answer
        
#so that the varibales can be imported   
AND = and_gate()
OR = or_gate()
XOR = xor_gate()
NOT = not_gate()
NAND = nand_gate()        
    
            
            

if __name__ == "__main__":
    #testing if the logic gates work
##    AND = gate("and")
##    OR = gate("or")
##    XOR = gate("xor")
##    NOT = gate("not")
##    NAND = gate("nand")

    AND = and_gate()
    OR = or_gate()
    XOR = xor_gate()
    NOT = not_gate()
    NAND = nand_gate()

    and_truth_table = [AND.answer(0,0),AND.answer(0,1),AND.answer(1,0),AND.answer(1,1)]
    print("AND truth table")
    for item in and_truth_table:
        print(item)

    or_truth_table = [OR.answer(0,0),OR.answer(0,1),OR.answer(1,0), OR.answer(1,1)]
    print("\nOR truth table")
    for item in or_truth_table:
        print(item)

    xor_truth_table = [XOR.answer(0,0),XOR.answer(0,1),XOR.answer(1,0),XOR.answer(1,1)]
    print("\nXOR truth table")
    for item in xor_truth_table:
        print(item)

    not_truth_table = [NOT.answer(0),NOT.answer(1)]
    print("\nNOT truth table")
    for item in not_truth_table:
        print(item)

    nand_truth_table = [NAND.answer(0,0),NAND.answer(0,1),NAND.answer(1,0),NAND.answer(1,1)]
    print("\nNAND truth table")
    for item in nand_truth_table:
        print(item)





            
            
        







