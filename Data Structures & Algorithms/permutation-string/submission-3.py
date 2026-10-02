class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Here s2_count is our current windows char code
        This iteratively gets updated as we go through the array

        LOGIC:
        First check that s1 can be a substr of s2
        Init and populate char codes for s1, s2
        Then check that the first window of s1 and s2 
        Next iter from the end of first window to end of s2 and 
        update/check s2_count to s1 count
        '''

        # first check that s1 can be a substr of s2
        if len(s1) > len(s2):
            return False

        # init count codes for both strings 
        s1_count = [0] * 26
        s2_count = [0] * 26

        # populate the count codes for s1 and first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # if the first substr is a matching anagram -> return True
        if s1_count == s2_count:
            return True

        # iterate from the end of first substr -> end of s2
        for r in range(len(s1), len(s2)):
            # update current substr char code (add right then subtract left)
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[r - len(s1)]) - ord('a')] -= 1

            # substr freq matches the current freq then return True
            if s2_count == s1_count:
                return True

        # otherwise we looped through the whole string -> 
        # no valid permutations found in window
        return False
            