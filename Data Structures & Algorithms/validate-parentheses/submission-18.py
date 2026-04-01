class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for p in s:
            # closed case
            if p in closeToOpen:
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    # either a closed para came before its corresponding open OR the para do not match
                    return False
            # open case
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False