# 9. Write a lambda function which accepts two numbers and returns multiplication.

Mul = lambda A,B : A * B

def main():
    no1 = int(input("Enter the 1st number - "))
    no2 = int(input("Enter the 2nd number - "))

    ret = Mul(no1,no2)

    print("Multiplication is - ",ret)

if __name__ == "__main__":
    main()