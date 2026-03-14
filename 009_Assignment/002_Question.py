# 2. Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input: 10 20 
# Output: 20 is greater


def ChkGreater(No1,No2):
    if No1 > No2 :
        return True
    else :
        return False
    

Value_1 = 0
Value_2 = 0

print("Enter 1st Number - ")
Value_1 = int(input())


print("Enter 2nd Number - ")
Value_2 = int(input())

Result = ChkGreater(Value_1,Value_2)

print(Result)

if Result == True :
    print("NO1 is Greater than No2")

else :
    print("NO2 is Greater than No1")


    