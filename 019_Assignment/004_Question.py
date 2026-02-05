# 4.Write a program which contains filter(), map() and reduce() in it. Python application which 
# contains one list of numbers. List contains the numbers which are accepted from user. Filter 
# should filter out all such numbers which are even. Map function will calculate its square. 
# Reduce will return addition of all that numbers. 

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204 

from functools import reduce

def Fun(No):
    return No % 2 == 0

def Mun(No):
    return No ** 2 

def Run(a,b):
    return a + b

def Main():
    Data = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    ret = list(filter(Fun,Data))
    ret_2 = list(map(Mun,ret))
    ret_3 = reduce(Run,ret_2)

    print(ret)
    print(ret_2)
    print(ret_3)

if __name__ == "__main__":
    Main()
