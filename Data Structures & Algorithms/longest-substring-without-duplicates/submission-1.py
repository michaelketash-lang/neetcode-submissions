class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        window_size = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            window_size = max(window_size, r - l + 1)
        return window_size