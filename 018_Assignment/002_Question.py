# 2.Write a program which accept N numbers from user and store it into List. Return Maximan of all elements from that List. 
#Input : Number of elements : 7
#Input Elements : 13 5 45 7 4 56 34
#Output : 56

def Add(No):
    zero = No[0]
    print(zero)
    for i in range(1,No):
        if zero > i:            
            print(zero)
    return zero

def main():
    no = 0

    print("Enter the Number - ")
    no = int(input())

    result = list()

    for i in range(no):
        data = int(input())
        result.append(data)

    print(result)

    ret = Add(result)

    print("Sum is -",ret)

if __name__ == "__main__":
    main()
