class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init hashmap for operations 
        ops = {
            "+" : lambda a, b : a + b, 
            "-" : lambda a, b : a - b, 
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b) # rounds towards zero 
        }
        stack = [] # last value on the stack is the last value (performed op on)

        # ex) [1, 2, +] means 1 + 2 so here 1=a and 2=b
        for tok in tokens:
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            else:
                stack.append(int(tok))

        return stack[-1]
            