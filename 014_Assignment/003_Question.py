# 3. Write a lambda function which accepts two numbers and returns maximum number.

Greater = lambda A,B: A > B

def main():
    no = 0
    no2 = 0

    print("Enter number 1 - ")
    no = int(input()) 

    print("Enter number 2 - ") 
    no2 = int(input()) 

    ret = Greater(no,no2)

    if ret == True:
        print("Number 1 is greater - ",no)

    else:
        print("Number 2 is greater - ",no2)

if __name__ == "__main__":
    main()

