class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes Algorithim
        # Record the sum if its positive, otherwise reset the sum to zero

        maxSum = nums[0]
        curSum = 0

        if len(nums) == 1:
            return maxSum

        for num in nums:
            # reset negative sums to 0
            if curSum < 0: 
                curSum = 0 
            curSum += num 
            # record and update the maxSum 
            maxSum = max(maxSum, curSum)
        
        return maxSum 
