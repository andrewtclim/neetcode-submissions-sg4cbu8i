class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Stack of numbers. Each operator pops the top two values,
        applies the op, and pushes the result. Final answer is the
        one value left on the stack.

        Key details:
        - Pop order matters: second-popped is `a`, first-popped is `b`.
          So `a - b` and `int(a / b)` respect the original order.
        - `int(a / b)` truncates toward zero (LC 150 requirement)
          `a // b` would floor toward negative infinity, wrong for negatives.
        '''
        stack = []
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b, 
            "/" : lambda a, b : int(a/b)
        }

        for tok in tokens:
            # operation case
            if tok in ops:
                # define our last two values 
                b = stack.pop()
                a = stack.pop()
                # apply function to a and b then append new value to stack 
                stack.append(ops[tok](a, b))
            # numerical case
            else:
                stack.append(int(tok))
        
        return stack[-1]