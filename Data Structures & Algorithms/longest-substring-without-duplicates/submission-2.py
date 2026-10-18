class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        res = 0
        l = 0
        for r,c in enumerate(s):
            while c in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(c)
            window = r - l + 1
            res = max(res , window)
        
        return res
