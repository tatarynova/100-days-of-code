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
        answer = user_num1 * user_num2
    return answer

def print_operators():
    operators_list = ["+", "-", "*", "/"]
    for operator in operators_list:
        print(operator)

user_num1 = eval(input("What is the first number? "))
print_operators()
user_operator = input("Pick an operator: ")
user_num2 = eval(input("What is the next number? "))
answer = calculations(user_num1, user_operator, user_num2)
print(f"{user_num1} {user_operator} {user_num2} = {answer}")

while True:
    isContinue = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type 'q' to finish: ")
    if isContinue != 'y' or isContinue != 'n' or isContinue != 'q':
        continue
    elif isContinue == 'y':
        print_operators()
        user_operator = input("Pick an operator: ")
        user_num2 = eval(input("What is the next number? "))