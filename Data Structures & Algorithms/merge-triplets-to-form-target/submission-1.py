class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                for i ,v in enumerate(t):
                    if v == target[i]:
                        good.add(i)
        
        return len(good) == 3
            
        