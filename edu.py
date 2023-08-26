class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)


s = Stack()
s.push("Dave")
s.push([23,13])
s.push([42, 45])
p = s.pop()
z = s.pop()
print(p)
print(z)
print(s.stack)
print(s.length)