class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        while l < r:
            # found a non alpha num value on the left side (increase until we find alnum value)
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            # compare left and right chars 
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l, r = l+1, r-1
        
        # at the end of the loop (when l=r or l goes past r)
        # if all the l,r values are equal we have a palindrome
        return True
        