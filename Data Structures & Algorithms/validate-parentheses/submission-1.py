class Solution:
    def isValid(self, s: str) -> bool:
        # all valid strings must be even 
        if len(s) % 2 != 0:
            return False

        # initalize stack and hashmap 
        stack = []
        closeToOpen = {"}":"{", ")":"(", "]":"["}

        # loop through string 
        for c in s:
            # closed
            if stack and c in closeToOpen:
                if stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # open
            else:
                stack.append(c)
        
        # all open parantheses have matched 
        if not stack:
            return True
        else:
            return False

        