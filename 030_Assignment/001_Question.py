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
    Ret = fobj.readlines()

    print("Total count of  line are - ",len(Ret))

    

def Main():
    File_Name = input("Enter the File Name - ")
    Directory_Scanner(File_Name)


if __name__ == "__main__":
    Main()