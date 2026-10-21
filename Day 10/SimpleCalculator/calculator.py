import art

print(art.logo)

def calculations(user_num1, user_operator, user_num2):
    answer = 0
    if user_operator == "+":
        answer = user_num1 + user_num2
    elif user_operator == "-":
        answer = user_num1 - user_num2
    elif user_operator == "*":
        answer = user_num1 * user_num2
    else:
        answer = user_num1 / user_num2
    return answer

def print_operators():
    operators_list = ["+", "-", "*", "/"]
    for operator in operators_list:
        print(operator)

def print_response(user_num1, user_operator, user_num2):
    print(f"{user_num1} {user_operator} {user_num2} = {calculations(user_num1, user_operator, user_num2)}")

user_num1 = eval(input("What is the first number? "))
print_operators()
user_operator = input("Pick an operator: ")
user_num2 = eval(input("What is the next number? "))
answer = calculations(user_num1, user_operator, user_num2)
print_response(user_num1, user_operator, user_num2)

while True:
    isContinue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to finish: ")
    if isContinue != 'y' and isContinue != 'n' and isContinue != 'q':
        print("Incorrect input, please try again.")
        continue
    if isContinue == 'y':
        user_num1 = answer
        print_operators()
        user_operator = input("Pick an operator: ")
        user_num2 = eval(input("What is the next number? "))
        answer = calculations(user_num1, user_operator, user_num2)
        print_response(user_num1, user_operator, user_num2)
    elif isContinue == 'n':
        user_num1 = eval(input("What is the first number? "))
        print_operators()
        user_operator = input("Pick an operator: ")
        user_num2 = eval(input("What is the next number? "))
        answer = calculations(user_num1, user_operator, user_num2)
        print_response(user_num1, user_operator, user_num2)
    else:
        break