# 3. Write a program which contains one function named as Add() which accepts two numbers 
# from user and return addition of that two numbers. 
# Input : 11    5     Output : 16


def Add(A,B):
    ans = 0
    ans = A + B
    return ans


def main():
    no1 = 0 
    no2 = 0

    print("enter the 1st number -") 
    no1 = int(input())

    print("enter the 2nd number -")
    no2 = int(input())

    ret = Add(no1,no2)

    print("Addition is - ",ret)

if __name__ == "__main__":
    main()
