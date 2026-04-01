class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack (holds all open para)
        stack = []
        closeToOpen = {")":"(", "}":"{", "]":"["}
        
        for p in s:
            # closed para follow two conditions 
            if p in closeToOpen:
                # 1. match the last open para -> pop last open para
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                # 2. don't match last open or come before an open para -> invalid
                else:
                    return False
            # open para added to the top of stack
            else:
                stack.append(p)
        
        # all open para processed -> valid para
        if not stack:
            return True
        else:
            return False
