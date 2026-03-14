#Q2) Count Words in a File
#Problem Statement: 
#Write a program which accepts a file name from the user and counts the total number of words in that file.
#Input: 
#Demo.txt
#Expected Output: 
#Total number of words in Demo.txt


import os

def Count_Words(FileName):

    Ret = False

    Ret = os.path.exists(FileName)
    if (Ret == False):
        print("File does not exist")
        return

    fobj = open(FileName, "r")
    Data = fobj.read()
    fobj.close()

    Words = Data.split()
    print("Total number of words in", FileName, "are:", len(Words))


def main():
    FileName = input("Enter file name: ")
    Count_Words(FileName)


if __name__ == "__main__":
    main()
