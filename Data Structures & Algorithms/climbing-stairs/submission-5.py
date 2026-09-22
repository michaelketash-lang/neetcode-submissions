class Solution:
    def climbStairs(self, n: int) -> int:
        #lets look at a smaller example according to contstraints:
        # n = 1 we have only one option to climb to the 1st stair
        # n = 2 we have two options to climb to the 2nd stair.
        # lets look at n = 4 we have :
        # 1 + 1 + 1 + 1 =4
        # 1 + 1 + 2 = 4
        # 1 + 2 + 1 = 4
        # 2 + 1 + 1 = 4
        # 2 + 2 = 4
        # series of the stairs : 1 , 2 ,3 ,5
        res1 , res2 = 1 , 2
        for _ in range(1 , n):
            res1 , res2 = res2 , res1 + res2
        
        return res1