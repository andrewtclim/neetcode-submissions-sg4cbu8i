class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            # calculate comp of target
            comp = target - nums[i]
            # seen complement -> found answer 
            if comp in seen:
                return [seen[comp], i]
            # populate hashmap
            seen[n] = i 
        