class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        code = [0]*26

        if len(s) != len(t):
            return False
        
        for cs, ct in zip(s, t):
            code[ord(cs) - ord('a')] += 1
            code[ord(ct) - ord('a')] -= 1
        
        return all(c == 0 for c in code)