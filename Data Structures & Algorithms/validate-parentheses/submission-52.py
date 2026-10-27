class Solution:
    def isValid(self, s: str) -> bool:
        # ex) "[[()]]" or "(((())))" is valid 
        # so the stack holds all of the open para it sees in order
        # ex) "[[(" then processes the matching closing para in order ")]]"
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for p in s:
            # closed case
            if p in closeToOpen:
                # valid match -> pop from stack 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                # invalid closed para found 
                else:
                    return False
            # open case
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False