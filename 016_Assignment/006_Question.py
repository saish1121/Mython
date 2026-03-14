#6.Write a program which accept number from user and check whether that number is positive or negative or zero. 
#Input : 11     Output : Positive Number 
#Input : 0      Output : Zero 
#Input : -8     Output : Negative Number     
#Input : 25     Output : Positive Number 


def Check_Number(No):
    if No > 0 :
        return "True"
    elif No < 0 :
        return "False"
    elif No == 0:
        return "0"
      
def main():
    Number = int(input("Enter the Number - "))

    ret = Check_Number(Number)

    if ret == "True":
        print("Positive Number")
    
    elif ret == "False":
        print("Negative Number")

    elif ret == "0" :
        print("The Number is Zero")

if __name__ == "__main__":
    main()
    
    
    
