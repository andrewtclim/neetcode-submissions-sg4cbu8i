class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmap {char:freq}
        count_s, count_t = {}, {}

        if len(s) != len(t):
            return False
        
        # iter over one index
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        return count_s == count_t