class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initalize pointer (next unique num)
        l = 1

        # iterate over nums (r=current pointer, start from r=1 -> end)
        for r in range(1, len(nums)):
            # unique case 
            if nums[r] != nums[r-1]:
                # update left (all unqiue nums) and pointer
                nums[l] = nums[r]
                l += 1
        
        return l