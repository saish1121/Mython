# 5. Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5 
# Output: 5 4 3 2 1


def Fun(new):
    result = list()
    for i in new:
        result.append(new[-i])

    return result


no = 0 

print("Enter the Iteration - ")
no = int(input())

new = list()

for i in range(no):
    Data = int(input())
    new.append(Data)


ans = Fun(new)
print(ans)
