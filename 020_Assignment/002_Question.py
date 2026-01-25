# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.

# • Both threads should accept one integer number as a parameter.
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.
# • After both threads complete execution, the main thread should display the message: “Exit from main”

import threading

def EvenFactor(No):
    result = list()
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            result.append(i)
            sum = sum + i
    print("EvenFactors are - ",result)
    print("Sum of even number is - ",sum)
    


def ODDFactor(No):
    result = list()
    sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            result.append(i)
            sum = sum + i
    print("OddFactors are -",result)
    print("Sum of odd is - ",sum)


def main():
    number = int(input("Enter the Number -"))

    t1 = threading.Thread(target=EvenFactor,args=(number,))
    t2 = threading.Thread(target=ODDFactor,args=(number,))

    t1. start()
    t2. start()

    t1.join()
    t2.join()


    print("End of main Function")

if __name__ == "__main__":
    main()