#7.  Write a program which accept one number and display below pattern. 
# Input : 5
# Output :   1  2  3  4  5
#            1  2  3  4  5
#            1  2  3  4  5
#            1  2  3  4  5

def PF(No):
    for j in range(1,No+1):         # rows (4 times if No = 5)
        for i in range(1,No+1):     # columns (1 to 5)
            print(i,end=" ")
        print()                     # new line after each row

def main():
    no = int(input("Enter the Number -"))

    PF(no)

if __name__ == "__main__":
    main()