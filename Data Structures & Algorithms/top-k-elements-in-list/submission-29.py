class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initalize counter hashmap and bucket_sort array 
        count_map = {}
        freq_arr = [[] for i in range(len(nums)+1)]

        # populate count_map [num -> freq]
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # populate buckets in freq_arr
        for num, freq in count_map.items():
            freq_arr[freq].append(num)

        # return the last k values 
        # freq_arr is sorted from least -> most frequent
        res = []       
        for i in range(len(freq_arr)-1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res