# Problem Statement: 
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input: Demo.txt
# Expected Output: Display whether Demo.txt exists or not.

import os

def Directory_Scanner(Directory_Name):
    Ret = False
    Ret = os.path.exists(Directory_Name)
    Ret_1 = os.path.isdir(Directory_Name)


    if (Ret == True and Ret_1 == True):
        print("File is Present in Directory")

    
    else :
        print("No Such File is Present in Directory")   




def main():
    File_name = input("Enter the File Name - ")
    Directory_Scanner(File_name)

if __name__ == "__main__":
    main()