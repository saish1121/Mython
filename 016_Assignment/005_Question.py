# 5.Write a program which display 10 to 1 on screen. 
# Output : 10  9  8  7  6  5  4  3  2  1

def Display(No):
    result = list()
    for i in range(1 ,No+1):
        result.append(i)
    return result    

def main():
    no = int(input("Enter the iterations - "))
    ret = Display(no)

    rest = list()

    for i in ret:
        rest.append(ret[-i])

    print(rest)


if __name__ == "__main__":
    main()