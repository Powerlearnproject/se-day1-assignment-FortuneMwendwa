def simple_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numbers.")

simple_calculator()
