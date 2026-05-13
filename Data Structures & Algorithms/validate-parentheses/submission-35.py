class Solution:
    def isValid(self, s: str) -> bool:
        # initalize a stack and a hashmap 
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        # iterate over the stack
        # rules of stack: always add any open para, check if closed para is valid and matching
        for p in s:
            # closed case
            if p in closeToOpen:
                # if the stack is non empty (has an open para) and the first stack elem matches our corr closed para
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False