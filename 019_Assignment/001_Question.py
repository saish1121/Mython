# 1.Write a program which contains one lambda function which accepts one parameter and returnpower of two.
# Input : 4 Output : 16
# Input : 6 Output : 64


Power = lambda No : No ** 2

def main():
    print("Enter the Number -")
    no = int(input())

    ret = Power(no)

    print("The Power",no,"is - ",ret)

if __name__ == "__main__":
    main()