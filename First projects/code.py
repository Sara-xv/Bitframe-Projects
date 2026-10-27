#  create a Command-Line Calculator with python 

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
    print(" ")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice (1/2/3/4/5): ")
 
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("first")
            num2 = get_number("second")
 
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
 
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            print("I hope you enjoyed using the calculator. Have a great day!")
            break
        else:
            print("Invalid input. Please select a valid operation.")
 
 
if __name__ == "__main__":
    main()




'''
با ارسال کد به  هوش مصنوعی یک کد بهینه تر دریافت کردم 
By sending the code to AI, I received a more optimized version of the code
'''
# code:

 
## create a Command-Line Calculator with python 

# def get_number(number):
#     while True:
#         try:
#             return float(input(f"Enter {number} number: "))
#         except ValueError:
#             print("Invalid input. Please enter a valid number.")


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):  
#     if b == 0:
#         return "Error! Division by zero."
#     else:
#         return a / b


# def show_menu():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")


# def main():
#     operations = {
#         "1": ("+", add),
#         "2": ("-", subtract),
#         "3": ("*", multiply),
#         "4": ("/", divide),
#     }

#     while True:
#         show_menu()
#         choice = input("Enter choice (1/2/3/4/5): ")

#         if choice in operations:
#             num1 = get_number("first")
#             num2 = get_number("second")

#             symbol, func = operations[choice]
#             result = func(num1, num2)
#             print(f"{num1} {symbol} {num2} = {result}")

#         elif choice == '5':
#             print("Exiting the calculator. Goodbye!")
#             print("I hope you enjoyed using the calculator. Have a great day!")
#             break
#         else:
#             print("Invalid input. Please select a valid operation.")


# if __name__ == "__main__":
#     main()
