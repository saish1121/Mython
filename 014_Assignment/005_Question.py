# 5. Write a lambda function which accepts one number and returns True if number is even otherwise False.

Check_Even = lambda No : No % 2 == 0

def main():
    number = int(input("Enter the number - "))

    ret = Check_Even(number)
    print(ret)

    if ret == True :
        print("Even")

    else :
        print("Odd")

if __name__ == "__main__":
    main()