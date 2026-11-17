class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # init a set of nums and var to track longest consec. sequence
        numSet = set(nums)
        res = 0 

        # iter over each number 
        for n in nums:
            # check if that number is the start of a sequence
            # numbers (that do not a left neighbor) are the start of the sequence
            if (n-1) not in numSet:
                seq_length = 0 
                # update seq_length as we see more consecutive numbers
                while (n+seq_length) in numSet:
                    seq_length += 1
                # update res variable
                res = max(res, seq_length)
        
        return res

