class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a hashmap for the operations and their lambda funcs
        ops = {
            '+' : lambda a, b : a+b,
            '-' : lambda a, b : a-b,
            '*' : lambda a, b : a*b,
            '/' : lambda a, b : int(a/b)
        }

        # init stack to track progress of RPN
        stack = []

        for tok in tokens:
            # combine the last two values and apply op
            if tok in ops:
                # isolate the last two values 
                b = stack.pop()
                a = stack.pop()
                # attach result to stack 
                # ops[tok] returns a lambda function that expects two inputs 
                stack.append(ops[tok](a,b))

            # for nums, typecast them and add to stack
            else:
                stack.append(int(tok))
        
        return stack[0]

