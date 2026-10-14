class Solution:
    def isValid(self, s: str) -> bool:
        # init hashmap and stack 
        closeToOpen = {"}" : "{",
                        "]" : "[",
                        ")" : "("
                        }
        stack = []

        for p in s:
            # closed case 
            if p in closeToOpen:
                # check if its valid 
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            # open case -> always add to top of stack
            else:
                stack.append(p)

        if not stack:
            return True
        else:
            return False