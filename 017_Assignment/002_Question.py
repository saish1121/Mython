# 2. Write a program which accept one number and display below pattern. 
#Input - 5 
#Output -        *  *  *  *  *
#                *  *  *  *  *
#                *  *  *  *  *
#                *  *  *  *  * 


def stars(No):
    for i in range(1,No+1):
        print("* " * No)
           
            

def main():
    Number = int(input("Enter the Number - "))

    stars(Number)

if __name__ == "__main__":
    main()

    

