class Solution:
    def isPalindrome(self, s: str) -> bool:
        # init two pointers 
        l, r = 0, len(s)-1

        # iter over chars
        while l < r:
            # skip over any non alnum chars from left and right sides 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # if the two elems match (continue to next pair)
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        # passes checks -> palindrome 
        return True
