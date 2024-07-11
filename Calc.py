def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            if choice == '1':
                result = add(num1, num2)
                operation = "addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "division"
            
            print(f"The result of the {operation} is: {result}")
            break
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()
