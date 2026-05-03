# 5.Write a program which accepts one number and prints all odd numbers till that number.

def Odd_check(No):
    result = list() # Dukaandar chi topli
    for i in range(No):
        if i % 2 == 1 : # Condition
            result.append(i) # Append means will addup the values one by one in list

    return result

No1 = 0

print("Enter the Number -")

No1 = int(input())
ans = Odd_check(No1)

print("Odd Digit are - ",ans)