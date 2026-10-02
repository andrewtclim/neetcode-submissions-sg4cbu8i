class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is the substring within s2

        # freq_map of s1 chars
        s1_freq_map = Counter(s1)

        # helper function to determine if substr is an anagram of s1
        def checkSubstring(substr):
            return Counter(substr) == s1_freq_map

        # substring must be size of s1
        N = len(s1)
        l = 0
        for r in range(0, len(s2)):
            # isolate substring 
            substr = s2[l:r+N]
            # check if substring is anagram 
            if checkSubstring(substr):
                return True
            else:
                # otherwise slide the window
                l += 1
        
        return False



