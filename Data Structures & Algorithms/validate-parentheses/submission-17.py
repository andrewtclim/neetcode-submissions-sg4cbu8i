class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack 
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            # closed case
            if p in closeToOpen:
                # stack must have preceding open and that open p must match this closed p 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        # all open p processed 
        if not stack:
            return True
        else:
            return False