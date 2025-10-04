# for addition
def add(num1, num2):
    return num1 + num2

# for subtraction
def subtract(num1, num2):
    return num1 - num2

# for multiplication
def multiply(num1, num2):
    return num1 * num2

# for division
def divide(num1, num2):
    if (num2 == 0):
        return "ERROR: Division by zero is not allowed"
    else:    
        return num1 / num2

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))
choice = input("1:for addition\n2:for subtraction\n3:for multiplication\n4:for division\n--> ")

# Basic Calculator Function
def Calculator(num1, num2, choice):
    if choice == "1":
        print(f"Addition is {add(num1, num2)}")
    elif choice == "2":
        print(f"Subtraction is {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Multiplication is {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Division is {divide(num1, num2)}")
    else:
        print("Invalid Choice!")

Calculator(num1, num2, choice)