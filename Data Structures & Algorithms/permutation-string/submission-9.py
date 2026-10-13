class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        # char codes for both 
        count_s1, count_s2 = [0]*26, [0]*26

        # populate inital substring length of s1
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        # compare first substr window
        if count_s1 == count_s2:
            return True
        
        # check all other windows (start at the end of first substr window)
        l = 0 
        for r in range(len(s1), len(s2)):
            count_s2[ord(s2[r]) - ord('a')] += 1
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if count_s1 == count_s2:
                return True
        
        return False