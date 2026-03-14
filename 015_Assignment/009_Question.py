# 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all elements.
from functools import reduce

product = lambda A,B: A * B

def main():
    number = int(input("Enter the number - "))

    result = list()

    for i in range(number):
        data = int(input())
        result.append(data)

    print("List is - ",result)

    ret = reduce(product,result)
    print("Product of all elements - ",ret)

if __name__ == "__main__":
    main()