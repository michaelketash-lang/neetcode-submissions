class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force will be to sort it
        res = defaultdict(list)
        for word in strs:
            sorted_word = sorted(word)
            res[tuple(sorted_word)].append(word)
        
        return list(res.values())
