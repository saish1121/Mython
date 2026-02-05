# 9. Write a program which display first 10 even numbers on screen. 
# Output : 2  4  6  8  10  12  14  16  18  20   


def Even():
    i = 1 
    while i <= 20 :
        if i % 2 == 0 :
            print(i, end=" ") # end = " " works like there is space and next number will print here
        i = i + 1 

def main():
    Even()

if __name__ == "__main__":
    main()

    


    
    
