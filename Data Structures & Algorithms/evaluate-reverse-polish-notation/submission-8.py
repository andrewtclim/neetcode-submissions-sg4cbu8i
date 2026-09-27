class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a stack to process results (stack[-1] -> latest value)
        stack = []
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a-b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b)
        }

        for tok in tokens:
            if tok in ops:
                # div and subtraction take place from right to left
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[tok](a, b))
            else:
                # push the new value as an int
                stack.append(int(tok))
        
        return stack[-1]