# 7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false. 
#Input : 8  Output : False 
#Input 25   Output : True 


def Div_5(No):
    if No % 5 == 0:
        return True
    
def main():
    number = int(input("Enter the number - "))

    ret = Div_5(number)

    if ret == True :
        print(number,"is divisible by 5 ")
    else :
        print("Not a divisible by 5")

if __name__ == "__main__":
    main()
    
    
    
