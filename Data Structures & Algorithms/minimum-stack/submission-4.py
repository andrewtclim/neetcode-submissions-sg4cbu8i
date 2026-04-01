class MinStack:

    def __init__(self):
        # initalize class object with two stacks
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push val onto normal stack as usual
        self.stack.append(val)
        
        # only keep the min value at the top of minStack
        if not self.minStack:
            # append if minStack is empty 
            self.minStack.append(val)
        else:
            # compare and only keep the minimum val
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
