class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initalize pointers
        l , r = 0, len(s)-1

        # slide until pointers meet (if they do all match -> return True (end of loop))
        while l < r:
            # different letter case
            if s[l] != s[r]:
                # sub arrays to check the left and right sides
                # checking left side means 
                # if we eliminated letter at r, would we get a palindrome? and vice versa 
                R_side = s[l+1:r+1]
                L_side = s[l:r]

                return (R_side == R_side[::-1] or L_side == L_side[::-1])
            # matching letter case
            l, r = l+1, r-1
        
        return True

        