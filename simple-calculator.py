def calculator():
    number_1 = float(input("Enter the first number:"))
    number_2 = float(input("Enter the second number:"))
    operation = input("Chose the operation (+-*/):")

    if operation == '+':
        return number_1 + number_2
    elif operation == '-':
        return number_1 - number_2
    elif operation == '/':
        return number_1 / number_2
    elif operation == '*':
        return number_1 * number_2
    else:
        return "invalid operation"

print(calculator())