class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap for counting num and freq {num -> freq}
        # initalize a bucket sort arr where index=freq and element=[num w/ freq]
        freq_map = {}
        freq_list = [[] for i in range(len(nums)+1)] # index starts at 0 to len(nums) (aka most frequent number possible)

        # populate hashmap
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        # populate buckets in bucket sort arr
        for n, freq in freq_map.items():
            freq_list[freq].append(n)
        
        # iterate from most freq -> least freq until u reach k-elements
        res = []
        # each bucket
        for i in range(len(freq_list)-1, 0, -1):
            # each num in that bucket    
            for num in freq_list[i]:
                res.append(num)
                if len(res)==k:
                    return res


