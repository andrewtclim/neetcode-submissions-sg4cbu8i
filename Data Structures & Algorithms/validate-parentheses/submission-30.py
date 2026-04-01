class Solution:
    def isValid(self, s: str) -> bool:
        # init stack holds open paras 
        # top is next open para to be matched
        stack = []
        closeToOpen = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for p in s:
            # next close para must follow
            # 1) stack must not be empty -> open para before closed
            # 2) if it matches last open para -> pop open para
            if p in closeToOpen:
                if stack and closeToOpen[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # all open para will be added to stack 
            # ex) (((()))) -> 4 valid open paras added
            else: 
                stack.append(p)
        
        # if the whole stack processed -> valid, otherwise trailing unclosed open para
        if not stack:
            return True
        else:
            return False