class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Utilize a hashset to check the numbers next value
        Start of sequences are numbers where their left neighbor DNE
        '''
        num_set = set(nums)
        res = 0 

        for n in nums:
            # check start of sequence
            if (n-1) not in num_set:
                # init the start of a sequence
                length = 1
                # record how long this sequence is
                while (n+length) in num_set:
                    length += 1
                
                # record this sequence length in result
                res = max(res, length)
        
        return res
