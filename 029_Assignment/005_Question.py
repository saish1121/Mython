# Problem Statement: 
# Write a program which accepts a file name and one string from the user and returns the frequency (count of 
# occurrences) of that string in the file.
# Input: Demo.txt Marvellous
# Expected Output: Count how many times "Marvellous" appears in Demo.txt

import os
import sys

def Directory_Scanner(FileName, Text):

    if os.path.exists(FileName) and os.path.isfile(FileName):
        print("File is Present in Directory")

        fobj = open(FileName, "r")
        Data = fobj.read()
        fobj.close()

        Count = Data.count(Text)

        if Count > 2 :
            print("Frequency of", Text, "is:", Count)

    else:
        print("No Such File is Present in Directory")


def main():
    Directory_Scanner(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
