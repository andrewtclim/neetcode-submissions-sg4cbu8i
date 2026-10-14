class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # monotonically decreasing stack (top contains the coldest day, and bottom is warmest)
        stack = [] # (temp, index)
        res = [0] * len(temps) # each i=days in the array 

        for i, t in enumerate(temps):
            # found a warmer day -> process
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # append the new days (temp, index)
            stack.append((t, i))
        
        return res
