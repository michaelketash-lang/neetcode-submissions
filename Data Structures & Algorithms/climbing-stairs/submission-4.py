class Solution:
    def climbStairs(self, n: int) -> int:
        num1 , num2 = 1 , 2
        for i in range(1 , n):
            num1 , num2 = num2 , num1 + num2
        
        return num1

        