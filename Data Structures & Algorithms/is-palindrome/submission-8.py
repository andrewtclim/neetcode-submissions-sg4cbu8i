class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers 
        l, r = 0, len(s)-1

        while l < r:
            # skip over elements that are not alnum
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare alnum letters from either side (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # update pointers to next position 
            l, r = l+1, r-1 
        
        # passes all checks
        return True