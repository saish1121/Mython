# 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of all elements.

from functools import reduce

Add = lambda A,B : A + B 

def main():

    no = 0 

    print("Enter the number -")
    no = int(input())

    result = list()

    sum = 0

    for i in range(no):
        data = int(input())
        result.append(data)

        sum = reduce(Add,result)

    print(sum)

if __name__ == "__main__":
    main()