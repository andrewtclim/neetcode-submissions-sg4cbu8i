class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # two ds required
        # hashmap for {num : freq} 
        # arr for freq_buckets [i=frequency and [nums of that freq]]
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # append nums to each bucket 
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # iter from buckets from most freq to least 
        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res