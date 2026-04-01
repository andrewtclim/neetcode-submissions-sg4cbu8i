class MinStack:

    def __init__(self):
        # class objects will have two stacks
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # min_stack will only hold the minimum elem in stack
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
    # class method for checking the stacks in class object
    def reveal(self) -> str:
        return "The stack is {}.\n The minimum stack is {}".format(self.stack, self.min_stack) 
