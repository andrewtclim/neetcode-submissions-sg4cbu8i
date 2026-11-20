class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # init hashmaps for each string {char : freq}
        count_s, count_t = {}, {}

        # ensure the length of strings are equal 
        if len(s) != len(t):
            return False 
        
        # populate the hashmaps 
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        
        # compare the hashmaps 
        return count_s == count_t