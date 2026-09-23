class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes Algorithim
        # reset the running sum to zero whenever it's gone negative
        # then always add the current number and check for a new max

        maxSum = nums[0]
        curSum = 0

        for num in nums:
            # reset negative sums to 0
            if curSum < 0: 
                curSum = 0 
            curSum += num 
            # record and update the maxSum 
            maxSum = max(maxSum, curSum)
        
        return maxSum 
