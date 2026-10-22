class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # (index, temp)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # found warmer day -> process
            while stack and stack[-1][1] < t:
                waitIndex, waitTemp = stack.pop()
                res[waitIndex] = i - waitIndex
            stack.append((i, t))
        
        return res