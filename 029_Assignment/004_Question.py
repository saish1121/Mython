# Problem Statement: 
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure

import os
import sys

def File1(Text):

    Ret = False

    Ret = os.path.exists(Text)

    if (Ret == True):
        fobj = open(Text,"r")
        Result = fobj.read()
        print(Text,"Having this text - ",Result)

    return Result

def File2(Text):

    Ret = False

    Ret = os.path.exists(Text)

    if (Ret == True):
        fobj = open(Text,"r")
        Result = fobj.read()
        print(Text,"Having this text - ",Result)

    return Result

def main():
    Ans1 = File1(sys.argv[1])
    Ans2 = File2(sys.argv[2])

    if Ans1 == Ans2 :
        print("Success")

    else:
        print("Failure")
    

if __name__ == "__main__":
    main()