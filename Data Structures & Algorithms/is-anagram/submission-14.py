class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmaps to track {char : freq}
        counterS, counterT = {}, {}

        # ensure same length 
        if len(s) != len(t):
            return False

        # populate the hashmaps 
        for i in range(len(s)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1
        
        return counterS == counterT