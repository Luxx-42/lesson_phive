# Task 3 added divisible by 0 and other errors
def add_calc(x, z):
    return x + z

def subtract_calc(x, z):
    return x - z

def multiply_calc(x, z):
    return x * z

def divide_calc(x, z):
    if z == 0: # added div / 0
        return "can't divide by zero" #added cant return 0
    return x / z