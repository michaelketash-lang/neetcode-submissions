class Solution:


    def isPalindrom(self, s:str , i: int , j:int):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


    def partition(self, s: str) -> List[List[str]]:
        res , part = [] ,[]
        
        def dfs(i , j):
            if j >= len(s):
                if i == j:
                    res.append(part[:])
                return
            
            if self.isPalindrom(s, i , j):
                part.append(s[i : j + 1])
                dfs(j + 1 , j + 1)
                part.pop()
            
            dfs(i , j + 1 )
        dfs(0 , 0)
        return res
            

            
        

