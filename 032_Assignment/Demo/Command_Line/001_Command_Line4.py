import sys
# python 001_Command_line4 11 10
# print("Number of Command line aruguments are :",len(sys.argv)) argument vector(array)


# Main Function-------
def main():
    print("Command line arguments are :")

    print()

    ans = 0
    
    for i in range(len(sys.argv)):
        print("File Name is -",sys.argv[i])

    ans = int(sys.argv[1]) + int(sys.argv[2])
    print("Additon of ",sys.argv[1],"And",sys.argv[2],"is",ans)

    

# Starter--------
if __name__ == "__main__":
    main()