class Solution:
    def isValid(self, s: str) -> bool:
        # init a stack and hashmap 
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for p in s:
            # closed case
            if p in closeToOpen:
                # stack must exist (have a prior open para) and match
                if stack and closeToOpen[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # open paras always add to stack 
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False
