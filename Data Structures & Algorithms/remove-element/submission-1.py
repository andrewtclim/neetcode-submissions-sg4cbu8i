class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initalize pointer (position of the next non-val number)
        l = 0

        for i in range(len(nums)):
            # non-val case
            if nums[i] != val:
                # update the first half of nums
                nums[l] = nums[i]
                l += 1
        
        # l will be equal to the number of non-val nums we have seen 
        return l