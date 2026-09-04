class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initalize two hashmaps for counters
        counter_s, counter_t = {}, {}

        # ensure same length 
        if len(s) != len(t):
            return False
        
        # populate hashmaps with char occurences
        for i in range(len(s)):
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1
            counter_t[t[i]] = counter_t.get(t[i], 0) + 1
        
        return counter_s == counter_t