class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Use a hashset of the input array (checks membership in O(1) time)
        Seperate our input array into seperate consecutive sequence chunks (visualize in num. line)
        A number is the start of a sequence if it's n-1 value is not in the input
        After we identify the start of a sequence, add to length any consecutive number we see
        Update our result variable after each sequence 
        '''
        nums_set = set(nums)
        res = 0 # track longest sequnce length 

        # iter over each number
        for n in nums:
            # locate the start of a sequence
            if (n-1) not in nums_set:
                # init the length of this sequence
                length = 1
                # update the length with each consecutive number we see
                while (n+length) in nums_set:
                    length += 1
            
                # update res with sequence lengths
                res = max(res, length)
        
        return res

