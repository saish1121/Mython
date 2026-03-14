# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15 
# Output: Divisible by 3 and 5


No1 = 0 

print("Enter the Number - ")

No1 = int(input())

if No1 % 3 == 0 and No1 % 5 == 0 :
    print("Divisible by 3 and 5")

else :
    print("Not divisible by 3 and 5")
    