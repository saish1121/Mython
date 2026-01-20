#3. Write a program which accepts one number and prints factorial of that number.
# Input: 5 
# Output: 120


No1 = 0 

print("Enter The Number - ")

No1 = int(input())

sum = 1

for i in range(1,No1+1):
    sum = sum * i
print("Output : ",sum)