# app/calculator.py

# Import the new functions for exponentiation, square root, absolute value, and cube.
from app.operations import exponentiation, square_root, absolute_value, cube

def calculator():
    """Basic REPL calculator that performs exponentiation, square root, absolute value, and cube calculations."""
    
    print("Welcome to the calculator REPL! Type 'exit' to quit.")
    
    while True:
        user_input = input(
            "Enter an operation (exponentiation, sqrt, abs, cube) and the necessary numbers, or 'exit' to quit: "
        )

        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        try:
            parts = user_input.split()
            operation = parts[0]
            
            # Handle different cases based on the operation
            if operation in {"sqrt", "abs", "cube"}:
                num = float(parts[1])
            else:
                num1, num2 = float(parts[1]), float(parts[2])
                
        except (ValueError, IndexError):
            print("Invalid input. Please follow the format: <operation> <num1> <num2> for exponentiation, or <operation> <num1> for sqrt, abs, cube.")
            continue

        # Handle each operation
        if operation == "exponentiation":
            result = exponentiation(num1, num2)
        elif operation == "sqrt":
            try:
                result = square_root(num)
            except ValueError as e:
                print(e)
                continue
        elif operation == "abs":
            result = absolute_value(num)
        elif operation == "cube":
            result = cube(num)
        else:
            print(f"Unknown operation '{operation}'. Supported operations: exponentiation, sqrt, abs, cube.")
            continue

        print(f"Result: {result}")
