
def calculator(number1, number2, operator):

    if operator == '*':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '**':
        return number1 ** number2
    elif operator == '/':
        if number2 == 0:
            return 'False'
        return number1 / number2
    elif operator == '//':
        if number2 == 0:
            return 'False'
        return number1 // number2
    elif operator == '-':
        return number1 - number2

    
    
def parse_input():
    user_input = input ("Enter equation: ")
    user_input = user_input.strip().split(" ")

    number1 = float(user_input[0])
    number2 = float(user_input[2])
    operator = user_input[1]
