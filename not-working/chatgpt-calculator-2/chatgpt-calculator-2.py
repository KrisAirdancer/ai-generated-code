# Define a function to evaluate arithmetic expressions
def evaluate(expression):
    try:
        # Split the expression into operands and operator
        operands = expression.split()
        operator = operands[1]

        # Convert the operands to float values
        operand1 = float(operands[0])
        operand2 = float(operands[2])

        # Evaluate the expression and return the result
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
        else:
            return "Error: Invalid operator"
    except:
        # If the expression is invalid, return an error message
        return "Error: Invalid expression"

# Display prompt and wait for user input
while True:
    expression = input("Enter an arithmetic expression or 'q' to quit: ")

    # If user enters 'q', exit the program
    if expression.lower() == 'q':
        break

    # Evaluate the expression and print the result
    result = evaluate(expression)
    print("Result: ", result)
