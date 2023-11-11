from logic_gates import *

def test():
    #testing circuits:

    #(A XOR B) OR (A AND B) - will be true unless both = 0
    print("(A XOR B) OR (A AND B)")
    A = int(input("A>"))
    B = int(input("B>"))
    answer_circuit = OR.answer((XOR.answer(A,B)),(AND.answer(A,B)))
    print(answer_circuit)

    #(A AND B) XOR (A OR NOT B)
    print("(A AND B) XOR (A OR NOT B)")
    answer_circuit = XOR.answer(AND.answer(A,B),OR.answer(A,NOT.answer(B)))
    print(answer_circuit)


def half_adder(A,B):
    A = int(A)
    B = int(B)
    
    #S = A XOR B; C = A AND B    
    S = XOR.answer(A,B)
    C = AND.answer(A,B)
    return S,C

def full_adder(A,B, Cin=0):
    bits = len(A)
    answer = ""
    
    for bit in range(bits):
        index = bits - bit - 1
        S1,carry1 = half_adder(A[index],B[index])
        S,carry2 = half_adder(S1,Cin)
        Cout = OR.answer(carry1,carry2)
        
        #print("%s add %s add %s equals %d carry %d"%(A[index],B[index],Cin,S,Cout))
        answer = str(S) + answer
        Cin = Cout

##    if Cout != 0:
##        answer = str(Cout) + answer
        #^final carry bit isn't included
    return answer

def test_full_adder():
    print("1010 + 1111")
    final_answer = full_adder("1010","1111")
    print("\nFinal Answer:",final_answer)

if __name__ == "__main__":
    while True:
        A = input("\n>")
        B = input(">")
        print("%s + %s"%(A,B))
        answer = full_adder(A,B)
        print("final answer",answer)
    
    
        
    
    
