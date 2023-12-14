
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
