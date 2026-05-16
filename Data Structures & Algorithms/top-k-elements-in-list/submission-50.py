class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init freq_map to count frequency of nums
        # init buckets to store nums of that freq (i=freq)
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets 
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        res = []
        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res