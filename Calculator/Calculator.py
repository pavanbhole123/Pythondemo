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
while True:
    number1 = int(input("Enter first number: "))#10
    number2 = int(input("Enter second number: "))#20
    operator_input = input("Enter operator (+, -, *, /): ")#+
    if operator_input != "+" and operator_input != "-" and operator_input != "*" and operator_input != "/":
        print("Invalid operator. Please enter a valid operator.")
        continue
    if operator_input == "+":
        result = add(number1, number2)
    elif operator_input == "-":
        result = subtract(number1, number2)
    elif operator_input == "*":
        result = multiply(number1, number2)
    elif operator_input == "/":
        result = divide(number1, number2)
    print(f"Result: {result}")
    again = input("Do you want to calculate again? (yes/no): ")#yes no
    if again.lower() == "no":  
        break   
        
    