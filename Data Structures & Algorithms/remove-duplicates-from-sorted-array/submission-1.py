class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initalize the pointer (l=next unique num)
        l = 1

        # iterate from (r = 1 to end of array)
        for r in range(1, len(nums)):
            # unique case
            if nums[r] != nums[r-1]:
                # found a unique number
                nums[l] = nums[r]
                l += 1

        return l 