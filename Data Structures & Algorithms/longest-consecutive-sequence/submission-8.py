class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0 

        for num in nums:
            # check start of sequence (consider these sequences)
            if (num-1) not in nums_set:
                # init the start of sequence
                length = 1

                # check how long the sequence is
                while (num+length) in nums_set:
                    length += 1
                
                # update the res variable with the lengths
                res = max(res, length)
        
        return res
                
