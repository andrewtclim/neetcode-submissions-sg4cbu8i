class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack and hashmap 
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            # closed case
            if p in closeToOpen:
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        return True if not stack else False