# 6. Write a lambda function which accepts one number and returns True if number is odd otherwise False.

Check_odd = lambda No : No % 2 == 1 

def main():
    number = int(input("Enter the number - "))

    ret = Check_odd(number)
    print(ret)

    if ret == True:
        print("Odd")

    else :
        print("Even")

if __name__ == "__main__":
    main()