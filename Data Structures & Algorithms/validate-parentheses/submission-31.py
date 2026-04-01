class Solution:
    def isValid(self, s: str) -> bool:
        # init hashmap key=close para and val=open para
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []
        # RULES: stack will only keep open paras, if we see a matching para then pop 
        for p in s:
            # closed case 
            if p in closeToOpen:
                # invalid if stack is empty (closed p before an open)
                # or the last open para doesnt match 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()  
                else:
                    return False
            # open case 
            else:
                stack.append(p)
        
        if not stack:
            return True 
        else:
            return False