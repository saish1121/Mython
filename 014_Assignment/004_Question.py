# 4. Write a lambda function which accepts two numbers and returns minimum number.

Smaller = lambda A,B : A < B 

def main():
    no1 = 0
    no2 = 0

    print("Enter the 1st number - ")
    no1 = int(input())

    print("Enter the 2nd number - ")
    no2 = int(input())

    ret = Smaller(no1,no2)

    if Smaller == True:
        print("1st Number is Smaller - ",no1)

    else :
        print("2nd Number is Smaller - ",no2)

if __name__ == "__main__":
    main()


