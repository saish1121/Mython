# 2. Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5 
# Output: 15


No1 = 0

print("Input is  - ")

No1 = int(input())

sum = 0 

for i in range(No1):
    sum = sum + i

print("Outut is  - ",sum)
