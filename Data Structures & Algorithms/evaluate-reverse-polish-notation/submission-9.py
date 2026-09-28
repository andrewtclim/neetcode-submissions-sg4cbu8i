class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init stack (top of stack is the last product)
        stack = []
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b)
        }

        for tok in tokens:
            # apply operations to last two values 
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            
            # numerical values get added to the top of stack
            else:
                stack.append(int(tok))
        
        return stack[-1]
