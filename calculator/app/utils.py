from .classes import Stack
from .classes import Operation

op_add = Operation("+", 0)
op_sub = Operation("-", 0)
op_un_min = Operation("un_min", 2)
op_mul = Operation("*", 1)
op_div = Operation("/", 1)

operations = [op_add, op_sub, op_div, op_mul, op_un_min]
index = 0


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Your expression is incorrect: attempt to divide by zero!")


def unary_minus(a):
    return (-1) * a


def make_number(calculate):
    global index
    string_num = []
    while ((index < len(calculate)) and (calculate[index] != "(") and (calculate[index] != ")") and (
            (calculate[index] not in ["*", "-", "+", "/"])) and (calculate[index] != " ")):
        string_num.append(calculate[index])
        index = index + 1
    index = index - 1
    if "." in string_num:
        return float(''.join(string_num))
    else:
        return int(''.join(string_num))


def check_operation(elem, index, calculate):
    if ((elem == op_sub.op) and ((index == 0)
                                 or (calculate[index - 1] == "("))):
        return op_un_min
    else:
        for elem_op in operations:
            if (elem_op.op == elem):
                return elem_op
    return None


def make_list_ok(list_1):
    list_2 = []
    global index
    while index < len(list_1):
        elem = list_1[index]
        if (elem != " "):
            if (elem not in ["0", "1", "2", "3",
                             "4", "5", "6", "7", "8", "9"]):
                list_2.append(elem)
            else:
                list_2.append(make_number(list_1))
        index = index + 1
    return list_2


def convert_to_polish(calculate):
    calculate_polish = []
    s = Stack()
    index = 0
    for elem in calculate:
        if (elem == "("):
            s.push(elem)
        elif (elem == ")"):
            elem_stack = s.pop()
            if (elem_stack == "("):
                return "Your expression is incorrect!"
            else:
                while (elem_stack != "("):
                    if (elem_stack is None):
                        return "Stack is empty - your expression is incorrect: please enter correct sequence of brackets!"
                    calculate_polish.append(elem_stack)
                    elem_stack = s.pop()
        elif check_operation(elem, index, calculate) in operations:
            op_input = check_operation(elem, index, calculate)
            elem_stack = s.pop()
            while ((elem_stack in operations) and (
                    elem_stack.priority >= op_input.priority)):
                calculate_polish.append(elem_stack)
                elem_stack = s.pop()
            s.push(elem_stack)
            s.push(op_input)
        else:
            calculate_polish.append(elem)
        index = index + 1
    elem_stack = s.pop()
    while (elem_stack is not None):
        calculate_polish.append(elem_stack)
        elem_stack = s.pop()
    return calculate_polish


def calculate_expression(polish_calculate):
    global index
    s = Stack()
    for elem in polish_calculate:
        if elem not in operations:
            s.push(elem)
        else:
            if elem == op_add:
                elem_1 = s.pop()
                elem_2 = s.pop()
                s.push(add(elem_1, elem_2))
            if elem == op_mul:
                elem_1 = s.pop()
                elem_2 = s.pop()
                s.push(mul(elem_1, elem_2))
            if elem == op_un_min:
                elem_1 = s.pop()
                s.push(unary_minus(elem_1))
            if elem == op_sub:
                elem_1 = s.pop()
                elem_2 = s.pop()
                s.push(sub(elem_2, elem_1))
            if elem == op_div:
                elem_1 = s.pop()
                elem_2 = s.pop()
                s.push(div(elem_2, elem_1))
    index = 0
    return s.pop()
