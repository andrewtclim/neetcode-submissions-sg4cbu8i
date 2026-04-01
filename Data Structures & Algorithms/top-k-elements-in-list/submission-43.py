class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init count map Dict{num : freq}
        freq_map = {}
        # init buckets for each freq List[[nums of least_freq]... [nums of most_freq]]
        freq_list = [[] for i in range(len(nums) + 1)]

        # populate our freq_map 
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # populate the freq_list buckets 
        for num, freq in freq_map.items():
            freq_list[freq].append(num)

        # take the last k items of freq_list (the k most frequent)
        res = []
        # reverse indexing over freq_list index
        for i in range(len(freq_list)-1, 0 , -1):
            # iterate over nums in the bucket
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res 
            

