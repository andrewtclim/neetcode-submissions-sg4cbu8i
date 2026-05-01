class Solution:
    def isValid(self, s: str) -> bool:
        # init hashmap {close : open}
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        stack = []

        for p in s:
            # p is closed 
            if p in closeToOpen:
                # matches eliminate matching open para
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # p is open
            else:
                stack.append(p)
        
        # if all the paranthese have been processed -> return True
        if not stack:
            return True
        else:
            return False