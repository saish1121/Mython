# 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings having length greater than 5.

Check = lambda input : len(input) > 5 

def main():

    number = 0

    print("Enter the number of Iteration - ")
    number = int(input())

    result = list()

    print("*" * 50)
    print("Strings are - ")

    for i in range(number):
        string = input()
        result.append(string)

    print("String are -",result)

    ret = list(filter(Check,result))

    print("list of strings having length greater than 5 - ",ret)

    print("*" * 50)


if __name__ == "__main__":
    main()

    