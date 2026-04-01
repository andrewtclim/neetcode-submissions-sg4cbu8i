class Solution:
    def isValid(self, s: str) -> bool:
        # IDEA: stack will contain every open para, 
        # when we see a closed para it must match our last open para
        # initalize stack and hashmap 
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        # iterate over p
        for p in s:
            # closed case
            if p in closeToOpen:
                # stack must not be empty (an open p must exist before closed)
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                # either stack was empty or the last open para did not match closed para
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False
