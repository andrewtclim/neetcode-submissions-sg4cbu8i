class Solution:
    def isValid(self, s: str) -> bool:
        # initalize a hashmap that stores {closed : open}
        closeToOpen = {"}":"{", "]":"[", ")":"("}
        stack = []

        # iterate over para
        for p in s:
            # close case
            if p in closeToOpen:
                # check validity (not before an open para, also matches the last openning para)
                if stack and closeToOpen[p] == stack[-1]:
                    # pop off the last open para
                    stack.pop()
                # otherwise -> invalid
                else:
                    return False
            # add any open para
            else:
                stack.append(p)
        
        # stack processed -> valid 
        if not stack:
            return True
        else:
            return False
