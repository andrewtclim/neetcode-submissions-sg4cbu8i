class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1 # position of next unique num

        for r in range(1, len(nums)):
            # found unique num -> update nums[l] and l
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        # l = the number of unique nums
        return l
