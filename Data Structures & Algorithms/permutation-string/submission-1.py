class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # step 1: if the length s1 is bigger than it cant be a substring of s2
        n , m = len(s1) , len(s2)
        if n > m:
            return False
        # step 2: count frequencies of s1
        need = {}
        for c in s1:
            need[c] = need.get(c,0) + 1
        # step 3: count frequencies of fixed size window
        window = {}
        for i in range(n):
            window[s2[i]] = window.get(s2[i],0) + 1
        # check if they are the same
        if need == window:
            return True
        # if we extend the window from the right we need ro reduce from the left
        for r in range(n,m):
            window[s2[r]] = 1 +window.get(s2[r] , 0 )
            left = s2[r-n]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
        # check if there is a match
            if window == need:
                return True
        return False

        


        