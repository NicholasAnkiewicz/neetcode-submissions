class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = math.inf

    def push(self, val: int) -> None:
        if val < self.smallest:
            self.smallest = val
        self.stack.insert(0, (val, self.smallest))

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop(0)
            if len(self.stack) != 0:
                self.smallest = self.stack[0][1]
            else:
                self.smallest = math.inf

    def top(self) -> int:
        return self.stack[0][0]

    def getMin(self) -> int:
        return self.stack[0][1]
