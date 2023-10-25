# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function
def main():
    print("Simple Calculator")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation choice (1/2/3/4): ")

    # Perform calculation based on user's choice
    if operation == '1':
        result = add(num1, num2)
    elif operation == '2':
        result = subtract(num1, num2)
    elif operation == '3':
        result = multiply(num1, num2)
    elif operation == '4':
        result = divide(num1, num2)
    else:
        result = "Invalid operation choice."

    # Display the result
    print("Result: ", result)

# Call the main function
if __name__ == "__main__":
    main()
