# 1. Write a program which accepts one number and checks whether it is prime or not.
#Input: 11 
#Output: Prime Number


def Check_prime(NO):
    result = list()
    for i in range(1,NO+1):
        if NO % i == 0 :
            result.append(i)
    return result
                
No1 = 0

print("Enter the Values - ")
No1 = int(input())

ans = Check_prime(No1)
print(ans)

if len(ans) > 2 :
    print("Not a Prime Number")

else :
    print("Prime Number")

