class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first iteration to count zeros and calc non-zero prod 
        cnt_zeros = 0 
        prod = 1
        for num in nums:
            if num == 0:
                cnt_zeros += 1
            else:
                prod *= num 
        
        # init res array
        res = [0] * len(nums)

        # if there are two or more zeros in nums -> all subprod = 0
        if cnt_zeros >= 2:
            return res
        
        # second iteration for any arr with one or less zeros
        for i, num in enumerate(nums):
            # for arrays w/ just one zero: all sub prods are zero except that index with a zero 
            if cnt_zeros:
                if num == 0:
                    res[i] = prod
                else:
                    res[i] = 0 
            else:
                res[i] = prod // num
        
        return res
                

