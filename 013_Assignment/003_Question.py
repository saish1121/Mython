# 3. Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6 
# Output: Perfect Number

no1 = 0 

print("Enter the Number - ")
no1 = int(input())

result = list()

for i in range(1,no1):
    if no1 % i == 0:
        result.append(i)
print("Factors are - ",result)

sum = 0

for i in result:
    sum = sum + i 
print("Addition is - ",sum)


if no1 == sum :
    print("Perfect Number")

else :
    print("Not a Perfect Number")