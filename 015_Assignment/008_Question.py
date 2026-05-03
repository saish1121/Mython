# 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

D_3_5 = lambda NO : NO % 3 == 0 and NO % 5 == 0 

def main():
    number = int(input("Enter the number -"))

    result = list()

    for i in range(number):
        data = int(input())
        result.append(data)

    print("The List is - ",result)

    ret = list(filter(D_3_5,result))

    print("Divisible by 3 and 5 is -",ret)

if __name__ == "__main__":
    main()
