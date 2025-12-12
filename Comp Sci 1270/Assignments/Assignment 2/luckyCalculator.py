# Gavin King                9-28-25
# Assignment 2
# This calculator can do your basic equations, as well as give a lucky number!

def addition(input, input2):
    answer = input + input2
    print("Your answer is", answer)

def subtraction(input, input2):
    answer = input - input2
    print("Your answer is", answer)

def multiplication(input, input2):
    answer = input * input2
    print("Your answer is", answer)    

def division(input, input2):
    answer = input / input2
    print("Your answer is", answer)

def floorDivide(input, input2):
    answer = input // input2
    print("Your answer is", answer)

def squareRoot(input, input2):
    answer = input ** input2
    print("Your answer is", answer)



print("Welcome to the Lucky Calculator what would you like to do?")
print("(C)alculation, (L)ucky number, or to (Q)uit?")
choice = input("")
if choice == "C":
    print("What calculation would you like to Preform?")
    calc = input("[+] [-] [*] [/] [//] [**] : ")
    if calc == "+":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        addition(integer, integer2)
    elif calc == "-":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        subtraction(integer, integer2)       
    elif calc == "*":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        multiplication(integer, integer2)       
    elif calc == "/":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        if integer or integer2 == 0:
            print("Error:  Cannot divide by zero!")
        else:
           division(integer, integer2)       
    elif calc == "//":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        if integer or integer2 == 0:
            print("Error:  Cannot divide by zero!")
        else:
           floorDivide(integer, integer2)    
    elif calc == "**":
        integer = int(input("Please enter your first integer: "))
        integer2 = int(input("Please enter your second integer: "))
        squareRoot(integer, integer2)       


elif choice == "L":
     integer = int(input("Please enter your first integer: "))
     integer2 = int(input("Please enter your second integer: "))
     if integer or integer2 == 0:
         print("Error: Cannot compute with a 0!")
     else:
      answer = (integer + integer2) * (integer/integer2) + 10 


elif choice == "Q":
    print("Goodbye")
else:
    print("Invalid Option: Please Restart Program")