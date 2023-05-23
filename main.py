def add(x,y):
    """Addition"""
    return x + y

def subtract(x,y):
    """Subtraction"""
    return x - y

def multiply(x,y):
    """Multiplication"""
    return x * y

def divide(x,y):
    """Division"""
    return x / y

    if y !=0:
        return x / y
    else:
        return "Error: Cannot divide by zero!"
    
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice in ["1","2","3","4"]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))

    if choice == '1':
        print("Result:", add(num1,num2))
    elif choice == '2':
        print("Result:", subtract(num1,num2))
    elif choice == '3':
        print("Result:", multiply(num1,num2))
    elif choice == '4':
        print("Result", divide(num1,num2))
    else:
        print("Invalid input")