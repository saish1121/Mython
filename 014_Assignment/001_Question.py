# 1. Write a lambda function which accepts one number and returns square of that number

Square = lambda No : No ** 2

def main():
    no = 0

    print("Enter the Number - ")

    no = int(input())

    ret = Square(no)

    print("The Square of a number - ",ret)

if __name__ == "__main__":
    main()