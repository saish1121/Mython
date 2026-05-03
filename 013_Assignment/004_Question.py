# 4. Write a program which accepts one number and prints binary equivalent.

def printBinary(no):
    binary = ""

    while no > 0:
        binary = str(no % 2) + binary
        no = no // 2

    print("Binary equivalent is:", binary)

def main():
    num = int(input("Enter a number: "))
    printBinary(num)

if __name__ == "__main__":
    main()


