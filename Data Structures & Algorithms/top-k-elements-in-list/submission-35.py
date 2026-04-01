class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap {num -> freq}
        # bucket sort array is [i=freq and elems=[nums of that freq]] in ascending frequency
        freq_map = {}
        # initalized buckets
        freq_buckets = [[] for i in range(len(nums)+1)]

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        # key, value in dict.items()
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        res = []
        # iterate from most frequenct bucket to least (l <- r)
        # per bucket
        for i in range(len(freq_buckets)-1, 0, -1):
            # per num in bucket
            for num in freq_buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
                
                



        
        