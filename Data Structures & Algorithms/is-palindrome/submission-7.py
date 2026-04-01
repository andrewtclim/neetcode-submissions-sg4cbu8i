class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers 
        l, r = 0, len(s)-1

        while r > l:
            
            # skip over any non-alpha numeric characters 
            while r>l and not s[l].isalnum():
                l += 1
            while r>l and not s[r].isalnum():
                r -= 1
            
            # compare the two chars from both ends (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            
            # increment pointers
            l, r = l+1, r-1
        
        # passes all conditions then
        return True
            