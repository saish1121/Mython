# 2. Write a program which accepts radius of circle and prints area of circle

def Circle(Value):
    result = 0 
    pi = 3.14
    result = (pi * (Value ** 2))
    return result


Rad = 0.00


print("Enter the Radius  - ")
Rad = float(input())

Ans = Circle(Rad)
print("Area of Circle is - ",Ans)
