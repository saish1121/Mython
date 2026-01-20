#2.Write a program which accepts one number and prints count of digits in that number.
#Input: 7521 
#Output: 4


No1 = 0

print("Enter the Digits") # Iteration input
No1 = int(input())

print("The Digits are -")

Result = list()


for i in range(No1):
    Data = int(input())
    Result.append(Data)

print(Result)
print(len(Result))
    
    



