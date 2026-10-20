class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case:
        if len(strs) == 1:
            return strs[0]
        
        s = sorted(strs)
        min_length = min(len(s[0]) , len(s[-1]))

        for i in range(min_length):
            word1 = s[0]
            word2 = s[-1]
            if word1[i] != word2[i]:
                return word1[:i]
        
        return s[0]