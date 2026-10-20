class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        longest = 0

        for c in charSet:
            left = 0
            count = 0
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                
                while count > k:
                    if s[left] != c:
                        count -= 1
                    left += 1
                
                longest = max(longest, r - left + 1)
        
        return longest