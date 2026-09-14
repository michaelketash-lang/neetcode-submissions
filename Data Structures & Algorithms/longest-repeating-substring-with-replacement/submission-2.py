class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # its a bit greedy a bit sliding window
        res = 0
        chars = set(s)

        for c in chars:
            l = count = 0
            for r in range(len(s)):
                if s[r] != c:
                    count += 1
                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1
                res = max(res,r - l + 1)
        return res