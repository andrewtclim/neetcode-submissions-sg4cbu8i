class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        LOGIC: First check the length of s1 < s2
        then use a char code [0]*26 arr to check char freq 
        check the first substr length of s1
        then iterate over the other chars from s1 to end of s2
        '''
        if len(s1) > len(s2):
            return False
        
        # init char codes
        code_s1 = [0] * 26
        code_s2 = [0] * 26

        # populate char codes for s1 and s2 (inital substring window of len(s1))
        for i in range(len(s1)):
            code_s1[ord(s1[i]) - ord('a')] += 1
            code_s2[ord(s2[i]) - ord('a')] += 1
        
        if code_s1 == code_s2:
            return True

        l = 0 
        for r in range(len(s1), len(s2)):
            # update and check (keep updating from code_s2: dynamic substring)
            code_s2[ord(s2[r]) - ord('a')] += 1
            code_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1

            if code_s1 == code_s2:
                return True

        # no matches found then
        return False