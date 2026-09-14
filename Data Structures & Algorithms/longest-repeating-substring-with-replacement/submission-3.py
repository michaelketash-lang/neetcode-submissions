class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_bank =  set(s)

        for c in char_bank:
            replaced = l = 0
            for r in range(len(s)):
                if c != s[r]:
                    replaced += 1
                while replaced > k :
                    if c != s[l]:
                        replaced -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res