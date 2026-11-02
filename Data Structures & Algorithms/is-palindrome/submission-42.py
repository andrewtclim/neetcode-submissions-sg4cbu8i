class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init pointers on both sides
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alphanum from left side (then right)
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            # compare s[l] and s[r]
            if s[l].lower() != s[r].lower():
                return False
            # slide pointers
            l += 1
            r -= 1
        
        # pass checks -> valid
        return True