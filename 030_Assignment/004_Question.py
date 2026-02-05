# Problem Statement: 
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file



import os

def Copy_File(SourceFile, DestinationFile):

    Ret = False

    Ret = os.path.exists(SourceFile)
    if (Ret == False):
        print("File does not exist")
        return

    fsrc = open(SourceFile, "r")
    Data = fsrc.read()
    fsrc.close()

    fdest = open(DestinationFile, "w")
    fdest.write(Data)
    fdest.close()

    print("Contents of", SourceFile, "copied into", DestinationFile)


def main():
    SourceFile = input("Enter source file name: ")
    DestinationFile = input("Enter destination file name: ")

    Copy_File(SourceFile, DestinationFile)


if __name__ == "__main__":
    main()
