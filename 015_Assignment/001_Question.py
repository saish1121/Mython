# 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number.

Square = lambda No : No ** 2 

def main():

    number = int(input("Enter the Number - "))

    result = list()

    print("List is -")

    for i in range(number):
        data = int(input())
        result.append(data)

        ret = list(map(Square,result))

    print("The list is - ",ret)


    

if __name__ == "__main__":
    main()