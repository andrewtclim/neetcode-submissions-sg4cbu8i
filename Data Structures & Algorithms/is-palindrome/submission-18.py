class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        # one from the left and one from the right side
        l, r = 0, len(s)-1

        while r > l:
            # skip over any non alnum chars
            while r > l and not s[r].isalnum():
                r -= 1
            while r > l and not s[l].isalnum():
                l += 1 
            # compare the two chars
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l , r = l+1, r-1
        
        return True
            
        