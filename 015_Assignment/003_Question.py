# 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

Check_Odd = lambda No : No % 2 == 1

def main():
    number = int(input("Enter the Number - "))
    
    result = list()

    for i in range(number):
        data = int(input())
        result.append(data)

        ret = list(filter(Check_Odd,result))

    print("Odd numbers are - ",ret)


        


if __name__ == "__main__":
    main()