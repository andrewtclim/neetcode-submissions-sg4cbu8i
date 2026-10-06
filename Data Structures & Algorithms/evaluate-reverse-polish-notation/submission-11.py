class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # utilize stack 
        stack = []
        ops = {
            '+' : lambda a, b : a + b,
            '-' : lambda a, b : a - b,
            '*' : lambda a, b : a * b,
            '/' : lambda a, b : int(a/b)
        }

        for tok in tokens:
            # operation case (pop last two and combine new value, push onto stack)
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            else:
                stack.append(int(tok))
        
        return stack[-1]