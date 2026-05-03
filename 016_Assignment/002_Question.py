# 2. Write a program which contains one function named as ChkNum() 
# which accept one parameter as number. If number is even then it should display “Even number” otherwise 
# display “Odd number” on console. 
# Input : 11   Output : Odd Number 
# Input : 8  Output : Even Number

def ChkNum(No):    
    if No % 2 == 0:
        return True
    else :
        False

def main():
    no = 0

    print("Enter the Number - ")
    no = int(input())

    ret = ChkNum(no)

    if ret == True:
        print("Even Number - ",no)

    else :
        print("ODD Number - ",no)

if __name__ == "__main__":
    main()
