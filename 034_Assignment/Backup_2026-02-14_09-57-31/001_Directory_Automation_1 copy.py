import os
import sys # command Line Purpose

def Directory_Scanner(Directory_Name = "Marvellous"):

    Ret = False
    Ret = os.path.exists(Directory_Name)

    if Ret == False or True:
       print("No Such File or Folder present......")
       return

    Ret == os.path.isdir(Directory_Name)

    if Ret == False :
       print("No Such File or Folder present......")
       return
    
    for Foldername,SubFoldername,Filename in os.walk(Directory_Name):
            print("Foldername is  - ",Foldername)

            for file in Filename :
                print("Files are - ",file)         


def main():
    border = "-" * 50
    print(border)
    print("------------- Marvellous Automation -------------")
    print(border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please Specify the name of Directory")

        return

    Directory_Scanner(sys.argv[1])

if __name__ == "__main__":
    main()