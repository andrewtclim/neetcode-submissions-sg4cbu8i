class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b,
            '/' : lambda a, b : int(a/b)
        }

        stack = []

        for tok in tokens:
            # operation case
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            # numerical case 
            else:
                stack.append(int(tok))
        
        return stack[-1]
