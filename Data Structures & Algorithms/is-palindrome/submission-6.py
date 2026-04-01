class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        # check pointers until they meet 
        while r > l:
            # if left char is not alnum, skip until we find the alnum char
            while r > l and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            # check the opposing two chars (case insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # update pointers to next positions
            l, r = l+1, r-1

        return True 
