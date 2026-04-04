class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first loop through the nums once 
        # count num of zeros and the nonzero product
        cnt_zeros = 0 
        prod = 1
        for num in nums:
            if num == 0:
                cnt_zeros += 1
            else:
                prod *= num 
        
        # init res arr 
        res = [0] * len(nums)

        # if we have more than or equal to two zeros in arr -> all zero array
        if cnt_zeros >= 2:
            return res

        # populate res arr
        for i, n in enumerate(nums):
            # if there is one zero in the arr
            # all the entries will be zero except the zero num
            if cnt_zeros:
                if n == 0:
                    res[i] = prod
                else:
                    res[i] = 0 
            # no zeros in arr -> entries are just prod // num (prod except self)
            else:
                res[i] = prod // n
        
        return res


