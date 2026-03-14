#4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List. 
# Input : Number of elements : 10
# Input Elements : 13 5 7 4 56 5 34 2 5 65
# Element to search : 5 
# Output : 3 

def Frequency(No):    
        sum = 0
        element = int(input("Element - "))
        for j in No:
            if j == element:
                sum = sum + 1 
        return sum

def main():
    Number = 0

    print("Number of Element - ")
    Number = int(input())

    rest = list()

    for i in range(Number):
        data = int(input())
        rest.append(data)

    print(rest)

    ret = Frequency(rest)

    print("Total number of Element in list - ",ret)

if __name__ == "__main__":
    main()