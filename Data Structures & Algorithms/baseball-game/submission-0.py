class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # init stack to track scores
        stack = []

        for op in operations:
            if op == "+":
                # add the prev two scores and append to stack
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # double the prev score then append to stack
                stack.append(2 * stack[-1])
            elif op == "C":
                # remove the prev score (pop it)
                stack.pop()
            else:
                # record the new score 
                stack.append(int(op))
        
        return sum(stack)