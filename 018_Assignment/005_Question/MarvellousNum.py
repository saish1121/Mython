# 5.Write a program which accept N numbers from user and store it into List. Return addition of all 
# prime numbers from that List. Main python file accepts N numbers from user and pass each 
# number to ChkPrime() function which is part of our user defined module named as 
# MarvellousNum. Name of the function from main python file should be ListPrime(). 

# Input : Number of elements : 10
# Input Elements : 11 5 7 4 8 5 10 2 5 9
# Output : 54 (prime number addition)

def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


    

