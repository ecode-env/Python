from art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def compute():
    print(logo)
    first_number = float(input("Enter first number: "))
    keep_calculating = True
    while keep_calculating:

        for operator in calculator:
            print(operator)
        operation = input("Choose the operation: ")
        next_number = float(input("Enter next number: "))

        print(f"{first_number} {operation} {next_number} = {calculator[operation](first_number, next_number)}")
        should_continuous = str(input(
            f"Type 'y' to continue calculating with {calculator[operation](first_number, next_number)}, or type 'n' to start a new calculation: "))
        temp = calculator[operation](first_number, next_number)
        if should_continuous == 'y':
            first_number = temp
        if should_continuous == 'n':
            break
        else:
            keep_calculating = False
            print("\n" * 20)
            compute()
compute()


