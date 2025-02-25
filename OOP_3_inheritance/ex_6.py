class Stack:
    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        elements = reversed(self.data)
        return "[" + ", ".join([str(el) for el in elements]) + "]"

s = Stack()
print(s.is_empy())
print(s)
s.push(6)
s.push(7)
print(s.is_empy())
print(s)
print(s.pop())
print(s)
