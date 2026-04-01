class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initalize position for next unique number
        l = 1

        for r in range(1, len(nums)):
            # unique case
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l