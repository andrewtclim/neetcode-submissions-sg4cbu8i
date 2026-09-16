class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a stack
        stack = []
        # hashmap to map out operations to a function 
        ops = {
            "+" : lambda a,b : a+b,
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a*b,
            "/" : lambda a,b :int(a/b)
        }

        for tok in tokens:
            # operation found 
            if tok in ops:
                # from right to left [a, b, ...]
                # problem defines subtraction as a-b and a/b here
                b = stack.pop()
                a = stack.pop()
                # call the corr func and append new value to stack 
                stack.append(ops[tok](a,b))
                
            # append next nums to stack 
            else:
                stack.append(int(tok))
        
        return stack[-1]

