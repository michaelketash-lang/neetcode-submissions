class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to avoid the sorting so lets count freq
        res = defaultdict(list)
        # scan the words
        for word in strs:
            buckets = [0] * 26
            # count the letters in each word
            for letter in word:
                buckets[ord(letter) - ord('a')] += 1
            # insert to the hashmap and converting key to tuple to be immutable
            res[tuple(buckets)].append(word)
        # convert to the required type
        return list(res.values())