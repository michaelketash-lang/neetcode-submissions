class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1) , len(word2)

        if m < n:
            m , n = n , m
            word1 , word2 = word2 , word1
        
        prev = [0] * (n + 1)
        for i in range(n + 1):
            prev[i] = n - i
        
        dp = [0] * (n + 1)
        for i in range(m - 1 , -1 , -1):
            dp[n] = m - i

            for j in range(n - 1 , -1 ,-1):
                if word1[i] == word2[j]:
                    dp[j] = prev[j + 1]
                else:
                    dp[j] = 1 + min(dp[j + 1], prev[j + 1] , prev[j])
            
            prev = dp[:]
        
        return prev[0]