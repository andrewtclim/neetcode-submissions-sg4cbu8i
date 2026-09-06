class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ensure same length 
        if len(s) != len(t):
            return False
        
        # init shared char count
        count = [0] * 26 

        # iter over shared index 
        for i in range(len(s)):
            # count up for s's chars
            count[ord(s[i]) - ord('a')] += 1
            # count down for t's chars 
            count[ord(t[i]) - ord('a')] -= 1 
        
        return all(c == 0 for c in count)