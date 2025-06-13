from collections import deque


class Stack:
    def __init__(
        self,
    ):
        self.data = deque()
        self.top = None
        self.len = 0

    def push(self, value):
        self.data.append(value)
        self.top = value
        self.len += 1

    def pop(self):
        if self.len == 0:
            return None
        else:
            self.top = self.data.pop()
            self.len -= 1
            return self.top

    def peek(self):
        return self.top

    def is_empty(self):
        return True if self.len == 0 else False

    def size(self):
        return self.len


st = Stack()
st.push(1)
print(st.peek(), st.size())


st.push(3)
print(st.peek(), st.size())


st.push(5)
print(st.peek(), st.size())


st.pop()
print(st.peek(), st.size())
