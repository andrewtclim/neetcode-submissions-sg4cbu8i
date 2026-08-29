class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmaps to count char occurences of each string
        # key : value pairs are char : occurences
        s_counter, t_counter = {}, {}

        # anagrams must have the same length 
        if len(s) != len(t):
            return False

        # iter over one index
        for i in range(len(s)):
            # populate the occurences 
            s_counter[s[i]] = s_counter.get(s[i], 0) + 1
            t_counter[t[i]] = t_counter.get(t[i], 0) + 1

        return t_counter == s_counter 