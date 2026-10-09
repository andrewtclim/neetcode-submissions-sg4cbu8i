class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init two pointer
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alphanum chars from left (then right)
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare l and r chars
            if s[l].lower() != s[r].lower():
                return False
            # otherwise skip to next chars 
            l += 1
            r -= 1
        
        return True