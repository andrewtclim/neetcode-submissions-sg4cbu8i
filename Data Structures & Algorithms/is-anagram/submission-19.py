class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26 

        for cs, ct in zip(s, t):
            # add values for cs
            count[ord(cs) - ord('a')] += 1
            # decrement value for ct
            count[ord(ct) - ord('a')] -= 1
        
        return all(c == 0 for c in count)