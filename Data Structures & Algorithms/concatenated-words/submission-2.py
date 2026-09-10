class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        dp = {}
        hashSet = set(words)
        def dfs(word):
            if word in dp:
                return dp[word]
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in hashSet and suffix in hashSet) or (prefix in hashSet and dfs(suffix))):
                    dp[word] = True
                    return True
            dp[word] = False
            return False
        for w in words:
            if dfs(w):
                res.append(w)
        return res