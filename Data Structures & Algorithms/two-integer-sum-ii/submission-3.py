class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initalize two pointers 
        l, r = 0, len(numbers)-1

        while r > l:
            curSum = numbers[l] + numbers[r]

            if curSum == target:
                return [l+1, r+1]
            elif curSum < target:
                l += 1
            else:
                r -= 1

        