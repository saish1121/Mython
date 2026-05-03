# 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even numbers.

Check_Even = lambda No : No % 2 == 0 

def main():
    number = int(input("Enter the Number - "))
    
    result = list()

    for i in range(number):
        data = int(input())
        result.append(data)

        ret = list(filter(Check_Even,result))

    print("Even numbers are - ",ret)
        
if __name__ == "__main__":
    main()