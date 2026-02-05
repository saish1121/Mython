# 1.Design automation script which accept directory name and display checksum of all files. 
# Usage : DirectoryChecksum.py “Demo” 
# Demo is name of directory. 

import os
import sys
import hashlib # command Line Purpose


def Check_sum(Name):
    fobj = open(Name,"rb")
    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)> 0):
        hobj.update(Buffer)
        Buffer= fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def Directory_Scanner(Dir_Name):
    Ret = False

    Ret = os.path.exists(Dir_Name)
    if (Ret == False):
        print("No Such Folder Present at path Location....")

    
    Ret = os.path.isdir(Dir_Name)
    if (Ret == False):
        print("NO Folder Present.....")


    for Folder_Name,Sub_Folder_Name,File_Names in os.walk(Dir_Name):
        for File in File_Names:
            Ret = os.path.join(Folder_Name,File)
            print("File are - ",Ret)
            Check = Check_sum(Ret)

    print("Check_sum - ",Check)


def main():
    FileName = input("Enter the Directory Name - ")
    Directory_Scanner(FileName)


if __name__ == "__main__":
    main()





