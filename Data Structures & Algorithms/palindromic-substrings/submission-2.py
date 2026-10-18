class Solution:
    def countSubstrings(self, s: str) -> int:
        # Approach : expand from the middle
        res = 0
        for i in range(len(s)):
            # what if we have odd sequence
            l , r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # what if we have even sequence

            l , r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res

