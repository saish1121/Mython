# 1: Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def Even(No):
    result = list()
    for i in range(1,No+1):
        if i % 2 == 0:
            result.append(i)
    print("Even Numbers is - ",result)


def ODD(No):
    result = list()
    for i in range(1,No+1):
        if i % 2 == 1:
            result.append(i)
    print("Odd number is -",result)


def main():
    number = int(input("Enter the Number -"))

    t1 = threading.Thread(target=Even,args=(number,))
    t2 = threading.Thread(target=ODD,args=(number,))

    t1. start()
    t2. start()

    t1.join()
    t2.join()


    print("End of main Function")

if __name__ == "__main__":
    main()