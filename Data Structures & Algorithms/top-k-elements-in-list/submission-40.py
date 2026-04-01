class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize a hashmap {num : freq_of_num} and bucket sort arr [i=freq and val=[nums of freq]]
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums)+1)] # the last index should be the length of elems in nums

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        res = []
        # through each bucket from most frequent to least 
        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res