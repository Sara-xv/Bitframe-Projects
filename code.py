#  create a Command-Line Calculator with python 

#  
def get_number(number):
    while True:
        try:
            return float(input(f"Enter {number} number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):  
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b


def show_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    