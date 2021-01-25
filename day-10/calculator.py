from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    should_continue = True
    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        choice = input("Do you want to continue performing claculations? y or n: ")
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
