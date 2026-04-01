class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        while l < r:
            # skip over all non alpha num chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l, r = l+1, r-1
        
        # valid palindrome if it passes all tests 
        return True
            