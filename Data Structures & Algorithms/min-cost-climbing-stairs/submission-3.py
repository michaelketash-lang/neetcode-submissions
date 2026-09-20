class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        memoization = {}
        def dp(i):
            if i <= 1:
                return 0
            
            if i in memoization:
                return memoization[i]
            
            memoization[i] = min(dp(i-1) + cost[ i - 1 ] , dp(i-2) + cost[i-2])
            return memoization[i]
        
        return dp(len(cost))
        