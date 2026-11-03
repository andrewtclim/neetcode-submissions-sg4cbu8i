class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = [0]*26, [0]*26

        # populate count code maps 
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1
        
        if count_s1 == count_s2:
            return True
        
        # init l and r pointers (sliding window over s2)
        l = 0 
        for r in range(len(s1), len(s2)):
            # add the right char, subtract left pointer
            count_s2[ord(s2[r]) - ord('a')] += 1
            count_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if count_s1 == count_s2:
                return True
        
        return False
