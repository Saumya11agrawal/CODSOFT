def calculator():
    print("Simple Calculator")
    print("Operation: + for addition, - for subtraction, * for multiplication, / for division")
    
    num1 = float(input("Enter the first number:"))
    operation = input("Enter the operation (+, -, *, /):")
    num2 = float(input("Enter the second number:"))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation.")
        return
    print(f"the result of{num1} {operation} {num2} is {result}")
calculator()               

