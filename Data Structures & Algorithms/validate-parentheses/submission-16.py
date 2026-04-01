class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack and hashmap (closed : open)
        stack = []
        closeToOpen = {")":"(", "]":"[", "}": "{"}

        for p in s:
            # closed case
            if p in closeToOpen:
                # an open para comes before closed and this closed para must match the last open para
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        # if the stack is processed -> Valid
        if not stack:
            return True
        else:
            return False