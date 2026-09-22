class Solution:
    def isValid(self, s: str) -> bool:
        # stack only holds open paras waiting to be processed
        stack = []
        closeToOpen = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        for p in s:
            # closed case
            if p in closeToOpen:
                # valid (check if this closing para matches the last open)
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                # otherwise its an invalid closed para -> invalid
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        # whole stack processed -> valid 
        if not stack:
            return True
        else:
            return False
