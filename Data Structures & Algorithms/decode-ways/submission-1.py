from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            res = dp(i + 1)
            if i < len(s) - 1 :
                if (s[i] == '1' or s[i] == '2' and s[i + 1] < '7'):
                    res += dp(i + 2)
            return res
        
        return dp(0)