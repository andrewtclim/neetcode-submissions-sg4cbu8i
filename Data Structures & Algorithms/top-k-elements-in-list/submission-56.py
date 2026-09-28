class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap that counts the num : freq 
        # arr where i=freq and [nums with freq]
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # populate our freq_map 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets according to the nums frequency
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # iterate over freq_bucket backwards (most freq to least)
        res = []
        # iter over the buckets
        for i in range(len(freq_buckets)-1, -1, -1):
            # iter over the numbers in that bucket
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res