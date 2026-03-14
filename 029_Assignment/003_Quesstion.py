# Problem Statement: 
# Write a program which accepts an existing file name through command line arguments, creates a new file 
# named Demo.txt, and copies all contents from the given file into Demo.txt
# Input (Command Line): 
# ABC.txt
# Expected Output: 
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os

def Directory(Name):
    Ret = False

    Ret = os.path.exists(Name)
    if (Ret == False):
        print("Invalid Path......")

    Ret = os.path.isfile(Name)    
    if (Ret == False):
        print("No Such File Present....")

    fobj = open(Name,"r")
    Result = fobj.read()


    return Result


def New(Text):
    fobj_2 = open("NewFile.txt","w")
    fobj_2.write(Text)

def main():
    File = input("Enter the File Name - ")
    Res = Directory(File)
    print(Res)
    New(Res)


if __name__ == "__main__":
    main()