class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize left and right pointers
        l, r = 0, len(s)-1

        while l < r:
            # if the left char is not alnum skip until we find an alnum and likewise for right
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # check the two pointers
            if s[l].lower() != s[r].lower():
                return False
            # increment pointers after checking them
            l, r = l+1, r-1
        
        return True
