class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        LOGIC: Consider the starts of any consecutive sequence (n-1) DNE
        For each potential seq, log its length
        '''

        num_set = set(nums)
        res = 0 # track longest sequence length so far

        for n in nums:
            # start of sequence 
            if (n-1) not in num_set:
                # start the sequence 
                length = 1

                # log the sequence length 
                while (n+length) in num_set:
                    length += 1
                
                # update the res variable 
                res = max(res, length)
        
        return res

