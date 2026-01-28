# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.

# • Implement the following instance methods:
# ◦ Accept() – accepts values for Value1 and Value2 from the user.
# ◦ Addition() – returns the addition of Value1 and Value2.
# ◦ Subtraction() – returns the subtraction of Value1 and Value2.
# ◦ Multiplication() – returns the multiplication of Value1 and Value2.
# ◦ Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).

# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        
        print("*" * 40)
        print("Enter Value1 -")
        self.Value1 = int(input())

        print("Enter Value2 -")
        self.Value2 = int(input())

    def Add(self):
        Ans = 0 
        Ans = self.Value1 + self.Value2
        print("Addition -",Ans)
    
    def Sub(self):
        Ans = 0 
        Ans = self.Value1 - self.Value2
        print("Subtraction -",Ans)        
    
    def Mul(self):
        Ans = 0 
        Ans = self.Value1 * self.Value2
        print("Multiplication",Ans)          
    
    def Divsion(self):
        Ans = 0 
        Ans = self.Value1 % self.Value2
        print("Division - ",Ans)
        
    
obj1 = Arithmetic()
obj1.Accept()
obj1.Add()
obj1.Sub()
obj1.Mul()
obj1.Divsion()

obj2 = Arithmetic()
obj2.Accept()
obj2.Add()
obj2.Sub()
obj2.Mul()
obj2.Divsion()

obj3 = Arithmetic()
obj3.Accept()
obj3.Add()
obj3.Sub()
obj3.Mul()
obj3.Divsion()

