class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a stack that dynamically updates with RPN 
        stack = []
        # init a hashmap that maps the operation str with lambda func (a,b)
        ops = {
            "+" : lambda a,b : a+b, 
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a*b,
            "/" : lambda a,b : int(a/b)
        }

        for tok in tokens:
            # when we see an operation 
            # pop the first two vals in stack append the combination
            # NOTE: the first val popped is b and second is a 
            # stack is organized like [a, b, ...] where new val c = a - b
            if tok in ops:
                b = stack.pop()
                a = stack.pop()
                # apply operation 
                stack.append(ops[tok](a,b))
            # otherwise append and typecast the values into stack
            else:
                stack.append(int(tok))
        
        return stack[-1]

