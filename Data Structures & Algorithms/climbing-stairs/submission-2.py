class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        for i in range(n):
            temp = b
            b = a+b
            a = temp
        return a
        """
        brute force-approach
        def climbStairs(self, n: int) -> int:
            if n ==0:
                return 1

            if n < 0:
                return 0
            return self.climbStairs(n-1) +self.climbStairs(n-2)

        """
        """
        class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.memo_dfs(n, memo)

    def memo_dfs(self, n: int, memo: dict) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        # if already computed → return it
        if n in memo:
            return memo[n]
        
        # compute and store
        memo[n] = self.memo_dfs(n - 1, memo) + self.memo_dfs(n - 2, memo)
        return memo[n]

        """