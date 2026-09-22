class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Two data struc. are required
        1) A hashmap that counts the frequency of the nums {num:freq}
        2) An array where the i=freq and val=List[nums of that freq]
        by doing so we can arrange the freq from least_freq -> most_freq
        """
        freq_map = {}
        freq_buckets = [[] for i in range(len(nums)+1)] # starts at freq 0 to most freq (all nums same)

        # populate freq map
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # organize nums in their freq_buckets
        for num, freq in freq_map.items():
            freq_buckets[freq].append(num)
        
        # go from most freq to least (append to res)
        res = []
        for i in range(len(freq_buckets)-1, -1, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
                    