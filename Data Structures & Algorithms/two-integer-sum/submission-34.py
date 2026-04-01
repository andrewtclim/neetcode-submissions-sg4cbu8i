class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initalize hashmap {num -> index}
        seen = {}

        for i, num in enumerate(nums):
            # calculate a complement for current number 
            comp = target - num # num + comp (if it exists in hashmap) = target
            if comp in seen:
                return [seen[comp], i]
            seen[num] = i
        
        return -1