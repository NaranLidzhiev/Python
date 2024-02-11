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

    def printstack(self):
        print(self.stack)


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.printstack()

