#Q6. Program to display data type, memory address, and size

x = input("Enter a value: ")

print("Data type:", type(x))
print("Memory address:", id(x))
import sys
print("Size in bytes:", sys.getsizeof(x))


#Explanation:
#type() → shows data type
#id() → shows memory address
#getsizeof() → shows size in bytes

#(In Python, type() gives data type, id() gives memory location, and getsizeof() gives memory size.)