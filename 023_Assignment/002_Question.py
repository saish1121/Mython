# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# • The class should contain two instance variables:
# ◦ Name (Account holder name)
# ◦ Amount (Account balance)
# • The class should contain one class variable:
# ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
# ◦ Display() – displays account holder name and current balance
# ◦ Deposit() – accepts an amount from the user and adds it to balance

# ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if sufficient balance exists)
# ◦ CalculateInterest() – calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5
    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print("Account holder name - ",self.Name)
        print("Current balance - ",self.Amount)

    def Deposit(self):
        self.Add = int(input("Enter the Amount(Deposit) - "))
        self.Amount = self.Amount + self.Add
        print("Amount After Deposit - ",self.Amount)

    def Withdraw(self):
        self.withdraw = int(input("Enter the Amount(Withdraw) - "))

        if self.withdraw < self.Amount:
            self.Amount = self.Amount - self.withdraw

        else:
            print("Insufficient balance exists")

        print("Amount After Withdram - ",self.Amount)        

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        print("After Interest - ",self.Interest)
        

obj1 = BankAccount("Saish",5000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()


