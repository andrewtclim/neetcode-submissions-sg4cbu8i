class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init stack and hashmap for ops 
        stack = []
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b)
        }

        # iter over tokens 
        for tok in tokens:
            # operation -> pop off last two values and compute new value
            if tok in ops:
                b = stack.pop() 
                a = stack.pop()
                # access corresp. function from hashmap -> append new value
                stack.append(ops[tok](a, b))
            else:
                stack.append(int(tok))
        
        return stack[0]