class Solution:
    def isPalindrome(self, s: str) -> bool:
        # function checks if char is alpha numeric
        def is_alnum(c: str) -> bool:
            return (
                     (ord("A") <= ord(c) <= ord("Z")) or 
                    (ord('a') <= ord(c) <= ord("z")) or 
                    (ord('0') <= ord(c) <= ord('9'))
                    )
        
        # initalize two pointers
        l, r = 0, len(s)-1

        while l < r:
            # skip all non alphanum chars from both sides
            while l < r and not is_alnum(s[l]):
                l += 1
            while l < r and not is_alnum(s[r]):
                r -= 1
            # check both sides
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        # passes all checks -> valid palindrome
        return True