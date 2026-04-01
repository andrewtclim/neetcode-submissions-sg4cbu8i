class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize pointers
        l, r = 0, len(s)-1

        while l < r:
            # skip over all non alpha num chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # check both ends
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l, r = l+1, r-1
        
        # passes loop succesfully -> valid palindrome
        return True
        