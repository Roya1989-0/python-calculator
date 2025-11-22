def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again.")

def main():
    print("Simple Python Calculator")
    print("------------------------")

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    print("\nChoose operation:")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")

    choice = input("Enter option (1-4): ")

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
    else:
        print("Invalid option.")
        return

    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()
