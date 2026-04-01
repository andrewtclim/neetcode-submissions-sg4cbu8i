class MinStack:

    def __init__(self):
        # initalize the stack and minstack (the class object will have)
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # push as usual to stack 
        self.stack.append(val)

        # only keep the min val at the top of minStack 
        if not self.minStack:
            self.minStack.append(val)
        # compare val to the current min Value
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
