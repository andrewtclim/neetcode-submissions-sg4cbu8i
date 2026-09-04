class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init a hashmap for {num : freq}
        # init a bucket array s.t. [ i = freq and elems = values with that freq]
        freq_map = {}
        # first bucket is 0th freq, last bucket is most freq (all elems are of that value)
        freq_buckets = [[] for i in range(len(nums) + 1)] 

        # populate occurance map 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets 
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # iterate over the buckets in reverse order
        res = []
        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res