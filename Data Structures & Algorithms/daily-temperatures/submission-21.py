class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init stack and res
        stack = []
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            while stack and stack[-1][1] < t:
                waitIndex, waitTemp = stack.pop()
                res[waitIndex] = i - waitIndex
            stack.append((i, t))
        
        return res