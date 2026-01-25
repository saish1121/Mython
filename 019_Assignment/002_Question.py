# # 2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

Power = lambda No1, No2 : No1 * No2

def main():
    print("Enter the Number -")
    no1= int(input())

    print("Enter the Number -")
    no2 = int(input())

    ret = Power(no1,no2)

    print("The multiplication",ret)

if __name__ == "__main__":
    main()