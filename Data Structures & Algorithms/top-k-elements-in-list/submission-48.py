class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init a hashmap to count freq of nums 
        freq_map = {}
        # init a bucket to store the nums of that freq 
        freq_buckets = [[] for i in range(len(nums)+1)]

        # populate freq_map 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # populate buckets (i=freq and the bucket[i] stores nums of that freq)
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)

        res = []
        # iterate over buckets from right to left (most freq -> least freq)
        for i in range(len(freq_buckets)-1, 0, -1):
            # iter over each num in that bucket 
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            