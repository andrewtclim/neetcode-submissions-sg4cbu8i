class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init two pointers l and r 
        l = 0
        r = len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]
            # found target -> return the index pair that matches 
            if curSum == target:
                return [l+1, r+1]
            # curSum too small, must increase
            elif curSum < target:
                l += 1
            # otherwise decrease curSum 
            else:
                r -= 1
        
        
