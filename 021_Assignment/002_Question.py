# 2: Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

import threading

def Maximum(data):
    print("Maximum element:", max(data))


def Minimum(data):
    print("Minimum element:", min(data))


def main():
    data = []
    n = int(input("Enter number of elements: "))

    for i in range(n):
        data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(data,), name="MaxThread")
    t2 = threading.Thread(target=Minimum, args=(data,), name="MinThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
