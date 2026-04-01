class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        # overall loop 
        while l < r:
            # skip all non alphanumeric chars from the left side and right side
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare the two chars 
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        