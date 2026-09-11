class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using zip() and all() methods with char count array 
        # ensure same length 
        if len(s) != len(t):
            return False
        
        count = [0] * 26 

        for cs, ct in zip(s, t):
            # +1 values for chars in s 
            count[ord(cs) - ord('a')] += 1
            # -1 values for chars in t 
            count[ord(ct) - ord('a')] -= 1
        
        # if char count is all 0's the chars in bothe strings match 
        return all(c == 0 for c in count)