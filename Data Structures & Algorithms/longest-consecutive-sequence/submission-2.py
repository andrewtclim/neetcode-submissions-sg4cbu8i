class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        NOTE: Its helpful to put the numbers on a numberline and see how many
        sequences exisits in our array.

        Then realize that we really only have to consider the start of each sequence

        For example [100, 4, 200, 1, 2, 3, 101] when sorted into sequences is
        [1,2,3] then [100, 101] then [200]

        We check for the start of sequences by asking if its left neightbor (n-1) exists
        ex: For the num 100, we do not see 99 -> so it is a start of a seq

        Then for each sequence, we see how many consecutive nums exists
        Since checking values in hashsets only take O(1), 
        
        Then update your res variable after each sequence is populated
        '''

        # init a set of nums and var to track longest consec. sequence
        numSet = set(nums)
        res = 0 

        # iter over each number 
        for n in nums:
            # check if that number is the start of a sequence
            # numbers (that do not a left neighbor) are the start of the sequence
            if (n-1) not in numSet:
                # init the sequence tracker 
                seq_length = 0 
                # update seq_length as we see more consecutive numbers
                while (n+seq_length) in numSet:
                    seq_length += 1
                # update res variable
                res = max(res, seq_length)
        
        return res

