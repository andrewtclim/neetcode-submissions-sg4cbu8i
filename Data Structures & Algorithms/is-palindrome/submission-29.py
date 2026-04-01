class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initalize two pointers
        l, r = 0, len(s)-1

        # function that checks if a char is alpha num
        def is_alphanum(c):
            return (ord("A") <= ord(c) <= ord("Z") or 
                    ord("0") <= ord(c) <= ord("9") or
                    ord("a") <= ord(c) <= ord("z")
                    )
        
        while l < r:
            # skip over all non alpha num chars
            while l < r and not is_alphanum(s[l]):
                l += 1
            while l < r and not is_alphanum(s[r]):
                r -= 1
            # check both sides
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True