class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first ensure same length 
        if len(s) != len(t):
            return False
        # init a char_code -> tracks occurence of chars
        char_code = [0] * 26 

        # use zip() to create an iter of tuple pairs from s and t
        for cs, ct in zip(s, t):
            # +1 for each char from s
            char_code[ord(cs) - ord('a')] += 1
            # -1 for each char from t 
            char_code[ord(ct) - ord('a')] -= 1
        
        # if the char_code is all 0's -> s and t had the same chars
        return all(c == 0 for c in char_code)