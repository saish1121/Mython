# 1.Design automation script which accept directory name and file extension from user. Display all files with that extension. 
# Usage : DirectoryFileSearch.py “Demo” “.txt” 
# Demo is name of directory and .txt is the extension that we want to search. 

import os 
import sys

def Directory_Scanner(Directory_name,Extension = ".txt"):

    File = input("Enter the File name - ")  

    print("directory name - ",File)  
   

    for folder_name,subfolder_name,file_name in os.walk(Directory_name):
        print("Folder name is - ",folder_name)                

        for file in file_name:
            if file.startswith(File):
                if file.endswith(Extension):
                    print(file)

        for file in file_name:
            if file.endswith(Extension):
                print(file)

def main():
    Directory_Scanner(sys.argv[1])

if __name__ == "__main__":
    main()