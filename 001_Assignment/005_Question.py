# Q. Predict the output
    # a = 10 
    # b = 10
    # print(id(a) == id(b))

# Output - 
    # True

# Why - 
    # Object store the type information of an datatype.
    # Object is 10 which is interger.
    # Both Variable reference to the same object in return object will store at same memory address.


a = 10 
b = 10 

print(id(a) == id(b))

