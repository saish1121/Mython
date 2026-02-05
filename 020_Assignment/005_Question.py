# 5: Design a Python application that creates two threads named Thread1 and Thread2.

# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.

# • Ensure that:
# ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronizatio


import threading

def Number(NO):
    print("Number in sequence - ")
    for i in range(1,NO+1):
        print(i,end=" ")
    print()

def R_number(No):
    print()
    print("Number in sequence(Reverse Order) - ")
    for i in range(No,0,-1):
        print(i,end=" ")
    print()

def main():
    print("Start of main Function")    
    print()
    number = 50

    t1 = threading.Thread(target=Number,args=(number,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=R_number,args=(number,))
    t2.start()
    t2.join()

    print()
    print("End of main Function")

if __name__ == "__main__":
    main()