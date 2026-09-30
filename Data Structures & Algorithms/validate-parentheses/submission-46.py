class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", 
                        "]":"[", 
                        ")":"("}

        for p in s:
            # closed case 
            if p in closeToOpen:
                # check if closed para is valid (does it match our last open para?)
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    # closed para came before open or didnt match the last open para
                    return False

            # open case -> always push onto stacks
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False
