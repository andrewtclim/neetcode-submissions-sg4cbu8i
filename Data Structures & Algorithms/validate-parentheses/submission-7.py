class Solution:
    def isValid(self, s: str) -> bool:
        # initalize a stack (FILO)
        # a hashmap that maps closed -> open
        stack = []
        closeToOpen = {")": "(", "]" : "[", "}" : "{"}

        for p in s:
            # process closed parantheses 
            if stack and p in closeToOpen:
                # matches the last open para -> remove last
                if closeToOpen[p] == stack[-1]:
                    stack.pop()
                # doesnt match -> invalid
                else:
                    return False
            # process open parantheses
            # the stack will contain all open parantheses 
            else:
                stack.append(p)
        
        # if the stack is empty -> all valid otherwise invalid
        if not stack:
            return True
        else:
            return False
        