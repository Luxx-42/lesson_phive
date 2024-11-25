# Task 4 added together to create basikk calc

def add_calc(x, z):
    return x + z

def subtract_calc(x, z):
    return x - z

def multiply_calc(x, z):
    return x * z

def divide_calc(x, z):
    if z == 0:
        return "can't divide by zero"
    return x / z

numero_1 = float(input("Enter your first number: "))

operation = input("enter (+, -, *, /): ")

numero_2 = float(input("Enter your second number: "))

if operation == '+':
    rez = add_calc(numero_1, numero_2)

elif operation == '-':
    rez = subtract_calc(numero_1, numero_2)

elif operation == '*':
    rez = multiply_calc(numero_1, numero_2)

elif operation == '/':
    rez = divide_calc(numero_1, numero_2)

else:
    print("Incorrect operation")

print(f' rezult: {rez}')