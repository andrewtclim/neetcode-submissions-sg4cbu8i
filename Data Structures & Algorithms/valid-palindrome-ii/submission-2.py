class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initalize pointers
        l, r = 0, len(s)-1

        while l <= r:
            # unmatched letters (use one elimination)
            if s[l] != s[r]:
                # check subarrays
                skipL = s[l+1:r+1]
                skipR = s[l:r]

                return (skipL==skipL[::-1] or skipR==skipR[::-1])
            # update pointers
            l = l + 1
            r = r - 1
        
        # if it passes the loop (all chars match)
        return True