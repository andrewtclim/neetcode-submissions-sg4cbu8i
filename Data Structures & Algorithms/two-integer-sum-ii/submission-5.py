class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 

        while l < r:
            two_sum = numbers[l] + numbers[r]
            if two_sum == target:
                return [l+1, r+1]
            elif target > two_sum:
                l += 1
            else:
                r -= 1        