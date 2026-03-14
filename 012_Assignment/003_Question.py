# 3. Write a program which accepts two numbers and prints addition, subtraction, multiplication and division

def Add(A,B):
    return A + B

def Sub(A,B):
    return A - B

def Div(A,B):
    return A % B 

def Mul(A,B):
    return A * B 


No1 = 0
No2 = 0

print("Enter the 1st Number - ")
No1 = int(input())

print("Enter the 2nd Number - ")
No2 = int(input())

Ret_1 = Add(No1,No2)
Ret_2 = Sub(No1,No2)
Ret_3 = Div(No1,No2)
Ret_4 = Mul(No1,No2)

print("Addition is - ",Ret_1)
print("Subtraction is - ",Ret_2)
print("Division - ",Ret_3)
print("Multiplication is - ",Ret_4)
