import sys
# python 001_Command_line4 11 10
# print("Number of Command line aruguments are :",len(sys.argv)) argument vector(array)


# Main Function-------
def main():
    if (len(sys.argv) < 3 or len(sys.argv) > 3):
        print("Invaild no.of Arguments")

    else :
        ans = 0
        for i in range(len(sys.argv)):
            print("File Name is -",sys.argv[i])

        ans = int(sys.argv[1]) + int(sys.argv[2])
        print("Additon of ",sys.argv[1],"And",sys.argv[2],"is",ans)

    

# Starter--------
if __name__ == "__main__":
    main()


        #No1 = int(sys.argv[1])
        #No2 = int(sys.argv[2])
        #Ans = 0

        #Ans = No1 + No2

        #print(Ans)