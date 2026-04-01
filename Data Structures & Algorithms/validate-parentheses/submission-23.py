class Solution:
    def isValid(self, s: str) -> bool:
        # initalize hashmap {close -> open}
        # initalize stack -> keeps all open para
        closeToOpen = {")":"(",
                        "]":"[",
                        "}":"{"}
        stack = []

        for p in s:
            # closed case
            if p in closeToOpen:
                # closed para must 1. stack must have an open 2. match with the last open para
                if stack and closeToOpen[p] == stack[-1]:
                    stack.pop()
                else:
                # if it does not meet 2 conditions it is invalid
                    return False
            # open case
            else:
                stack.append(p)
        
        # stack all processed -> valid
        if not stack:
            return True
        else:
            return False