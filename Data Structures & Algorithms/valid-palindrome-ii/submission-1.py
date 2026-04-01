class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initalize pointers
        l, r = 0, len(s)-1

        while l < r:
            # different letter case
            if s[l] != s[r]:
                # subarr without s[l]
                skipL = s[l+1:r+1]
                # subarr without s[r]
                skipR = s[l:r]
                
                # check both cases
                # if one case works (eliminating one letter -> Valid)
                if (skipL == skipL[::-1] or skipR == skipR[::-1]):
                    return True
                # if neither case works -> invalid palindrome w/ elimination
                else:
                    return False
            
            # slide pointers
            l, r = l+1, r-1
        
        return True
        