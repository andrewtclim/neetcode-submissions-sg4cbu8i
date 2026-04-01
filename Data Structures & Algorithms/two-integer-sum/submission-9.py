class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap (key = num, value = index)
        seen = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [seen[comp], i]
            seen[n] = i
        
        