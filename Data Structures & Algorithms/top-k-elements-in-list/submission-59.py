class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init a hashmap to track {num : freq}
        # init a bucket array [i=freq and [nums of that freq]]
        freq_map = {}

        # sublist for every possible freq
        freq_buckets = [[] for i in range(len(nums) + 1)] 

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)

        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            # iter over frequencies from most to least
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
