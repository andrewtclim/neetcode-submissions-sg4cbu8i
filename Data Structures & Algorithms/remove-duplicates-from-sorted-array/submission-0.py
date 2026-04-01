class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initalize pointer (l = placeholder for next unique number)
        l = 1

        # r = constant pointer, finds unique numbers and stops at end of arr
        for r in range(1, len(nums)):
            # found a unique number
            if nums[r] != nums[r-1]:
                # update first part of array (where l-pointer is)
                nums[l] = nums[r]
                # update unique placeholder
                l += 1
        
        # l will count the number of unique numbers in the array
        return l


