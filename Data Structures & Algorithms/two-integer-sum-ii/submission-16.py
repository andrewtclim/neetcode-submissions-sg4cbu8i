class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init left pointer and right pointer 
        l, r = 0, len(numbers)-1

        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            elif target > cur:
                l += 1
            else:
                r -= 1