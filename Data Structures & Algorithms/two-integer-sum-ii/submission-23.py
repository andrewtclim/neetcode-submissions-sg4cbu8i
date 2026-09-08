class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init two pointers 
        l, r = 0, len(numbers)-1

        # iter over numbers 
        while l < r:
            # check current sum
            curSum = numbers[l] + numbers[r]
            # found sum -> return indicies 
            if curSum == target:
                return [l+1, r+1]
            # curSum is too small and we must increase it 
            elif curSum < target:
                l += 1
            # otherwise its too big and we must decrease it
            else:
                r -= 1
        
