class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

stack = Stack()
print(stack)

stack.push(5)
print(stack)

stack.push(28)
print(stack)

print(stack.peek())

stack.pop()
print(stack)

print(stack.size())