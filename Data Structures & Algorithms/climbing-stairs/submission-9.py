class Solution:
    def climbStairs(self, n: int) -> int:
        stair1 , stair2 = 1 , 2
        if n == 1:
            return stair1
        
        if n == 2:
            return stair2
        
        for _ in range(3 , n + 1):
            stair1 , stair2 = stair2 , stair1 + stair2
        
        return stair2