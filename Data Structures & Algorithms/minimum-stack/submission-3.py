class MinStack:

    def __init__(self):
        # initalize class object with a stack and minstack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # push val into stack
        self.stack.append(val)

        # only keep the minimum num in the top of min_stack 
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # pop from both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
