class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alnum elements
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare chars from each end
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l += 1
            r -= 1
        
        return True
        