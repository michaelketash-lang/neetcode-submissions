class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m = len(s1)
        n = len(s2)
        prev = [False for _ in range(n + 1)]

        prev[n] = True

        for i in range(m , -1 , -1):
            cur = [False for _ in range(n + 1)]
            if i == m:
                cur[n] = True
            
            for j in range(n , -1 ,-1):
                if i < m and s1[i] == s3[i + j] and prev[j]:
                    cur[j] = True
                
                if j < n and s2[j] == s3[i + j] and cur[j + 1]:
                    cur[j] = True
            
            prev = cur
        
        return prev[0]