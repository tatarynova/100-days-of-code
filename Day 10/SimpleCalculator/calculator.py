import art


def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number? "))
    while True:
        for key in operations:
            print(key)
        operator = input("Pick an operator: ")
        num2 = float(input("What is the next number? "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        isContinue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to finish: ")
        while (isContinue != 'n' and isContinue != 'q' and isContinue != 'y'):
            print("Incorrect input, please try again.")
            isContinue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to finish: ")
        if isContinue == 'y':
            num1 = answer
        elif isContinue == 'n':
            num1 = float(input("What is the first number? "))
        else:
            break

calculator()