# 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum element.

from functools import reduce

largest = lambda No1 , No2 : No1 if No1 > No2 else No2

def main():
    number = int(input("Enter the iteration number -"))

    result = list()

    for i in range(number):
        data = int(input())
        result.append(data)

    print(result)

    ret = reduce(largest,(result))

    print("The maximum Element is -" , ret)

if __name__ == "__main__":
    main()

    