class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init two pointers 
        l, r = 0, len(s)-1

        while l < r:
            # skip all nonalphanum characters (both left and right sides)
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # compare 
            if s[l].lower() == s[r].lower():
                # match? go to next pair 
                l += 1
                r -= 1
            else:
                return False 
        
        return True