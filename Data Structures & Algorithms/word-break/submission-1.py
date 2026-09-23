from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i == len(s):
                return True
            
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    if dp(i + len(word)):
                        return True
            return False
        
        return dp(0)