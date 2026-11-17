class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        For each number, only start counting if it's the beginning of a sequence
        (its left neighbor n-1 isn't in the set). Then walk forward counting
        consecutive numbers. Each number is visited at most twice total
        (once in the outer loop, once by an inner walk), so O(n).

        Example: [100, 4, 200, 1, 2, 3, 101]
          Sequences: [1, 2, 3], [100, 101], [200]
          Starts (no left neighbor): 1, 100, 200
          Longest: 3
        '''
        num_set = set(nums)
        res = 0

        for n in num_set:
            # start of a sequence found
            if n - 1 not in num_set:
                # init the seq length as 1
                length = 1
                # check for consecutive nums and update seq length
                while n + length in num_set:
                    length += 1
                # update the res variable after this sequence length was found
                res = max(res, length)

        return res