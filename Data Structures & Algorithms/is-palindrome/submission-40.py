class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init two pointer indices
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alnum values (left)
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare the two chars 
            if s[l].lower() == s[r].lower():
                # valid pair and skip to next chars
                l += 1
                r -= 1
            # invalid pairs -> not a palindrome
            else:
                return False
        
        # passes loop then valid
        return True