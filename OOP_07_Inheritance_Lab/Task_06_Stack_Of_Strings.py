class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) > 0:
            return False
        else:
            return True

    def __str__(self):
        self.data.reverse()
        result = "[" + ", ".join([str(x) for x in self.data]) + "]"
        self.data.reverse()
        return result


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack))  # '[carrot, apple]'
print(stack.pop())  # 'carrot'
print(stack.top())  # 'apple'
stack.push("cucumber")
print(str(stack))  # '[cucumber, apple]'
print(stack.is_empty())  # False
