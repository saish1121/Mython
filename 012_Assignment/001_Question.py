# 1. Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a 
# Output: Vowel


print("Enter the Character - ")
char = input()

if char == "a" or char == "i":
    print("Vowel")

elif char == "e" or char == "o":
    print("Vowel")

elif char == "u":
    print("Vowel")
            
else :
    print("Not a Vowel")