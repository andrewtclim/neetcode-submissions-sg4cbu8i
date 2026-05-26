class Solution:
    def isValid(self, s: str) -> bool:
        # init stack and hashmap 
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for p in s:
            if p in closeToOpen:
                # check conditions, closed para must match the last open para 
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