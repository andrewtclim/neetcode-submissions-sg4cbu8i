class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # initalize pointers (l = position of next non-val number)
        l = 0

        for i in range(len(nums)):
            # when we find a non-val number change the first half of the array
            if nums[i] != val:
                nums[l] = nums[i]
                l += 1
        
        # l is also equal to the number of non-val numbers
        # since l is only updated when we see non-val numbers
        return l 
