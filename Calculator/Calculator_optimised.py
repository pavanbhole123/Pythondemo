""" Accept two numbers + operator from user
• Use a function for each operation
• Handle division by zero — don't crash
• Loop: ask to calculate again """
    
from ast import operator


def add(a, b):
    return a + b
def subtract(a, b):
    return a - b  
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
while True:
    number1 = int(input("Enter first number: "))#10
    number2 = int(input("Enter second number: "))#20
    op = input("Enter operator (+, -, *, /): ")#+
    if op not in operators: #+
        print("Invalid operator")
        continue
    result = operators[op](number1, number2) #oprators[+] add(number1, number2)
             #add(number1, number2) 
    print("Result: ", result)
    again = input("Do you want to calculate again? (yes/no): ")#yes no
    if again.lower() == "no":  
        break   
        
    