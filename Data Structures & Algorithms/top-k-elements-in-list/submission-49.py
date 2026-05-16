class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init counter map {num : freq}
        freq_map = {}
        # frequency buckets i=freq and buckets[i] store the nums of that freq
        buckets = [[] for i in range(len(nums) + 1)]

        # populate freq_map
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate buckets 
        # iter over (num, freq) pairs in hashmap
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        # populate arr with most frequent items 
        res = []
        for i in range(len(buckets)-1, -1, -1):
            # iter over every num in that frequency 
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

