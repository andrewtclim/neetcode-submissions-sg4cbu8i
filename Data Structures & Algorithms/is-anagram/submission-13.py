class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check lengths 
        if len(s) != len(t):
            return False
        
        count = [0] * 26 

        for cs, ct in zip(s,t):
            # +1 for chars in s 
            count[ord(cs) - ord('a')] += 1
            # -1 for chars in t 
            count[ord(ct) - ord('a')] -= 1
        
        return all(c == 0 for c in count)