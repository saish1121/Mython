# 2. Design automation script which accept directory name and two file extensions from user. 
# Rename all files with first file extension with the second file extenntion. 
# Usage : DirectoryRename.py “Demo” “.txt” “.doc”


import os 
import sys

def Directory_Scanner(Directory_name,Extension = ".txt"):

    File = input("Enter the File name - ")  

    print("directory name - ",File)  

    print("-" * 20)   
    print("Before Renaming - ")
    for folder_name,subfolder_name,file_name in os.walk(Directory_name):
        print("Folder name is - ",folder_name)                

        for file in file_name:
            if file.startswith(File):
                if File.endswith(Extension):
                    print(File)

        for file in file_name:
            if file.endswith(Extension):
                print(file)

    Rename_with = ".doc"

    print("-" * 20)    
    print("After Renaming - ")
    for folder_name,subfolder_name,file_name in os.walk(Directory_name):
        print("Folder name is - ",folder_name)                

        for file in file_name:
            if file.startswith(File):
                if file.endswith(Extension):
                    new = file.replace(Extension,Rename_with)
                    print(new)

        for file in file_name:
            if file.endswith(Extension):
                new = file.replace(Extension,Rename_with)
                print(new)
            
    

def main():
    Directory_Scanner(sys.argv[1])

if __name__ == "__main__":
    main()