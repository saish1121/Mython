# 5.Write a program which accept N numbers from user and store it into List. Return addition of all 
# prime numbers from that List. Main python file accepts N numbers from user and pass each 
# number to ChkPrime() function which is part of our user defined module named as 
# MarvellousNum. Name of the function from main python file should be ListPrime(). 

# Input : Number of elements : 10
# Input Elements : 11 5 7 4 8 5 10 2 5 9
# Output : 54 (prime number addition)

import MarvellousNum

def ListPrime(lst):
    total = 0

    for num in lst:
        if MarvellousNum.ChkPrime(num):
            total = total + num

    return total


def main():
    print("Number of elements:")
    n = int(input())

    data = []
    print("Enter elements:")
    for i in range(n):
        data.append(int(input()))

    result = ListPrime(data)
    print("Addition of prime numbers is:", result)


if __name__ == "__main__":
    main()
