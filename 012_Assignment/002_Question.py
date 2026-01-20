# 2. Write a program which accepts one number and prints its factors.
# Input: 12 
# Output: 1 2 3 4 6 12


no1 = 0

print("Enter the Iteration - ")

no1 = int(input())

result = list()

for i in range(1,no1+1):
    if no1 % i == 0 :
        result.append(i)
    
print(result)