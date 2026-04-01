class MinStack:

    def __init__(self):
        # initalize two stacks 
        # general stack & astack to track most recent minimum value)
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        # append val to general stack as usual 
        self.stack.append(val)

        # update the minStack value (if we find a new minimum)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        # pop vals from both stacks 
        self.stack.pop()
        self.minStack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
