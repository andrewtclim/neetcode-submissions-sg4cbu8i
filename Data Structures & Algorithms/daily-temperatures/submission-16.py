class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0]*len(temps)

        for i, t in enumerate(temps):
            # process colder days
            while stack and stack[-1][0] < t:
                waitTemp, waitIndex = stack.pop()
                res[waitIndex] = i - waitIndex
            # add current day to stack 
            stack.append((t, i))
        
        return res 

        