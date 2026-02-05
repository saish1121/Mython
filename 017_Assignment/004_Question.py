# 4.Write a program which accept one number form user and return addition of its factors. 
# Input :  12
# Output : 16 ((1+2+3+4+6))

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

    sum = 0

    for i in ret:
        sum = sum + i

    print("Addition is - ",sum)
    

if __name__ == "__main__":
    main()
    
