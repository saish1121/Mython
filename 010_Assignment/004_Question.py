# 4. Write a program which accepts one number and prints all even numbers till that number.
# Input: 10 
# Output: 2 4 6 8 10 


def Check_Even(No):
    result = list() # Dukaandar chi topli
    for i in range(1,No+1):
        if i % 2 == 0: # Condition 
            result.append(i) # Append - will add one after other in list 
    return result

NO1 = 0 

print("Enter the Number - ")
NO1 = int(input())

ans = Check_Even(NO1)
print(ans)