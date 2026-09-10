class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        lst = [0]*(n+ 1) # initialize a n+1 array
        for i in range(2,n+1):
            #checking if taking 2 stairs or 1 is better
            lst[i] = min(cost[i-1]+lst[i-1],cost[i-2]+lst[i-2]) 
        return lst[n]
       
