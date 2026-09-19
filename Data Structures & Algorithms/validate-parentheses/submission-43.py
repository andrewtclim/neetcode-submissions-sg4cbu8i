class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {"}":"{", "]":"[", ")":"("}

        for p in s:
            # closed case
            if p in closeToOpen:
                # valid cases (already open and matches)
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
            
            