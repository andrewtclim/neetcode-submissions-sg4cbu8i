class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init a hashmap for each num freq
        # arr to store the chars with associated freqs
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num) # access freq key and append num of that freq
        
        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        