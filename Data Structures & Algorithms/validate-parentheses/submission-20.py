class Solution:
    def isValid(self, s: str) -> bool:
        # initalize a stack (holds all open para)
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        # iterate through string
        for p in s:
            # closed case
            if p in closeToOpen:
                # stack must have a preceding open para and they must match
                if not stack or stack[-1] != closeToOpen[p]:
                    return False
                else:
                    stack.pop()
            # open case
            else:
                stack.append(p)

        
        # all open para are processed
        if not stack:
            return True
        else:
            return False
