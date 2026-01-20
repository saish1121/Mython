# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

Div_5 = lambda No : No % 5 == 0

def main():
    no = int(input("Enter the Number - "))

    ret = Div_5(no)

    print(ret)

    if ret == True :
        print("Divisible by 5")

    else :
        print("Not a Divisible by 5")

if __name__ == "__main__":
    main()