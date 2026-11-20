class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init {num : freq} hashmap 
        # bucket array s.t. the i=freq and elems=[nums of that freq]
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        for n, freq in freq_map.items():
            freq_buckets[freq].append(n)
        
        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res