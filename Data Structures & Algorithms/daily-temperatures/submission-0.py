class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stk=[]
        for i,j in enumerate(temperatures):
            while stk and j>stk[-1][0]:
                stkk, stki=stk.pop()
                res[stki]=i-stki
            stk.append((j,i))
        return res
        