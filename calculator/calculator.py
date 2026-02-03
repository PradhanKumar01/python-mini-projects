def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def calculate(choice, x, y):
    if choice == "1":
        return x + y
    elif choice == "2":
        return x - y
    elif choice == "3":
        return x * y
    elif choice == "4":
        if y == 0:
            return "Error: Division by zero"
        return x / y
    else:
        return "Invalid choice"


while True:
    show_menu()
    option = input("Select an option: ")

    if option == "5":
        print("Calculator closed.")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = calculate(option, a, b)
    print("Result:", result)
