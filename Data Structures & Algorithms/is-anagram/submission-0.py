class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmaps for both strings key=char and val=occur
        count_s, count_t = {}, {}

        # anagrams must be same length (ensures loop over one index)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # update hashmaps 
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        return count_s == count_t