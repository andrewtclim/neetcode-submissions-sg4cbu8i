class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack FILO 
        # stack will only contain closed para
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}

        # iterate through parantheses
        for p in s:
            # closed para
            if p in closeToOpen:
                # stack must have a prior open para and it must match with the current closed
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        # if the stack is empty -> all open p were processed
        if not stack:
            return True
        else:
            return False