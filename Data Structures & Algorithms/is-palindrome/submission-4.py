class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l<r:
            # if we see a non alphanum element, skip it
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            # the two chars from opposite ends in a palindrome will be equal
            if s[l].lower() != s[r].lower():
                return False
            # increment pointers
            l,r = l+1, r-1
        return True
            
        