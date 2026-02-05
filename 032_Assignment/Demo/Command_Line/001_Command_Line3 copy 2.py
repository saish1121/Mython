import sys
# print("Number of Command line aruguments are :",len(sys.argv)) argument vector(array)


# Main Function-------
def main():
    print("Command line arguments are :")

    print()
    
    for i in range(len(sys.argv)):
        print(sys.argv[i])
    

# Starter--------
if __name__ == "__main__":
    main()