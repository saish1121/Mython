# 10. Write a lambda function which accepts three numbers and returns largest number.

Largest = lambda A,B,C : max(A,B,C)

def main():
    no1 = int(input("Enter the 1st number - "))
    no2 = int(input("Enter the 2nd number - "))
    no3  = int(input("Enter the 3rd number - "))

    ret = Largest(no1,no2,no3)
    print("The largest number is - ",ret)   
    

if __name__ == "__main__":
    main()