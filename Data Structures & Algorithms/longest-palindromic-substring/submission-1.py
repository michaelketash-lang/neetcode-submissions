class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = 0
        res = ""
        n = len(s)
        #scanning the string
        for i in range(n):
            l,r = i,i
            while l >= 0 and r < n and s[r] == s[l]:
                if max_pali < r-l+1:
                    max_pali = r - l + 1
                    res = s[l: r + 1]
                r += 1
                l -= 1
            l,r = i,i+1
            while l >= 0 and r < n and s[r] == s[l]:
                if max_pali < r-l+1:
                    max_pali = r - l + 1
                    res = s[l: r + 1]
                r += 1
                l -= 1
        return res