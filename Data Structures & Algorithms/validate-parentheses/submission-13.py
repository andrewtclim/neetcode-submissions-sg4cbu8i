class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack and hashmap 
        stack = [] 
        closeToOpen = {"]":"[", ")":"(", "}":"{"}

        # iterate para
        for p in s:
            # closed case
            if p in closeToOpen:
                # stack must have prev open para and must match to process
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        # stack will be empty -> Valid
        if not stack:
            return True
        else:
            return False
        