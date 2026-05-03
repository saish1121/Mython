#4. Write a program which accepts one number and prints reverse of that number.
#Input: 123 
#Output: 321

no1 = 0

print("Enter the Iteration - ")
no1 = int(input())

result = list()

for i in range(no1):
    Data = int(input())
    result.append(Data)

print(result)

new_result = list()

for i in result:
    new_result.append(result[-i])

print(new_result)

