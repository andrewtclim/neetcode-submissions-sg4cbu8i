class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize a hashmap [num -> index]
        seen = {}

        for i, n in enumerate(nums):
            comp = target - n 
            # if we find the complement (return index of comp and current index)
            if comp in seen:
                return [seen[comp], i]
            # populate hashmap
            seen[n] = i

        