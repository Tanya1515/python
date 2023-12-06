from classes import Stack
from classes import Operation

def add (a, b):
    return a + b

def mul (a, b):
    return a * b

def sub (a, b):
    return a - b

def div (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Your expression is incorrect: attempt to divide by zero")

def unary_minus (a):
    return (-1)*a

def polish (calculate):
    calculate_polish = []
    for elem in calculate:

    return calculate_polish

if __name__ == '__main__':
    calculate = list(input())

    print(calculate)
