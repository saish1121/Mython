# 5.Write a program which accept one number for user and check whether number is prime or not. 
# Input :  5
# Output : It is Prime Number 

def Fact(No):
    result = list()
    for i in range(1,No+1):
        if No % i == 0:
            result.append(i)
    return result 

def main():
    number = int(input("Enter the number -"))

    ret = Fact(number)
    print(ret)

    if len(ret) <= 2 :
        print("prime Number - ",number)

    else:
        print("Not a prime - ",number)
    
if __name__ == "__main__":
    main()
    


    
