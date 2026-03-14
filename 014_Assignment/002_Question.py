# 2. Write a lambda function which accepts one number and returns cube of that number....

Cube = lambda No : No ** 3

def main():
    no = 0

    print("Enter the Number - ")
    no = int(input())

    ret = Cube(no)
    print("The Cube of",no,"is",ret)

if __name__ == "__main__":
    main()