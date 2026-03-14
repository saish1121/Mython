#8. Write a program which accept number from user and print that number of “*” on screen. 
# Input : 5  
# Output * * * * * 

def star(No):
    for i in range(1,No+1):
        star = "* "
    print(i * star)
    
def main():
    number = int(input("Enter the number - "))

    star(number)    

if __name__ == "__main__":
    main()
        

    
    
