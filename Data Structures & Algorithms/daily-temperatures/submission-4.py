class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init a monotonic decreasing stack and result arr 
        stack = [] # tuples of (index, temp) of cold waiting days
        res = [0] * len(temps)


        for i, t in enumerate(temps):
            # found a new hotter day than the prev waiting day 
            while stack and t > stack[-1][1]:
                # remove this waiting day and calc the # of days it took 
                waitIndex, waitTemp = stack.pop()
                res[waitIndex] = i - waitIndex
            # otherwise push the next waiting day 
            stack.append((i, t))
        
        return res