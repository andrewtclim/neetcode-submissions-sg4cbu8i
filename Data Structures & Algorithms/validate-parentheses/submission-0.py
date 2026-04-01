class Solution:
    def isValid(self, s: str) -> bool:
        # all odd inputs are invalid
        if len(s) % 2 != 0:
            return False

        # initalize stack and hashmap
        # stack will hold all OPEN parantheses
        stack = []
        closeToOpen = {")":"(",
                       "}":"{",
                       "]":"["
                        }
        for c in s:
            # if closed -> run a check 
            if c in closeToOpen:
                # if match -> remove the last open 
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # add all open to stack
            else:
                stack.append(c)
        
        # if the stack is empty at the end -> valid 
        return True if not stack else False

        