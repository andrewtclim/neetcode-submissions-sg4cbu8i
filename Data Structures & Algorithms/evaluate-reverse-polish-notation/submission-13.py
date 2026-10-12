class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # hashmap of ops 
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b)
        }
        stack = []

        for tok in tokens:
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            else:
                stack.append(int(tok))
        
        return stack[-1]