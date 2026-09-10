class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map: Key (Character Count Tuple) -> Value (List of words)
        # Example: (1, 0, 1, ...) -> ["eat", "tea", "ate"]
        res = defaultdict(list)
        
        for s in strs:
            # 1. Create a "fingerprint" array of 26 zeros
            # count[0] is for 'a', count[1] for 'b', etc.
            count = [0] * 26 
            
            # 2. Count frequency of each char in the current string
            for c in s:
                # ord(c) gives ASCII value. ord('a') is 97.
                # ord(c) - ord('a') maps 'a'->0, 'b'->1...
                count[ord(c) - ord('a')] += 1
            
            # 3. Convert list to Tuple so it can be a Dict Key! (CRITICAL STEP)
            # Lists are mutable and cannot be hashed. Tuples are immutable.
            key = tuple(count)
            
            # 4. Group the word
            res[key].append(s)
            
        return list(res.values())
