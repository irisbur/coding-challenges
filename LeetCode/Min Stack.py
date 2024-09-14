
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Note: 0 is False in python! 
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if self.min_val is None or (val < self.min_val):
            self.min_val = val
        self.stack.append((val, self.min_val))

    def pop(self) -> None:
        last, min_val = self.stack.pop()
        if self.stack:
            self.min_val = self.stack[-1][1]
        else:
            self.min_val = None
        return last

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.min_val
        return None