def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def multiply(a: int, b: int):
    return a * b

def divide(a: int, b: int):
    return a / b

def main():
    input1 = int(input('input first number: '))
    input2 = int(input('input second number: '))
    operator = input('input operator (+|-|*|/): ')
    
    if (operator == '+'):
        print(add(input1, input2))
    elif (operator == '-'):
        print(subtract(input1, input2))
    elif (operator == '*'):
        print(multiply(input1, input2))
    elif (operator == '/'):
        print(divide(input1, input2))
    else:
        print('invalid operator')
    
    
main()