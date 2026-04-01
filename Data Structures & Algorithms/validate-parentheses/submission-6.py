class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(",
                       "]" : "[",
                       "}" : "{"}
        
        if len(s) % 2 != 0:
            return False
        
        for p in s:
            # closed para
            if stack and p in closeToOpen:
                if stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open para
            else:
                stack.append(p)
        
        # stack is processed (valid) otherwise (invalid)
        if not stack:
            return True 
        else:
            return False
        
        # note - open paras must come before closed 
        # which is why we check if stack (stack must not be empty to process closed)