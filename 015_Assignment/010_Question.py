# 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers.

Check_Even = lambda No : No % 2 == 0 

def main():
    number = int(input("Enter the Number - "))
    
    result = list()

    sum = 0 

    for i in range(number):
        data = int(input())
        result.append(data)

        ret = list(filter(Check_Even,result))

    print("Count of even numbers - ",len(ret))
        
if __name__ == "__main__":
    main()