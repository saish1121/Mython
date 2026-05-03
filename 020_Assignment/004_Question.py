# 4: Design a Python application that creates three threads named Small, Capital, and Digits.

# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def Small(No):
    print("Inside Small Function")
    print("Thread Name - ",threading.current_thread().name)
    print("Small Funtion ID - ",threading.get_ident())
    result = []
    for i in No:
        if i.islower():
            result.append(i)
    print("Small Letter are - ",result)

def Capital(No):    
    print("Inside Captial Function")
    print("Thread Name - ",threading.current_thread().name)
    print("Captial Funtion ID - ",threading.get_ident())
    result = []
    for i in No:
        if i.isupper():
            result.append(i)
    print("Capital Letter are - ",result)

def Digit(No):    
    print("Inside Digit Function")
    print("Thread Name - ",threading.current_thread().name)
    print("Digit Funtion ID - ",threading.get_ident())
    result = []
    for i in No:
        if i.isdigit():
            result.append(i)
    print("Digit Letter are - ",result)


def main():
    number = int(input("Enter the Number - "))

    arr = []

    for i in range(number):
        data = input()
        arr.append(data)

    print("The list is - ",arr)

    print("*" * 20)

    t1 = threading.Thread(target=Small,args=(arr,))
    t2 = threading.Thread(target=Capital,args=(arr,))
    t3= threading.Thread(target=Digit,args=(arr,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("*" * 20)
    print("End of main Function")

if __name__ == "__main__":
    main()

