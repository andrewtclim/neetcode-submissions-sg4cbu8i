class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # init a stack and also a result arr
        stack = [] # (temp, index) -> monotonically decreasing s.t. stack[-1] = coldest day
        res = [0] * len(temps)

        # iter over temps 
        for i, t in enumerate(temps):
            # case when we find a new warm temp 
            # process all the colder days that came before it
            while stack and t > stack[-1][0]:
                waitTemp, waitIndex = stack.pop()
                # calc and update the wait process time 
                res[waitIndex] = i - waitIndex
            # otherwise we found a cold day that we push ontop of our stack 
            stack.append((t, i))
        
        return res 


