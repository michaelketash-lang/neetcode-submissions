class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(n):
            temp = b
            b = a+b
            a = temp
        return a
