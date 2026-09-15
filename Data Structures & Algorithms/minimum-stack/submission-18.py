class MinStack:

    def __init__(self):
        # two stacks a regular one and a min stack one 
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # normal stack 
        self.stack.append(val)
        
        # init an empty min_stack with the first value
        if not self.min_stack:
            self.min_stack.append(val)
        # otherwise always keep the smallest val on min stack 
        else:
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> None:
        # pop from both stacks 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
