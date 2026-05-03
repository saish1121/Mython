# Problem Statement: 
# Write a program which accepts a file name and a word from the user and checks whether that word is present in 
# the file or not.
# Input: 
# Demo.txt Marvellous
# Expected Output: 
# Display whether the word Marvellous is found in Demo.txt or not.


import os

def Search_Word(FileName, Word):
    Ret = False
    Ret =  os.path.exists(FileName)

    if Ret == False:
        print("File does not exist")
        return

    fobj = open(FileName, "r")
    Data = fobj.read()
    fobj.close()

    if Word in Data:
        print("Word", Word, "is present in the file")
    else:
        print("Word", Word, "is not present in the file")


def main():
    FileName = input("Enter file name: ")
    Word = input("Enter word to search: ")

    Search_Word(FileName, Word)


if __name__ == "__main__":
    main()
