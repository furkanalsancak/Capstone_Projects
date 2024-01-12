import math

def add(num1, num2):
    total = num1 + num2
    return total

def subtract(num1, num2):
    total = num2 - num1
    return total

def multiply(num1, num2):
    total = num1 * num2
    return total

def divide(num1, num2):
    total = num1 / num2
    return total

def power(num1, num2):
    total = num1 ** num2
    return total

def sqrt(num):
    total = math.sqrt(num)
    return total

def modulus(num1, num2):
    total = num1 % num2
    return total





print("Simple Calculator")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Choose operation (+, -, *, /): ")

while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose operation (+, -, *, /, **, sqrt, %)(-1 to exit): ")
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '**':
        result = power(num1, num2)
    elif operation == 'sqrt':
        result = sqrt(num1)
    elif operation == '%':
        result = modulus(num1, num2)
    elif operation == '-1':
        break
    else:
        print("Invalid operation")
    print(f"Result: {result}")

