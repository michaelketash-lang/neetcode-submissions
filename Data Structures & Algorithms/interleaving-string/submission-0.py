class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        cache = {}
        def dp(i , j):
            if i >= len(s1) and j >= len(s2):
                return True
            
            if (i,j) in cache:
                return cache[(i , j)]
            
            answer = False

            if i < len(s1) and s1[i] == s3[i + j]:
                answer = answer or dp(i + 1 , j)
            
            if j < len(s2) and s2[j] == s3[i + j]:
                answer = answer or dp(i , j + 1)
            
            cache[(i,j)] = answer
            return cache[(i,j)]
        
        return dp(0 , 0)