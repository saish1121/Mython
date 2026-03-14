# 1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List. 
#Input : Number of elements : 6 
#Input Elements : 13 5 45 7 4 56
#Output : 130 

def Add(No):
    ans = 0 
    for i in No:
        ans = ans + i
    return ans

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
