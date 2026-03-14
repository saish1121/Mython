# 1. Write a program which accepts length and width of rectangle and prints area

def Area(A,B):
    result = 0
    result = A * B
    return result

No1 = 0.00
No2 = 0.00

print("Enter Length  - ")
No1 = float(input())


print("Enter width  - ")
No2 = float(input())

Ans = Area(No1,No2)
print("Area of Rectangle is - ",Ans)