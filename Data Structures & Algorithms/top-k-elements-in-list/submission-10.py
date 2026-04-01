class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize hashmap for nums and freq
        # initalize freq_list : a bucket sort of nums (i = freq and elems = [nums w/ freq])
        count_map = {}
        freq_list = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
        
        # populate bucket sort list
        for num, freq in count_map.items():
            freq_list[freq].append(num)
        
        # find and return the last k-elements from freq_list
        res = []
        for i in range(len(freq_list)-1, 0, -1):
            # iterate over each num in each bucket
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
        