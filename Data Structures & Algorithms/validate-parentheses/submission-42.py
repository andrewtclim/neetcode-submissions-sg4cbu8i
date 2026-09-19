class Solution:
    def isValid(self, s: str) -> bool:
        # have a stack that contains only open para 
        stack = []

        closeToOpen = { "}" : "{",
                        "]" : "[",
                        ")" : "("
        }

        for p in s:
            # closed case
            if p in closeToOpen:
                # if stack is empty (a closed para came first -> invalid)
                if not stack:
                    return False
                elif stack[-1] == closeToOpen[p]:
                    # process this open para
                    stack.pop()
                # otherwise this closed para did not match
                else:
                    return False
            # open case -> always append open para
            else:
                stack.append(p)
        
        if not stack:
            return True
        else:
            return False

