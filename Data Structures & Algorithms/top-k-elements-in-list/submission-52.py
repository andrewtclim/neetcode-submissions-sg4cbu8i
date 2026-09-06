class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create {elem : freq} hashmap 
        freq_map = Counter(nums)
        # init freq_buckets where i=frequency and val=[nums of that freq]
        freq_buckets = [[] for i in range(len(nums)+1)]

        # populate buckets
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # iter over buckets from most freq to least 
        res = []
        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        
        