class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap {key=num : val=num_freq}
        freq_map = {}
        # initalize freq_buckets [i=freq of elems, val=[nums of freq]]
        freq_buckets = [[] for i in range(len(nums) + 1)]

        # populate hashmap 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets 
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # iterate from the last bucket (most frequent num)
        res = []
        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

