# 4. Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5 
# Output: 1 2 3 4 5

def Fun(No1):
    result = list()
    for i in range(1,No1+1):
        result.append(i)

    return result


No = 0

print("Enter the Iteration - ")
No = int(input())

Ans = Fun(No)

print("Output is - ",Ans)