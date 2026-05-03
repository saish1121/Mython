# 1. Write a program which accepts one number and prints multiplication table of that number.
# Input: 4 
# Output: 4 8 12 16 20 24 28 32 36 40


No1 = 0 

print("Enter the number - ")

No1 = int(input())

print("Multiple of",No1,"is -")

result = list()

print("*" * 12)
print("Without List -  ")
for i in range(1,11):
    print(No1 * i)

print("*" * 12)
print("With List - ")
for i in range(1,11):
    ans = No1 * i 
    result.append(ans)

print(result)
print("*" * 12)
