# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce

def Filter(No):
    return No >= 70 and No <= 90

def Map(No):
    return No + 10

def red(A,B):
    return A * B   
    

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    ret_1 = list(filter(Filter,Data))
    ret_2 = list(map(Map,ret_1))
    ret_3 = reduce(red,ret_2)
    

    print("Filted Value is - ",ret_1)
    print("Mapped Value is - ",ret_2)
    print("Reduced Value is - ",ret_3)

if __name__ == "__main__":
    main()