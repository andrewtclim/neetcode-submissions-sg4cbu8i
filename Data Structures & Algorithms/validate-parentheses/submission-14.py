class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack (holds all open para)
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for p in s:
            # closed para
            if p in closeToOpen:
                # must match the last open para
                # the stack must have had a preceding open para
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False