class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack (FILO)
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            # closed para case
            if p in closeToOpen:
                # make sure stack has a preceding open para 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    # either a closed p came before an open
                    # or the closed para does not match its respective open
                    return False
            # open parantheses
            else:
                stack.append(p)
        
        # stack processed -> Valid parantheses 
        if not stack:
            return True
        else:
            return False