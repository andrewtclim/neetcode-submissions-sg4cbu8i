class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack and hashmap (close -> matching open)
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            # closed case
            if p in closeToOpen:
                # closed para must pass 1. an open para must precede 2. the closed must match its last open
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        # all open para match with their closed para
        if not stack:
            return True 
        else:
            return False
