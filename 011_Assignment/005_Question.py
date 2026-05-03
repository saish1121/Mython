#5. Write a program which accepts one number and checks whether it is palindrome or not.
#Input: 121 
#Output: Palindrome


no1 = 0

print("Enter the Iteration - ")
no1 = int(input())

result = list()

for i in range(no1):
    Data = int(input())
    result.append(Data)

print(result)

result_new = list()

for i in result:
    result_new.append(result[-i])

print(result_new)


if result == result_new :
    print("Palindrome")

else :
    print("Not a Palindrome")



