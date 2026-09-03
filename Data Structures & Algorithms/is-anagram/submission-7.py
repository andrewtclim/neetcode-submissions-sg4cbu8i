class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initalize hashmaps {char : occurences}
        count_s, count_t = {}, {}

        # anagrams must be the same length 
        if len(s) != len(t):
            return False
        
        # ensuring that our strings have the same length 
        # allows us to iter over just one strings index
        for i in range(len(s)):
            # populate our hashmaps 
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        # compare the two hashmaps (hashmaps arent ordered so we can directly compare the two)
        return count_s == count_t