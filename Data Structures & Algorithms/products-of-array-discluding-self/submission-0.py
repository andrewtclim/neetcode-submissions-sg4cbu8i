class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 

        for i in range(n):
            prod = 1 # running prod of arr (except itself)
            for j in range(n):
                # if it is itself (skip)
                if i == j:
                    continue
                # otherwise multiply to the runnig product
                prod *= nums[j]
            # update res array 
            res[i] = prod
        return res