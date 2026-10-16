class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first check the inital substr window of len(s1)
        if len(s1) > len(s2):
            return False

        code_s1, code_s2 = [0]*26, [0]*26

        for i in range(len(s1)):
            code_s1[ord(s1[i]) - ord('a')] += 1
            code_s2[ord(s2[i]) - ord('a')] += 1
        
        if code_s1 == code_s2:
            return True
        
        # l is lagging pointer
        # r is the current pointer
        l = 0 
        for r in range(len(s1), len(s2)):
            code_s2[ord(s2[r]) - ord('a')] += 1
            code_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if code_s1 == code_s2:
                return True
        
        return False