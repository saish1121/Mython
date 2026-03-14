# Problem Statement: 
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the 
# screen.
# Expected Output: 
# Display each line of Demo.txt one by one.



import os

def Display_Line_By_Line(FileName):
    Ret = False

    Ret = os.path.exists(FileName)
    if (Ret == False):
        print("File does not exist")
        return

    fobj = open(FileName, "r")

    for line in fobj:
        print(line, end="")

    fobj.close()


def main():
    FileName = input("Enter file name: ")
    Display_Line_By_Line(FileName)


if __name__ == "__main__":
    main()
