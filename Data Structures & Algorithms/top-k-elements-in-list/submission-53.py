class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # two data structures are needed (hashmap for counting elem freq) and 
        # (arr of buckets to organize frequency in terms of least to most)

        freq_map = {}
        freq_buckets = [[] for i in range(len(nums)+1)] # starts with 0 freq to most frequent 

        # populate hashmap 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # organize nums into their buckets (i=freq_bucket, val=nums of that freq)
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        res = []
        # iter from most freq to least 
        for i in range(len(freq_buckets)-1, 0, -1):
            # from this bucket 
            for num in freq_buckets[i]:
                res.append(num)
                # found k-th elems
                if len(res) == k:
                    return res
