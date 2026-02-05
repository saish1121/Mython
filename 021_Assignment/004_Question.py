# 4: Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.

import threading

sum_result = 0
product_result = 1

def Sum(data):
    global sum_result
    for num in data:
        sum_result += num


def Product(data):
    global product_result
    for num in data:
        product_result *= num


def main():
    data = [2, 3, 4, 5]

    t1 = threading.Thread(target=Sum, args=(data,))
    t2 = threading.Thread(target=Product, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", sum_result)
    print("Product of elements:", product_result)


if __name__ == "__main__":
    main()
