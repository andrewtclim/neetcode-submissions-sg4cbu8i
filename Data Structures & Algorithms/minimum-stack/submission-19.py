class MinStack:

    def __init__(self):
        # init a regular stack and a stack that always keeps the minimum val on top 
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # regular stack 
        self.stack.append(val)
        # min_stack -> always append the smallest value (compare new val with old)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # we can simply pop from both stacks as normal 
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
