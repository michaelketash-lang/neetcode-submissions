class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #memoization
        n = len(cost)
        dp = {0:0,1:0}
        def dfs(i):
            if i in dp:
                return dp[i]
            else:
                dp[i] = min(cost[i-2]+dfs(i-2),cost[i-1]+dfs(i-1)) 
                return dp[i]
        return dfs(n)