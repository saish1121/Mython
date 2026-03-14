#3. Write a program which accepts one number and prints sum of digits.
#Input: 123 
#Output: 6


no1 = 0

print("Enter the Iteration - ")

no1 = int(input())

sum = 0
result = list()

for i in range(no1):
    Data = int(input())
    result.append(Data)
    sum = sum + Data

print("Data is - ",result)
print("Addition is - ",sum)