from abc import ABC, abstractmethod

class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed
    def push(self, item):
        self.stack.append(item)

class Operation:
    def __init__(self, op, priority):
       self.op = op
       self.priority = priority

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
        print("Your expression is incorrect: attempt to divide by zero!")

def unary_minus (a):
    return (-1)*a