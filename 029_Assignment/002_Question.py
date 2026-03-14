# Q2) Display File Contents
# Problem Statement: 
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input: Demo.txt
# Expected Output: Display contents of Demo.txt on console.

import os

def Directory_Scanner(Directory_Name):
    Ret = False

    Ret = os.path.exists(Directory_Name)
    if (Ret == False):
        print("No Such File Present")

    Ret = os.path.isfile(Directory_Name)    
    if (Ret == False):
        print("No Such File Present...")

    fobj = open(Directory_Name,"r")
    Ret = fobj.read()

    print(Ret)

    fobj.close()


def Main():
    File_Name = input("Enter the File Name - ")
    Directory_Scanner(File_Name)


if __name__ == "__main__":
    Main()