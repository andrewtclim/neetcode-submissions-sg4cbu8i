class MinStack:

    def __init__(self):
        # initalize two stacks
        self.stack = []
        self.min_stack = [] 

    def push(self, val: int) -> None:
        # to the general stack (push as normal)
        self.stack.append(val)

        # keep the minimum val at the top of min_stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # pop top value simultaneously 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
