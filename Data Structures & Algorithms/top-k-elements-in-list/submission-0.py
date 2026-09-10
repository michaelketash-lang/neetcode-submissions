from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number -> O(N)
        count = Counter(nums)
        
        # Step 2: Create buckets where index = frequency
        # The size is len(nums) + 1 because the max possible frequency is len(nums)
        # freq[i] will store a list of numbers that appeared exactly 'i' times
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        # Step 3: Iterate backwards from the highest possible frequency (O(N))
        res = []
        # Start from end (len(nums)) down to 1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Once we collected k elements, we are done
                if len(res) == k:
                    return res
                    
        return res
        