# 1: Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.


import threading

def isPrime(no):
    if no < 2:
        return False
    for i in range(2, no):
        if no % i == 0:
            return False
    return True


def Prime(data):
    print("Prime numbers:")
    for num in data:
        if isPrime(num):
            print(num, end=" ")
    print()


def NonPrime(data):
    print("Non-prime numbers:")
    for num in data:
        if not isPrime(num):
            print(num, end=" ")
    print()


def main():
    data = [11, 8, 5, 16, 7, 10, 13]

    t1 = threading.Thread(target=Prime, args=(data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()


