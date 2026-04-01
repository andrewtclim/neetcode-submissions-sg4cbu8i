class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init use two pointers 
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alphanumeric (left and right side)
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # see if the two match 
            if s[l].lower() != s[r].lower():
                return False
            # update pointers 
            l += 1 
            r -= 1
        
        return True
            