# 9. Write a program which accept number from user and return number of digits in that number. 
# Input : 5187934   
# Output : 7 

def numbers(No):
    print("length is -",len(No))

def main():
    no = 0

    print("Enter the iteration - ")
    no = int(input())

    result = list()

    for i in range(no):
        data = int(input())
        result.append(data)

    print("List is -",result)

    numbers(result)

if __name__ == "__main__":
    main()