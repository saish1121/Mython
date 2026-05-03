# 1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() 
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two 
# parameters as number and perform the operation. Write on python program which call all the 
# functions from Arithmetic module by accepting the parameters from user.  

from Arithmetic_Server import Add,Sub,Mul,Div

def main():
    no1 = int(input("Enter the 1st Number -"))
    no2 = int(input("Enter the 2nd Number -"))

    ret1 = Add(no1,no2)
    ret2 = Sub(no1,no2)
    ret3 = Mul(no1,no2)
    ret4 = Div(no1,no2)

    print("Addition is - ",ret1)
    print("Subtraction is - ",ret2)
    print("Multiplication is - ",ret3)
    print("Division is - ",ret4)

main()