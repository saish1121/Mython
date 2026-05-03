# 3: Design a Python application that creates two threads named EvenList and OddList.

# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def Even_List(No):
    result = []
    sum = 0 
    for i in No:
        if i % 2 == 0:
            result.append(i)
            sum = sum + i
    print("Even List - ",result)
    print("Sum of Even number is - ",sum)

def Odd_List(No):
    result = []
    sum = 0
    for i in No:
        if i % 2 != 0:
            result.append(i)
            sum = sum + i
    print("Odd List - ",result)
    print("Sum of Odd number is - ",sum)



def main():
    number = int(input("Enter the Number - "))

    arr = []

    for i in range(number):
        data = int(input())
        arr.append(data)

    print("The list is - ",arr)

    t1 = threading.Thread(target=Even_List,args=(arr,))
    t2 = threading.Thread(target=Odd_List,args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main Function")

if __name__ == "__main__":
    main()

