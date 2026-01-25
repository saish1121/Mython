# 3. Write a program which accept one number from user and return its factorial. 
# Input :  5
# Output : 120 

def Fac(No):
    sum = 1
    for i in range(1 , No+1):
        sum = sum * i
    print(sum)

def main():
    no = 0 

    print("enter the number - ")
    no = int(input())

    Fac(no)

if __name__ == "__main__":
    main()
    
