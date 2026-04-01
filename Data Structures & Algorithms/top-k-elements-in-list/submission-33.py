class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize count map {nums : freq} 
        # initalize bucket sort arr [i=freq and elem=[nums w/ freq]]
        count_map = {}
        freq_arr = [[] for i in range(len(nums)+1)]

        # populate hashmap 
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate buckets
        for num, freq in count_map.items():
            freq_arr[freq].append(num)
        
        # return the last k elems from freq_arr
        res = []
        # per bucket
        for i in range(len(freq_arr)-1, 0, -1):
            # per num in each bucket
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res