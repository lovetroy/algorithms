from collections import deque


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_stack = deque()
        self.output_stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.output_stack:
            while len(self.input_stack) > 0:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.output_stack:
            while len(self.input_stack) > 0:
                self.output_stack.append(self.input_stack.pop())
        if not self.output_stack:
            return None
        return self.output_stack.__getitem__(-1)

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input_stack and not self.output_stack


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
