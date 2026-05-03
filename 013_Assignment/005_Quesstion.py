# 5. Write a program which accepts marks and displays grade.
# Condition Example:
# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail


def Result(Number):
    if Number >= 75 :
        return 75

    elif Number >= 60 :
        return 60

    elif Number >= 50 :
        return 50

    else :
        return False


Marks = 0.00

print("Enter the Marks - ")
Marks = float(input())

Ans = Result(Marks)

if Ans == 75 :
    print("Distinction")

elif Ans == 60 :
    print("First Class")

elif Ans == 50 :
    print("Second Class")

else :
    print("Fail")





