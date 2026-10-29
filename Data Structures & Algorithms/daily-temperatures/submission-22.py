class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0] * len(temps)

        for i, t in enumerate(temps):
            # warmer day, process all colder days 
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # colder days, get pushed on top (wait to be processed)
            stack.append((t, i))

        return res

