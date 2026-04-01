class Solution:
    def isValid(self, s: str) -> bool:
        # initalize stack and hashmap 
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        
        # iterate through para
        for p in s:
            # process closed para
            if p in closeToOpen:
                # stack must have a prior matching open 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # process open para        
            else:
                stack.append(p)
        
        # if the stack is processed (empty) -> valid parantheses
        if not stack:
            return True
        else:
            return False
        