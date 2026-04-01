class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initalize pointers from both sides
        l, r = 0, len(numbers)-1

        while l < r:
            check = numbers[l] + numbers[r]
            if target == check:
                return [l+1, r+1]
            elif target > check:
                l += 1
            else:
                r -= 1
    