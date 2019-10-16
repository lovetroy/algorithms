from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.appendleft(x)
        for i in range(len(self.queue) - 1):
            self.queue.appendleft(self.queue.pop())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue.__getitem__(-1)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
param_2 = obj.pop()
param_2 = obj.pop()
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
