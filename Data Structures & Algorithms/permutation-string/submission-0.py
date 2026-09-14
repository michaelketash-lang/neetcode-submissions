class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n , m = len(s1) , len(s2)
        if n > m:
            return False
        
        need = {}
        for c in s1:
            need[c] = need.get(c,0) + 1
        window = {}
        for i in range(n):
            window[s2[i]] = window.get(s2[i],0) + 1

        if need == window:
            return True
        
        for r in range(n,m):
            window[s2[r]] = 1 +window.get(s2[r] , 0 )
            left = s2[r-n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == need:
                return True
        return False

        


        