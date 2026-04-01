class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # init hashmap that tracks numbers we've seen
        # seen {num : index}
        seen = {}

        for i, n in enumerate(nums):
            # calc it's complement 
            comp = target - n
            if comp in seen:
                # return complements index and curr i
                return [seen[comp], i]
            # populate hashmap 
            seen[n] = i
        