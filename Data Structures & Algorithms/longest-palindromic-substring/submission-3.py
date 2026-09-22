class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest , indx = 0 , 0
        for i in range(len(s)):
            # we need to check for odd sequence
            l , r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window >= longest:
                    longest = window
                    indx = l
                l -= 1
                r += 1
            
            l , r = i , i + 1
            # we need to check for even sequence
            while l >= 0 and r < len(s) and s[l] == s[r]:
                window = r - l + 1
                if window >= longest:
                    longest = window
                    indx = l
                l -= 1
                r += 1
        
        return s[indx : longest + indx]
            