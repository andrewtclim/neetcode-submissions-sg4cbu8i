class Solution:
    def isValid(self, s: str) -> bool:
        # init hashmap closeToOpen and running stack
        # NOTE: Stack will keep only open para
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        stack = []

        for p in s:
            # closed case
            if p in closeToOpen:
                # valid case
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        # at the end if all our stack has been processed -> valid para
        if not stack:
            return True
        else:
            return False

