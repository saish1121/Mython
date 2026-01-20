# 8. Write a lambda function which accepts two numbers and returns addition.

Add = lambda A,B : A + B

def main():
    no1 = int(input("Enter the 1st number - "))
    no2 = int(input("Enter the 2nd number - "))

    ret = Add(no1,no2)

    print("Addition is - ",ret)

if __name__ == "__main__":
    main()