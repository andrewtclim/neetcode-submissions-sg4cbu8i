class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init a hashmap of operations and corresponding lambda functions 
        ops = {
            "+" : lambda a, b : a + b,
            "-" : lambda a, b : a - b,
            "*" : lambda a, b : a * b,
            "/" : lambda a, b : int(a/b)
        }

        # init stack 
        stack = []

        # iter through tokens 
        for i in tokens:
            # replace the last two values with the corresponing operation value
            if i in ops:
                # isolate first and second values (visualize stack)
                b = int(stack.pop())
                a = int(stack.pop())
                # then find and call the operation 
                new_val = ops[i](a, b)
                # push the new value
                stack.append(new_val)

            # add nums to the stack (also typecast)
            else:
                stack.append(int(i))
        
        return stack[-1]

