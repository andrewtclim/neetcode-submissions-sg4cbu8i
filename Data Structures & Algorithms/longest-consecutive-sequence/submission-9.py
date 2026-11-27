class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0 # var to track longest consecutive seq length 

        for num in nums:
            # check if its the start of a seq
            if (num-1) not in num_set:
                length = 1 # init sequence length 

                while (num+length) in num_set:
                    length += 1

                res = max(res, length)
        
        return res